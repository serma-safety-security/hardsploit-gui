"""swd.py"""

from PySide6.QtWidgets import QMessageBox
from hardsploit.core import HardsploitUtils, HardsploitError
from hardsploit.modules.swd.swd import HardsploitSWD

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.progress_bar import ProgressBar


class Swd:

    def __init__(self, chip, console, hardsploit_api):
        if HardsploitUtils.get_number_of_board_available() > 0:
            self.console = console
            self.chip = chip
            self._api = hardsploit_api
        else:
            QMessageBox(QMessageBox.Critical, "Error", "Hardsploit not plugged. Operation canceled").exec_()

    def do_swd_action(self, action, **option):
        try:
            Firmware('SWD', self._api)
            api = HardsploitSWD(
                memory_start_address=self.chip.swd_settings[0].memory_start_address,
                memory_size_address=self.chip.swd_settings[0].memory_size_address,
                cpu_id_address=self.chip.swd_settings[0].cpu_id_address,
                device_id_address=self.chip.swd_settings[0].device_id_address,
                hardsploit_api=self._api
            )
            if not api:
                return 0
            if action == 'detect':
                return api.obtain_codes()
            elif action == 'read':
                utils.progress_bar = ProgressBar(f"SWD: {action}...")
                utils.progress_bar.show()
                api.dump_flash(option['filepath'])
                return True
            elif action == 'write':
                utils.progress_bar = ProgressBar(f"SWD: {action}...")
                utils.progress_bar.show()
                api.write_flash(option['filepath'])
                return True
            elif action == 'erase':
                api.erase_flash()
        except HardsploitError.HardsploitNotFound:
            ErrorMsg.hardsploit_not_found()
        except Exception as e:
            ErrorMsg.custom("SWD Error", "Check wiring!")
            return None

    def detect(self):
        code = self.do_swd_action('detect')
        if code:
            self.console.print('New action: SWD Detect')
            QMessageBox(QMessageBox.Information, "SWD detection",
                        "Detected:\n" +
                        f"DP.IDCODE:  0x{hex(code['DebugPortId'])[2:].upper()}\n" +
                        f"AP.IDCODE:  0x{hex(code['AccessPortId'])[2:].upper()}\n" +
                        f"CPU ID:     0x{hex(code['CpuId'])[2:].upper()}\n"
                        ).exec_()

    def read(self, filepath):
        if self.do_swd_action('read', filepath=filepath):
            QMessageBox(QMessageBox.Information, "SWD Read Action", "Dump finished").exec_()
            utils.progress_bar.close()

    def write(self, filepath):
        if self.do_swd_action('write', filepath=filepath):
            QMessageBox(QMessageBox.Information, "SWD Write Action", "Write finished").exec_()
            utils.progress_bar.close()

    def erase(self):
        msg = QMessageBox()
        msg.setWindowTitle("Delete the data")
        msg.setText("You are going to delete all the data. Continue?")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            if self.do_swd_action('erase'):
                QMessageBox(QMessageBox.Information, "SWD Erase Action", "Erase finished").exec_()
