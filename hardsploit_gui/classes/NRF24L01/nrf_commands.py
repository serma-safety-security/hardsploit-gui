"""nrf_commands.py"""

from struct import pack

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMessageBox, QProgressDialog
from PySide6.QtWidgets import QInputDialog

from hardsploit.core import HardsploitError
from hardsploit.modules import NRF24L01

from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.generic_commands import GenericCommands


class NrfCommands(GenericCommands):
    """Custom commands window for NRF24L01 commands."""
    def __init__(self, chip, hardsploit_api):
        GenericCommands.__init__(self, chip, 'NRF24L01', hardsploit_api)

        # Settings should be filled in before using Commands
        if not self.chip.nrf_settings:
            self.view.btn_recv.setDisabled(True)
            QMessageBox.warning(self, "Empty Settings",
                                "No settings have been set. Please specify settings in the 'Settings' section first.")
        else:
            # Retrieve settings from the database
            nrf_settings = self.chip.nrf_settings[0]
            self.address = int(nrf_settings.address, 16)
            self.channel = nrf_settings.channel
            self.view.lbl_chip.setText(f"{chip.reference} | 0x{self.address:x} - {self.channel}")

    def _get_context_actions(self):
        return (self.view.actionExecute,
                self.view.actionExecute_n,
                self.view.actionEdit,
                self.view.actionTemplate,
                self.view.actionDelete,
                )

    @Slot()
    def execute_n(self):
        """Slot that should be executed when the user want to send
        multiple frames at once.
        """
        # Ask the user for the number of times to send the frame
        n, ok = QInputDialog.getInt(self, "Execute n times", "Number of times", 10, 1)

        cmd_array = self.prepare_cmd()
        self._exec_cmd(cmd_array, n)

    def _exec_cmd(self, array_sent, times=1):
        """Low level command execution.
        Takes the array of bytes to send through the NRF24L01
        and the number of times to send the frame.
        """
        # Load the firmware
        Firmware('SPI', self._api)

        # Display progress bar showing the progress of the sending process
        progress = QProgressDialog(f"Sending {times} frame{'s' if times > 1 else ''}", "", 0, times)
        progress.setWindowModality(Qt.WindowModal)
        progress.setAutoClose(False)
        progress.setAutoReset(False)
        progress.setCancelButton(None)
        progress.forceShow()

        try:
            nrf = NRF24L01(self._api)

            if nrf.reset():
                # TODO: Do the conversion in the API
                addr = [byte for byte in pack(">Q", self.address) if byte]

                nrf.init_drone(self.channel, addr)

                nrf.flush_rx()
                nrf.flush_tx()

                for i in range(times):
                    nrf.send(array_sent)
                    progress.setValue(i+1)
            else:
                progress.cancel()
                return QMessageBox.crititcal(self, "NRF24L01 Error", "NRF24L01 Not found")
        except HardsploitError.HardsploitNotFound:
            progress.cancel()
            return ErrorMsg.hardsploit_not_found()
        except HardsploitError.USBError:
            progress.cancel()
            return ErrorMsg.usb_error()
        except Exception as e:
            ErrorMsg.unknown(e)
            progress.cancel()


        if times > 1:
            progress.close()
        else:
            # Let the window open as a confirmation that the frame has been sent
            # when sending only 1 frame
            progress.setCancelButtonText("Close")
