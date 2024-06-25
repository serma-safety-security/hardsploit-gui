"""swd_settings.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import SwdSetting
from hardsploit_gui.gui.gui_swd_settings import Ui_Swd_settings
from hardsploit_gui.classes.error_msg import ErrorMsg


class SwdSettings(QWidget):

    def __init__(self, chip):
        super().__init__()
        self.view = Ui_Swd_settings()
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_cpu_id_address, 4)
        input_restrict(self.view.lie_device_id_address, 4)
        input_restrict(self.view.lie_size_address, 4)
        input_restrict(self.view.lie_start_address, 4)
        self.chip = chip
        if self.chip.swd_settings:
            self.feed_settings_form()

    @Slot()
    def save_settings(self):
        if self.chip.swd_settings:
            self.update()
        else:
            self.create()

    def feed_settings_form(self):
        self.view.lie_cpu_id_address.setText(self.chip.swd_settings[0].cpu_id_address)
        self.view.lie_device_id_address.setText(self.chip.swd_settings[0].device_id_address)
        self.view.lie_size_address.setText(self.chip.swd_settings[0].memory_size_address)
        self.view.lie_start_address.setText(self.chip.swd_settings[0].memory_start_address)

    def create(self):
        if self.check_values():
            chip_settings = SwdSetting.create(
                cpu_id_address=self.view.lie_cpu_id_address.text(),
                device_id_address=self.view.lie_device_id_address.text(),
                memory_size_address=self.view.lie_size_address.text(),
                memory_start_address=self.view.lie_start_address.text(),
                chip_id=self.chip.id
            )
            chip_settings.save()
            QMessageBox(QMessageBox.Information, 'Success', 'SWD settings saved').exec_()
            self.close()

    def update(self):
        if self.check_values():
            swd_setting = self.chip.swd_settings[0]
            swd_setting.cpu_id_address = self.view.lie_cpu_id_address.text()
            swd_setting.device_id_address = self.view.lie_device_id_address.text()
            swd_setting.memory_size_address = self.view.lie_size_address.text()
            swd_setting.memory_start_address = self.view.lie_start_address.text()
            swd_setting.save()
            QMessageBox(QMessageBox.Information, 'Success', 'SWD settings updated').exec_()
            self.close()

    def check_values(self):
        checker = True
        if len(self.view.lie_cpu_id_address.text()) != 8:
            ErrorMsg.custom("Value Error", "Invalid CPU ID address")
            checker = False
        elif len(self.view.lie_device_id_address.text()) != 8:
            ErrorMsg.custom("Value Error", "Invalid Device ID address")
            checker = False
        elif len(self.view.lie_size_address.text()) != 8:
            ErrorMsg.custom("Value Error", "Invalid memory size address")
            checker = False
        elif len(self.view.lie_start_address.text()) != 8:
            ErrorMsg.custom("Value Error", "Invalid memory start address")
            checker = False
        return checker
