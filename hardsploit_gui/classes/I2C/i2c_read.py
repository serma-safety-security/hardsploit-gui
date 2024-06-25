"""i2c_read.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox
from pathlib import Path

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.progress_bar import ProgressBar
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.gui.gui_generic_read import Ui_Generic_read
from hardsploit.core import HardsploitUtils
from hardsploit.modules import HardsploitI2c


class I2cRead(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_Generic_read()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_start, 0)
        input_restrict(self.view.lie_stop, 0)
        self.chip = chip
        self.filepath = None

    @Slot()
    def select_read_file(self):
        try:
            self.filepath = QFileDialog.getSaveFileName(self, 'Select a file', '/', '*.*')[0]
            if self.filepath:
                self.view.btn_read.setEnabled(True)
                self.view.lbl_selected_file.setText(str(self.filepath).split("/")[-1])
        except Exception as e:
            ErrorMsg.unknown(e)

    @Slot()
    def read(self):
            if HardsploitUtils.get_number_of_board_available() < 1:
                return ErrorMsg.hardsploit_not_found()
            if self.filepath:
                utils.file = open(self.filepath, 'wb')
            if self.view.rbn_full.isChecked():
                if not self.control_read_settings('full'):
                    return False
                start = 0
                stop = self.chip.i2c_settings[0].total_size - 1
                control = self.chip.i2c_settings[0].total_size
            else:
                if not self.control_read_settings('partial'):
                    return False
                start = int(self.view.lie_start.text())
                stop = int(self.view.lie_stop.text())
                control = (stop - start) + 1
            Firmware('I2C', self._api)
            utils.progress_bar = ProgressBar("I²C: Reading...")
            utils.progress_bar.show()

            speed = 0
            if self.chip.i2c_settings[0].frequency in [40, 100, 400, 1000]:
                if self.chip.i2c_settings[0].frequency == 100:
                    speed = 0
                elif self.chip.i2c_settings[0].frequency == 400:
                    speed = 1
                elif self.chip.i2c_settings[0].frequency == 1000:
                    speed = 2
                elif self.chip.i2c_settings[0].frequency == 40:
                    speed = 3
                i2c = HardsploitI2c(speed=speed, hardsploit_api=self._api)
                i2c.i2c_generic_dump(
                    i2c_base_address=int(self.chip.i2c_settings[0].address_w, base=16),
                    start_address=start,
                    stop_address=stop,
                    size_max=self.chip.i2c_settings[0].total_size
                )
            utils.file.close()
            if control != Path(self.filepath).stat().st_size:
                ErrorMsg.filesize_error()
            else:
                utils.progress_bar.close()
                self.close()
                QMessageBox(QMessageBox.Information, 'I2C read', "Memory read successfully!\r\n"
                                                                 f"File location: {self.filepath}").exec_()

    @Slot()
    def control_read_settings(self, type):
        if not self.chip.i2c_settings:
            return ErrorMsg.settings_missing()
        if not self.chip.i2c_settings[0].frequency:
            return ErrorMsg.frequency_missing()
        if not self.chip.i2c_settings[0].total_size:
            return ErrorMsg.full_size_error()
        if self.chip.i2c_settings[0].total_size == 0:
            return ErrorMsg.full_size_error()
        if type == 'partial':
            if self.view.lie_start.text() == "":
                return ErrorMsg.start_stop_missing()
            if self.view.lie_stop.text() == "":
                return ErrorMsg.start_stop_missing()
            start = int(self.view.lie_start.text())
            stop = int(self.view.lie_stop.text())
            total_size = self.chip.i2c_settings[0].total_size
            if start == stop:
                return ErrorMsg.start_neq_stop
            if start > stop:
                return ErrorMsg.start_inf_to_stop
            if start > (total_size - 1):
                return ErrorMsg.inf_to_total_size
            if stop > (total_size - 1):
                return ErrorMsg.inf_to_total_size
        return True
