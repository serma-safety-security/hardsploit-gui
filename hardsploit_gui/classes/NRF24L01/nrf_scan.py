"""nrf_scan.py"""

from time import time
from struct import pack

from PySide6.QtCore import Slot, QThreadPool, QRunnable
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit.core import HardsploitUtils, HardsploitError
from hardsploit.modules import NRF24L01

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_nrf24l01_scan import Ui_NRF24L01_scan


class NrfScan(QWidget):
    """Scanning window for NRF24L01 Module"""
    def __init__(self, chip, hardsploit_api=None):
        # Initialize the GUI
        super().__init__()
        self.view = Ui_NRF24L01_scan()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)

        self.chip = chip

        # Attributes used for channel scanning
        self._thread_pool = QThreadPool()
        self._scanner = None
        self.stop_scan()  # Reset scanning in a known state

        # Populate address parameter from database if available
        if chip.nrf_settings:
            self.view.lie_addr.setText("0x" + str(self.chip.nrf_settings[0].address))

    def close_event(self, event):
        # Stop any currently running scanning thread
        self.stop_scan()
        self._thread_pool.clear()
        event.accept()

    @Slot()
    def save_settings(self):
        """Save settings given in the form into the database."""
        # Save new settings in database or edit existing ones
        if self.chip.spi_settings:
            self.update()
        else:
            self.create()

    @Slot()
    def channel_scan(self):
        """Launch a channel scan"""
        # Get parameters from the form
        address = int(self.view.lie_addr.text(), 16)
        min_chan = self.view.spin_min_chan.value()     # First channel to test
        max_chan = self.view.spin_max_chan.value()     # Last channel to test
        time_step = self.view.dspin_time_step.value()  # The amount of time to wait for data before testing the next channel
        if min_chan > max_chan:
            # Sanity check
            QMessageBox(QMessageBox.Critical, "Value Error",
                        "Minimal channel should be less than Maximum channel").exec_()
            return

        self.view.list_scan.clear()
        self.scan_update_status("Starting scan")
        self._scanner = NrfChannelScanner(self, self._api, address, min_chan, max_chan, time_step)

        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        Firmware('SPI', self._api)

        # Update the button, so it can be used to stop the scan
        self.view.btn_scan.setText("Stop")
        self.view.btn_scan.clicked.disconnect()
        self.view.btn_scan.clicked.connect(self.stop_scan)

        # Start the Scanning thread
        self._thread_pool.start(self._scanner)

    @Slot()
    def stop_scan(self):
        """Stop any running scan and reset the related GUI elements to the default state."""
        if self._scanner:
            self._scanner.stop()
            self._scanner = None

        # Reset the scan button to the default state
        self.view.btn_scan.setText("Scan")
        self.view.btn_scan.disconnect(self.view.btn_scan)
        self.view.btn_scan.clicked.connect(self.channel_scan)

    @Slot()
    def scan_update_status(self, status):
        """Update the status element in the scan list.

        The last element in the scan list is used as a status message.
        """
        nb_elt = self.view.list_scan.count()
        if nb_elt:
            self.view.list_scan.item(nb_elt-1).setText(" ... " + status)
        else:
            # If the list is empty create a new element
            self.view.list_scan.addItem(" ... " + status)

    @Slot()
    def scan_add_item(self, item):
        """Add a new item in the scan list"""
        # Insert the element just before the last element (which is the status message)
        idx = self.view.list_scan.count() - 1
        self.view.list_scan.insertItem(idx, item)


class NrfChannelScanner(QRunnable):
    """A Class implementing a Scanner runnable in a separate thread
    using the NRF module through the HardsploitAPI.
    """
    def __init__(self, parent, hardsploit_api, address, min_chan=0, max_chan=126, step_time_secs=1):
        QRunnable.__init__(self)
        self._api = hardsploit_api
        self._parent = parent
        self.address = address
        self.min_chan = min_chan
        self.max_chan = max_chan
        self.step_time = step_time_secs
        self._running = False

    def stop(self):
        """Used to stop a running scan."""
        self._running = False

    def run(self):
        """The QRunnable method, launch the scan."""
        nrf = None
        # Try to connect to the NRF module through SPI
        # (Hardsploit bitstream should have been set before)
        exception_happened = True
        try:
            nrf = NRF24L01(self._api)
            if nrf.reset():
                # TODO: Do the conversion in the API
                addr = [byte for byte in pack(">Q", self.address) if byte]

                nrf.init_drone(self.min_chan, addr)
            else:
                QMessageBox(QMessageBox.Critical, "NRF24L01 Error", "NRF24L01 Not found").exec_()
                self._parent.scan_update_status("Error")
                self._parent.stop_scan()
        except HardsploitError.HardsploitNotFound:
            ErrorMsg.hardsploit_not_found()
        except HardsploitError.USBError:
            ErrorMsg.usb_error()
        else:
            exception_happened = False

        if exception_happened:
            # If any exception is caught, stop the scan
            self._parent.stop_scan()
            self._parent.scan_update_status("Error")
            return

        self._running = True
        # Iterate over each desired channels
        for channel in range(self.min_chan, self.max_chan + 1):
            self._parent.scan_update_status(f"Scanning channel {channel}")
            nrf.flush_tx()
            nrf.flush_rx()
            nrf.change_channel(channel)

            time_start = time()
            while self._running and time() - time_start < self.step_time:
                data = nrf.read()
                if len(data) > 0:
                    self._parent.scan_add_item(f"Data found on channel {channel}")
                    break

            if not self._running:
                break

        self._parent.scan_update_status("Scan over")
        self._parent.stop_scan()
