"""i2c_settings.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import I2cSetting
from hardsploit_gui.gui.gui_i2c_settings import Ui_I2c_settings
from hardsploit.core import HardsploitUtils
from hardsploit.modules import HardsploitI2c


class I2cSettings(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_I2c_settings()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_total_size, 0)
        input_restrict(self.view.lie_page_size, 0)
        input_restrict(self.view.lie_write_page_latency, 0)
        input_restrict(self.view.lie_address_r, 3)
        input_restrict(self.view.lie_address_w, 3)
        self.view.tbl_bus_scan.resizeColumnsToContents()
        self.view.tbl_bus_scan.resizeRowsToContents()
        self.view.tbl_bus_scan.horizontalHeader().setStretchLastSection(True)
        self.chip = chip
        if self.chip.i2c_settings:
            self.feed_settings_form()

    @Slot()
    def save_settings(self):
        if self.chip.i2c_settings:
            self.update()
        else:
            self.create()

    def feed_settings_form(self):
        self.view.lie_address_w.setText(self.chip.i2c_settings[0].address_w)
        self.view.lie_address_r.setText(self.chip.i2c_settings[0].address_r)
        self.view.cbx_frequency.setCurrentIndex(self.view.cbx_frequency.findText(str(self.chip.i2c_settings[0].frequency)))
        self.view.lie_write_page_latency.setText(str(self.chip.i2c_settings[0].write_page_latency))
        self.view.lie_page_size.setText(str(self.chip.i2c_settings[0].page_size))
        self.view.lie_total_size.setText(str(self.chip.i2c_settings[0].total_size))

    def create(self):
        if self.check_values():
            chip_setting = I2cSetting.create(
                address_w=self.view.lie_address_w.text(),
                address_r=self.view.lie_address_r.text(),
                frequency=int(self.view.cbx_frequency.currentText()),
                write_page_latency=self.view.lie_write_page_latency.text(),
                page_size=self.view.lie_page_size.text(),
                total_size=self.view.lie_total_size.text(),
                chip_id=self.chip.id
            )
            chip_setting.save()
            QMessageBox(QMessageBox.Information, 'Success', 'I2C settings saved').exec_()
            self.close()

    def update(self):
        if self.check_values():
            i2c_setting = self.chip.i2c_settings[0]
            i2c_setting.address_w = self.view.lie_address_w.text()
            i2c_setting.address_r = self.view.lie_address_r.text()
            i2c_setting.frequency = int(self.view.cbx_frequency.currentText())
            i2c_setting.write_page_latency = self.view.lie_write_page_latency.text()
            i2c_setting.page_size = self.view.lie_page_size.text()
            i2c_setting.total_size = self.view.lie_total_size.text()
            i2c_setting.save()
            QMessageBox(QMessageBox.Information, 'Success', 'I2C settings updated').exec_()
            self.close()

    def check_values(self):
        if len(self.view.lie_total_size.text()) >= 20:
            ErrorMsg.custom("Value Error", "Invalid total size value!")
            return False
        elif len(self.view.lie_page_size.text()) >= 20:
            ErrorMsg.custom("Value Error", "Invalid page size value!")
            return False
        elif len(self.view.lie_write_page_latency.text()) >= 20:
            ErrorMsg.custom("Invalid value", "Invalid write page latency value!")
            return False
        return True


    @Slot()
    def bus_scan(self):
        try:
            if HardsploitUtils.get_number_of_board_available() < 1:
                return ErrorMsg.hardsploit_not_found()
            self.view.tbl_bus_scan.setRowCount(0)
            Firmware('I2C', self._api)

            if not self.chip.i2c_settings:
                chip_setting = I2cSetting.create(
                    address_w="00",
                    address_r="00",
                    frequency=int(self.view.cbx_frequency.currentText()),
                    write_page_latency=self.view.lie_write_page_latency.text(),
                    page_size=self.view.lie_page_size.text(),
                    total_size=self.view.lie_total_size.text(),
                    chip_id=self.chip.id
                )
                chip_setting.save()
            else:
                i2c_setting = self.chip.i2c_settings[0]
                i2c_setting.address_w = self.view.lie_address_w.text()
                i2c_setting.address_r = self.view.lie_address_r.text()
                i2c_setting.frequency = int(self.view.cbx_frequency.currentText())
                i2c_setting.write_page_latency = self.view.lie_write_page_latency.text()
                i2c_setting.page_size = self.view.lie_page_size.text()
                i2c_setting.total_size = self.view.lie_total_size.text()
                i2c_setting.save()

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
            scan_result = i2c.i2c_scan()
            if len(scan_result) > 0:
                for i, v in enumerate(scan_result):
                    if v == 1:
                        self.view.tbl_bus_scan.insertRow(self.view.tbl_bus_scan.rowCount())
                        self.view.tbl_bus_scan.setItem(self.view.tbl_bus_scan.rowCount() - 1, 0,
                                                       QTableWidgetItem(f"0x{hex(i)[2:].upper()}"))
                        if i % 2 == 0:
                            self.view.tbl_bus_scan.setItem(self.view.tbl_bus_scan.rowCount() - 1, 1, QTableWidgetItem('Write'))
                        else:
                            self.view.tbl_bus_scan.setItem(self.view.tbl_bus_scan.rowCount() - 1, 1, QTableWidgetItem('Read'))
                QMessageBox(QMessageBox.Information, "Bus Scan",
                            f"Bus scan ended correctly: {self.view.tbl_bus_scan.rowCount()} address(es) found").exec_()
            else:
                QMessageBox(QMessageBox.Information, "Bus addresses", "No valid addresses have been returned by the scan").exec_()
        except Exception as e:
            ErrorMsg.unknown(e)
