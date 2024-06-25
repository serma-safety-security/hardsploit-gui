"""i2c_command.py"""

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit_gui.classes.command_editor import CommandEditor
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.gui.gui_i2c_command import Ui_I2c_command


class I2cCommand(QWidget):

    def __init__(self, chip, bus_id, parent):
        super().__init__()
        self.view = Ui_I2c_command()
        center_window(self)
        self.view.setupUi(self)
        self.view.rbn_read.setChecked(True)
        input_restrict(self.view.lie_size, 0)
        self.chip = chip
        self.chip_settings = chip.i2c_settings
        self.bus_id = bus_id
        self.parent = parent
        self.i2c_cmd_form = None

    @Slot()
    def open_generic_cmd(self):
        if not self.check_form_param():
            return 0
        addr = ""
        if self.view.rbn_read.isChecked():
            mode = "r"
            if self.chip_settings:
                addr = self.chip_settings[0].address_r
        else:
            mode = "w"
            if self.chip_settings:
                addr = self.chip_settings[0].address_w
        self.i2c_cmd_form = CommandEditor(0, None, None,
                                          self.chip, self.bus_id, self.parent, mode=mode,
                                          size=self.view.lie_size.text(), addr=addr)
        self.i2c_cmd_form.setWindowModality(Qt.ApplicationModal)
        self.i2c_cmd_form.show()

    def check_form_param(self):
        if self.view.lie_size.text() == "" or int(self.view.lie_size.text()) == 0:
            QMessageBox(QMessageBox.Information, "Form invalid", "Payload size must be filled and superior to 0").exec_()
            return 0
        return 1
