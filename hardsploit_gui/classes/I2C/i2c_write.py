"""i2c_write.py"""

from hardsploit.core import HardsploitUtils
from hardsploit.modules import HardsploitI2c
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.progress_bar import ProgressBar
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.gui.gui_generic_write import Ui_Generic_write


class I2cWrite(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_Generic_write()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_start, 0)
        self.chip = chip
        self.filepath = None

    @Slot()
    def select_write_file(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Select a file', '/', '*.*')[0]
        if self.filepath:
            self.view.btn_write.setEnabled(True)
            self.view.lbl_selected_file.setText(str(self.filepath).split('/')[-1])

    @Slot()
    def write(self):
        try:
            if HardsploitUtils.get_number_of_board_available() < 1:
                return ErrorMsg.hardsploit_not_found()
            if not self.control_write_settings():
                return 0
            Firmware('I2C', self._api)
            utils.progress_bar = ProgressBar("I²C: Writing...")
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
                i2c.i2c_generic_import(
                    i2c_base_address=int(self.chip.i2c_settings[0].address_w, base=16),
                    start_address=int(self.view.lie_start.text()),
                    page_size=self.chip.i2c_settings[0].page_size,
                    memory_size=self.chip.i2c_settings[0].total_size,
                    data_file=self.filepath,
                    write_page_latency=self.chip.i2c_settings[0].write_page_latency / 1000
                )
        except Exception as e:
            ErrorMsg.unknown(e)


    def control_write_settings(self):
        if not self.chip.i2c_settings:
            QMessageBox(QMessageBox.Warning, 'Missing I2C setting', 'No settings saved for this chip').exec_()
            return 0
        if not self.chip.i2c_settings[0].total_size:
            QMessageBox(QMessageBox.Warning, 'Missing I2C setting', 'Total size setting missing').exec_()
            return 0
        if not self.chip.i2c_settings[0].page_size:
            QMessageBox(QMessageBox.Warning, 'Missing I2C setting', 'Page size setting missing').exec_()
            return 0
        if not self.chip.i2c_settings[0].write_page_latency:
            QMessageBox(QMessageBox.Warning, 'Missing I2C setting', 'Write page latency setting missing').exec_()
            return 0
        if not self.chip.i2c_settings[0].frequency or not self.chip.i2c_settings[0].address_w:
            QMessageBox(QMessageBox.Warning, 'Missing I2C setting', 'Write base address or frequency settings missing').exec_()
            return 0
        if self.view.lie_start.text() == "":
            QMessageBox(QMessageBox.Warning, 'Missing start address', 'Please fill the Start address field').exec_()
            return 0
        return 1
