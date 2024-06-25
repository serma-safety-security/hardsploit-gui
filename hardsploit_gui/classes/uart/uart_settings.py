"""uart_settings.py"""
import peewee
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.uart.uart_baudrate import UartBaudrate
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import UartSetting
from hardsploit_gui.gui.gui_uart_settings import Ui_Uart_settings
from hardsploit.core import HardsploitUtils


class UartSettings(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_Uart_settings()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_baud_rate, 0)
        input_restrict(self.view.lie_idle_line_lvl, 0)
        input_restrict(self.view.lie_parity_bit, 0)
        input_restrict(self.view.lie_parity_type, 0)
        input_restrict(self.view.lie_stop_bits_nbr, 0)
        input_restrict(self.view.lie_word_size, 0)
        self.chip = chip
        self.baudUART = None
        if self.chip.uart_settings:
            self.feed_settings_form()

    @Slot()
    def save_settings(self):
        if self.chip.uart_settings:
            self.update()
        else:
            self.create()


    def feed_settings_form(self):
        self.view.lie_baud_rate.setText(str(self.chip.uart_settings[0].baud_rate))
        self.view.lie_idle_line_lvl.setText(str(self.chip.uart_settings[0].idle_line))
        self.view.lie_parity_bit.setText(str(self.chip.uart_settings[0].parity_bit))
        self.view.lie_parity_type.setText(str(self.chip.uart_settings[0].parity_type))
        self.view.lie_stop_bits_nbr.setText(str(self.chip.uart_settings[0].stop_bits_nbr))
        self.view.lie_word_size.setText(str(self.chip.uart_settings[0].word_size))
        if self.chip.uart_settings[0].return_type == 0:
            self.view.rbn_cr.setChecked(True)
        elif self.chip.uart_settings[0].return_type == 1:
            self.view.rbn_lf.setChecked(True)
        elif self.chip.uart_settings[0].return_type == 2:
            self.view.rbn_both.setChecked(True)

    def create(self):
        if self.check_values():
            chip_settings = UartSetting.create(
                baud_rate=int(self.view.lie_baud_rate.text()),
                idle_line=int(self.view.lie_idle_line_lvl.text()),
                parity_bit=int(self.view.lie_parity_bit.text()),
                parity_type=int(self.view.lie_parity_type.text()),
                stop_bits_nbr=int(self.view.lie_stop_bits_nbr.text()),
                word_size=int(self.view.lie_word_size.text()),
                return_type=self.get_return_type(),
                chip_id=self.chip.id
            )
            chip_settings.save()
            QMessageBox(QMessageBox.Information, 'Success', 'UART settings saved').exec_()
            self.close()
        else:
            return False


    def update(self):
        if self.check_values():
            uart_setting = self.chip.uart_settings[0]
            uart_setting.baud_rate = int(self.view.lie_baud_rate.text())
            uart_setting.idle_line = int(self.view.lie_idle_line_lvl.text())
            uart_setting.parity_bit = int(self.view.lie_parity_bit.text())
            uart_setting.parity_type = int(self.view.lie_parity_type.text())
            uart_setting.stop_bits_nbr = int(self.view.lie_stop_bits_nbr.text())
            uart_setting.word_size = int(self.view.lie_word_size.text())
            uart_setting.return_type = self.get_return_type()
            uart_setting.save()
            QMessageBox(QMessageBox.Information, 'Success', 'UART settings updated').exec_()
            self.close()

    def check_values(self):
        values = {
            'Word size': int(self.view.lie_word_size.text()),
            'Parity bit': int(self.view.lie_parity_bit.text()),
            'Parity type': int(self.view.lie_parity_type.text()),
            'Stop bits number': int(self.view.lie_stop_bits_nbr.text()),
            'Idle line level': int(self.view.lie_idle_line_lvl.text())
        }
        if len(self.view.lie_baud_rate.text()) > 10:
            ErrorMsg.custom("Invalid values", "Invalid baud rate value")
            return False
        for key, value in values.items():
            if value > 8:
                ErrorMsg.custom("Invalid values", f"Invalid {key} value")
                return False
        return True

    def get_return_type(self):
        if self.view.rbn_cr.isChecked():
            return 0
        elif self.view.rbn_lf.isChecked():
            return 1
        elif self.view.rbn_both.isChecked():
            return 2

    @Slot()
    def autodetect(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        self.baudUART = UartBaudrate(self.view, self._api)
        self.baudUART.setWindowModality(Qt.ApplicationModal)
        self.baudUART.show()
