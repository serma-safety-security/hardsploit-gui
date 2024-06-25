"""nrf_sniffer.py"""

from struct import pack
from time import sleep

from PySide6.QtCore import Slot, QThreadPool, QRunnable
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox, QTreeWidgetItem
from PySide6.QtWidgets import QMenu, QInputDialog

from hardsploit.core import HardsploitUtils, HardsploitError
from hardsploit.modules import NRF24L01

from hardsploit_gui.db.models import Command, Bus, Byte

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_nrf24l01_sniffer import Ui_NrfSniffer


class NrfSniffer(QWidget):
    """Sniffing window for NRF24L01 Module."""
    def __init__(self, chip, hardsploit_api):
        # Initialize the GUI
        super().__init__()

        self.view = Ui_NrfSniffer()
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)

        self._api = hardsploit_api
        self.chip = chip
        self._thread_pool = QThreadPool()
        self._receiver = None
        self.filepath = None
        self.stop_recv()  # Reset reception elements to known state

        # Settings should be filled in before using the sniffer
        if not self.chip.nrf_settings:
            self.view.btn_recv.setDisabled(True)
            QMessageBox(QMessageBox.Warning, "Empty Settings",
                        "No settings have been set. Please specify settings in the 'Settings' section first."
                        ).exec_()
        else:
            # Retrieve settings from the database
            nrf_settings = self.chip.nrf_settings[0]
            self.address = int(nrf_settings.address, 16)
            self.channel = nrf_settings.channel
            self.view.lbl_address.setText(f"0x{self.address:x}")
            self.view.lbl_channel.setText(f"{self.channel}")

        # Resize the data column with enough width to display 16 hexadecimal bytes (so 32 chars)
        char_width = self.view.tree_recv.fontMetrics().bounding_rect('A').right() + 2
        self.view.tree_recv.setColumnWidth(1, len("AA" * 16) * char_width)

    def closeEvent(self, event):
        # Stop any currently running sniffing thread
        self.stop_recv()
        self._thread_pool.clear()
        event.accept()

    def contextMenuEvent(self, event):
        # Add an option to save a frame as a command
        # ContextMenu deploys only on the frame (topLevelItem)

        item = self.view.tree_recv.currentItem()
        if self.view.tree_recv.indexOfTopLevelItem(item) < 0:
            return

        add_command = QAction("Save frame as command")
        add_command.triggered.connect(self.add_frame_as_command)

        menu = QMenu(self)
        menu.addAction(add_command)
        menu.exec_(event.globalPos())

    @Slot()
    def add_frame_as_command(self):
        """Save the currently selected frame as a command."""
        valid_cmd_name = False
        command_name = None

        frame = self.view.tree_recv.currentItem()
        bus_id = Bus.get(Bus.name == 'NRF24L01').id

        # Ask the user for a command name and retry in case of invalid name
        while not valid_cmd_name:
            command_name, ok = QInputDialog.getText(self, "Add frame as command", "Command name")
            if not ok:
                # Abort if user cancels
                return

            if not command_name:
                QMessageBox.critical(self, "Empty command name", "Please enter a command name")
            elif self.chip.commands.where(Command.bus == bus_id).where(Command.name == command_name).count():
                QMessageBox.critical(self, "Error", "A command already exists with this name.\nPlease specify another command name.")
            else:
                valid_cmd_name = command_name

        # Retrieve frame data as hexpairs
        data = []
        for idx in range(frame.childCount()):
            item = frame.child(idx)
            hex_data = item.text(1)

            # Take each hexpair and add then to the data list
            data += [hex_data[i:i+2] for i in range(0, len(hex_data), 2)]


        # Register the command
        command = Command(
                name=command_name,
                description="",
                chip=self.chip,
                bus=bus_id
            )
        command.save()

        command_id = command.get_id()

        for i, hexpair in enumerate(data):
            b = Byte(
                    position=i+1,
                    value=hexpair,
                    description="",
                    command=command_id
                )
            b.save()

        QMessageBox.information(self, "Command Saved", f"Successfully saved command: '{command_name}'")

    def save_data_to_file(self, filepath):
        """Save the data currently stored in the QTreeWidget into the given filepath."""
        with open(filepath, "wb") as f:
            for item_id in range(self.view.tree_recv.topLevelItemCount()):
                frame = self.view.tree_recv.topLevelItem(item_id)
                # Retrieve the 2nd column text of all children (data lines)
                # of each top level items (frame) in the tree.
                for line_id in range(frame.childCount()):
                    data_hex = frame.child(line_id).text(1)
                    f.write(bytes.fromhex(data_hex))


    @Slot()
    def select_read_file(self):
        """Select a file to stores the data into."""
        self.filepath = QFileDialog.getSaveFileName(self, 'Select a file', '/', '*.*')[0]
        if self.filepath:
            self.view.lbl_selected_file.setText(str(self.filepath).split("/")[-1])

    @Slot()
    def stop_recv(self):
        """Stop the reception of the NRF module and reset related GUI elements to initial state."""
        if self._receiver:
            self._receiver.stop()
            self._receiver = None

            # Save data to file
            if self.filepath:
                self.save_data_to_file(self.filepath)

        # Reset Receiving button into default state
        self.view.btn_recv.clicked.disconnect()

        self.view.btn_recv.setText("Receive")
        self.view.btn_recv.clicked.connect(self.recv)

    @Slot()
    def add_received_data(self, data):
        """Add new data into the QTreeWidget."""

        n_frames = self.view.tree_recv.topLevelItemCount()
        frame = QTreeWidgetItem(self.view.tree_recv, (f"frame {n_frames}", "", f"{len(data)} bytes"))
        frame.setExpanded(True)

        # New line
        addr = 0
        # Add all complete lines in data
        for idx in range(0, len(data) - 16, 16):
            data_line = data[idx:idx+16]
            self._add_new_line(frame, addr, data_line)
            addr += 16

        # And add the remaining bytes
        data_line = data[addr:]
        self._add_new_line(frame, addr, data_line)

    def _add_new_line(self, frame, addr, data):
        """Add a new line of data in the QTreeWidget."""
        item = QTreeWidgetItem((
                f"0x{addr:04x}",
                data.hex(),
                bytes_to_ascii(data)
            ))
        frame.addChild(item)
        self.view.tree_recv.scrollToBottom()  # Auto scrolling

    @Slot()
    def recv(self):
        """Start sniffing."""
        self.view.tree_recv.clear()

        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        Firmware('SPI', self._api)

        # Update the start button so it can stop the sniffing
        self.view.btn_recv.clicked.disconnect()
        self.view.btn_recv.setText("Stop")
        self.view.btn_recv.clicked.connect(self.stop_recv)
        self._receiver = NrfReceiver(self, self._api, self.channel, self.address)

        # Start the sniffing thread
        self._thread_pool.start(self._receiver)


def bytes_to_ascii(data):
    """Convert a bytes object to its ASCII representation for display in a hexdump.

    Only characters representing a letter, a symbol or a single whitespace are
    represented (char code in range [0x20, 0x7e]). Any other char is replaced by a dot ('.').
    """
    def to_ascii(b):
        """Function to convert a single byte to its ascii representation."""
        if 0x20 <= b <= 0x7e:
            return chr(b)
        else:
            return '.'

    # Transform each character in the bytes using the `to_ascii` function
    # And joining the produced list into a string
    return ''.join(map(to_ascii, data))


class NrfReceiver(QRunnable):
    """A Class implementing a Sniffer runnable in a separate thread using
    the NRF hardsploit through the HardsploitAPI.
    """
    def __init__(self, parent, hardsploit_api, channel, address):
        QRunnable.__init__(self)

        self._parent = parent
        self._api = hardsploit_api
        self._channel = channel
        self._address = address
        self._running = False

    @Slot()
    def stop(self):
        """Stop the sniffer from sniffing."""
        self._running = False

    @Slot()
    def run(self):
        """The QRunnable method, launch the sniffing."""
        # Try to connect to the NRF module through SPI
        # (Hardsploit bitstream should have been set before)

        try:
            nrf = NRF24L01(self._api)

            if nrf.reset():
                # TODO: Do the conversion in the API
                addr = [byte for byte in pack(">Q", self._address) if byte]

                nrf.init_drone(self._channel, addr)
            else:
                self._parent.stop_recv()
                return QMessageBox(QMessageBox.Critical, "NRF24L01 Error", "NRF24L01 Not found").exec_()
        except HardsploitError.HardsploitNotFound:
            self._parent.stop_recv()
            return ErrorMsg.hardsploit_not_found()
        except HardsploitError.USBError:
            self._parent.stop_recv()
            return ErrorMsg.usb_error()

        self._running = True

        sniff_delay = 0.25  # Sleeping time between iterations

        nrf.flush_rx()
        nrf.flush_tx()


        while self._running:
            # Awaiting receiving a new frame
            frame_data = bytes(nrf.read())
            if len(frame_data) > 0:
                self._parent.add_received_data(frame_data)

            sleep(sniff_delay)
