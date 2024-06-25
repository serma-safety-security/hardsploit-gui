"""can_settings.py"""

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QMessageBox
from hardsploit.core import HardsploitUtils

from hardsploit_gui.classes.CAN.can_baudrate import CanBaudrate
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import CanSetting
from hardsploit_gui.gui.gui_can_settings import Ui_CAN_settings


class CanSettings(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_CAN_settings()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_baud_rate, 0)
        input_restrict(self.view.lie_crc_polynom, 0)
        input_restrict(self.view.lie_crc_type, 0)
        input_restrict(self.view.lie_id, 4)
        self.view.lie_crc_polynom.setText("50585")
        self.view.lie_crc_type.setText("16")
        self.chip = chip
        self.baud_can = None
        if chip.can_settings:
            self.feed_settings_form()


    @Slot()
    def save_settings(self):
        if self.get_return_frame_format() == 1:
            # id size has to be 29 bits
            if len(self.view.lie_id.text()) != 8:
                QMessageBox(QMessageBox.Warning,
                            'Error size of the id',
                            'The size of a extended id is 29 bits (8 hexadecimal characters)'
                            ).exec_()
                return 0
        else:
            # id standard size = 11 bits
            if len(self.view.lie_id.text()) != 3:
                QMessageBox(QMessageBox.Warning,
                            'Error size of the id',
                            'The size of a standard id is 11 bits (3 hexadecimal characters)'
                            ).exec_()
                return 0

        if self.chip.can_settings:
            self.update()
        else:
            self.create()

    def feed_settings_form(self):
        # Print the type and content of chip.can_settings for debugging
        self.view.lie_baud_rate.setText(str(self.chip.can_settings.baud_rate))
        self.view.lie_crc_polynom.setText(str(self.chip.can_settings.crc_poly))
        self.view.lie_crc_type.setText(str(self.chip.can_settings.crc_type))
        self.view.lie_id.setText(int(self.chip.can_settings.identifier, 16))
        if self.chip.can_settings.return_frame_format == 0:
            self.view.rbn_standard.setChecked(True)
        if self.chip.can_settings.return_frame_format == 1:
            self.view.rbn_extended.setChecked(True)

    def create(self):
        chip_settings = CanSetting.create(
            baud_rate=int(self.view.lie_baud_rate.text()),
            crc_poly=int(self.view.lie_crc_polynom.text()),
            crc_type=int(self.view.lie_crc_type.text()),
            identifier=str(self.view.lie_id.text()),
            return_frame_format=self.get_return_frame_format,
            chip_id=self.chip.id
        )
        chip_settings.save()
        QMessageBox(QMessageBox.Information, 'Success', 'CAN settings saved').exec_()
        self.close()

    def update(self):
        chip_settings = self.chip.can_settings[0]
        chip_settings.baud_rate = int(self.view.lie_baud_rate.text())
        chip_settings.crc_poly = int(self.view.lie_crc_polynom.text())
        chip_settings.crc_type = int(self.view.lie_crc_type.text())
        chip_settings.identifier = hex(self.view.lie_id.text())
        chip_settings.return_frame_format = self.get_return_frame_format()
        chip_settings.save()

        QMessageBox(QMessageBox.Information, 'Success', 'CAN settings updated').exec_()
        self.close()

    def get_return_frame_format(self):
        if self.view.rbn_standard.isChecked():
            return 0
        if self.view.rbn_extended.isChecked():
            return 1
        return None

    @Slot()
    def autodetect(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        self.baud_can = CanBaudrate(self.view, self._api)
        self.baud_can.setWindowModality(Qt.ApplicationModal)
        self.baud_can.show()

    def check_values(self):
        if not self.view.lie_baud_rate.text():
            ErrorMsg.custom("Invalid values", "Invalid baud rate")
            return False
        elif not self.view.lie_crc_polynom.text():
            ErrorMsg.custom("Invalid values", "Invalid CRC polynom")
            return False
        elif not self.view.lie_crc_type.text():
            ErrorMsg.custom("Invalid values", "Invalid CRC type")
            return False
        elif not self.view.lie_id.text():
            ErrorMsg.custom("Invalid values", "Invalid ID")
            return False
        return True
