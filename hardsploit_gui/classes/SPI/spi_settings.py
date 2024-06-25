"""spi_settings.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import SpiSetting
from hardsploit_gui.gui.gui_spi_settings import Ui_Spi_settings
from hardsploit_gui.classes.error_msg import ErrorMsg


class SpiSettings(QWidget):

    def __init__(self, chip):
        super().__init__()
        self.view = Ui_Spi_settings()
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_total_size, 0)
        input_restrict(self.view.lie_page_size, 0)
        input_restrict(self.view.lie_write_page_latency, 0)
        input_restrict(self.view.lie_cmd_read, 0)
        input_restrict(self.view.lie_cmd_write, 0)
        input_restrict(self.view.lie_cmd_write_enable, 0)
        input_restrict(self.view.lie_cmd_erase, 0)
        input_restrict(self.view.lie_erase_time, 0)
        self.chip = chip
        if chip.spi_settings:
            self.feed_settings_form()

    @Slot()
    def save_settings(self):
        if self.chip.spi_settings:
            self.update()
        else:
            self.create()

    def feed_settings_form(self):
        self.view.cbx_mode.setCurrentIndex(self.view.cbx_mode.findText(str(self.chip.spi_settings[0].mode)))
        self.view.cbx_frequency.setCurrentIndex(self.view.cbx_frequency.findText(self.chip.spi_settings[0].frequency))
        self.view.lie_cmd_read.setText(str(self.chip.spi_settings[0].command_read))
        self.view.lie_cmd_write.setText(str(self.chip.spi_settings[0].command_write))
        self.view.lie_write_page_latency.setText(str(self.chip.spi_settings[0].write_page_latency))
        self.view.lie_cmd_write_enable.setText(str(self.chip.spi_settings[0].command_write_enable))
        self.view.lie_cmd_erase.setText(str(self.chip.spi_settings[0].command_erase))
        self.view.lie_erase_time.setText(str(self.chip.spi_settings[0].erase_time))
        self.view.lie_page_size.setText(str(self.chip.spi_settings[0].page_size))
        self.view.lie_total_size.setText(str(self.chip.spi_settings[0].total_size))
        if not self.chip.spi_settings[0].is_flash:
            self.view.rbn_no.setChecked(True)

    def is_flash(self):
        if self.view.rbn_no.isChecked():
            return 0
        return 1

    def create(self):
        if self.check_values():
            chip_settings = SpiSetting.create(
                mode=int(self.view.cbx_mode.currentText()),
                frequency=self.view.cbx_frequency.currentText(),
                write_page_latency=self.view.lie_write_page_latency.text(),
                command_read=self.view.lie_cmd_read.text(),
                command_write=self.view.lie_cmd_write.text(),
                command_write_enable=self.view.lie_cmd_write_enable.text(),
                command_erase=self.view.lie_cmd_erase.text(),
                erase_time=self.view.lie_erase_time.text(),
                page_size=self.view.lie_page_size.text(),
                total_size=self.view.lie_total_size.text(),
                is_flash=self.is_flash(),
                chip_id=self.chip.id
            )
            chip_settings.save()
            QMessageBox(QMessageBox.Information, 'Success', 'SPI settings saved').exec_()
            self.close()

    def update(self):
        if self.check_values():
            spi_setting = self.chip.spi_settings[0]
            spi_setting.mode = int(self.view.cbx_mode.currentText())
            spi_setting.frequency = self.view.cbx_frequency.currentText()
            spi_setting.write_page_latency = self.view.lie_write_page_latency.text()
            spi_setting.command_read = self.view.lie_cmd_read.text()
            spi_setting.command_write = self.view.lie_cmd_write.text()
            spi_setting.command_write_enable = self.view.lie_cmd_write_enable.text()
            spi_setting.command_erase = self.view.lie_cmd_erase.text()
            spi_setting.erase_time = self.view.lie_erase_time.text()
            spi_setting.page_size = self.view.lie_page_size.text()
            spi_setting.total_size = self.view.lie_total_size.text()
            spi_setting.is_flash = self.is_flash()
            spi_setting.save()
            QMessageBox(QMessageBox.Information, 'Success', 'SPI settings updated').exec_()
            self.close()

    def check_values(self):
        if len(self.view.lie_cmd_write.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid write command")
            return False
        if len(self.view.lie_cmd_erase.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid Erase command")
            return False
        if len(self.view.lie_cmd_write_enable.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid Enable write command")
            return False
        if len(self.view.lie_total_size.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid total size")
            return False
        if len(self.view.lie_page_size.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid Write page latency")
            return False
        if len(self.view.lie_write_page_latency.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid page size")
            return False
        if len(self.view.lie_erase_time.text()) > 19:
            ErrorMsg.custom("Invalid value", "Invalid clear chip time")
            return False
        return True
