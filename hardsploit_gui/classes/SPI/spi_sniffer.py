"""spi_sniffer.py"""

from time import sleep

from PySide6.QtCore import Slot, QTimer
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from hardsploit.core import HardsploitUtils, HardsploitConstant, HardsploitError
from hardsploit.modules import HardsploitSPISniffer

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_spi_sniffer import Ui_Spi_sniffer


class SpiSniffer(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_Spi_sniffer()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.chip = chip
        self.resize_to_content()
        self.spi = None
        self.timer = None

    @Slot()
    def start(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        self.view.btn_stop.setEnabled(True)
        self.view.btn_start.setEnabled(False)
        self.view.cbx_type.setEnabled(False)
        Firmware('SPI_SNIFFER', self._api)
        mode = 0
        if self.view.cbx_type.currentIndex() == 0:
            mode = HardsploitConstant.SPISniffer.MISO_MOSI
        elif self.view.cbx_type.currentIndex() == 1:
            mode = HardsploitConstant.SPISniffer.MOSI
        elif self.view.cbx_type.currentIndex() == 2:
            mode = HardsploitConstant.SPISniffer.MISO
        if self.chip.spi_settings[0].mode is None:
            return ErrorMsg.spi_mode_missing()
        self.spi = HardsploitSPISniffer(
            mode=self.chip.spi_settings[0].mode,
            sniff=mode,
            hardsploit_api=self._api
        )
        self.spi.spi_set_settings()
        sleep(0.5)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    @Slot()
    def update(self):
        try:
            result = self.spi.spi_receive_available_data()
            if len(result) > 0:
                if self.spi.sniff == HardsploitConstant.SPISniffer.MISO_MOSI:
                    for i, elem in enumerate(result[0]):
                        ascii_miso = ""
                        ascii_mosi = ""
                        if str(elem).isascii() and elem != 255 and elem != 0:
                            ascii_mosi = chr(elem)
                        if str(result[1][i]).isascii() and result[1][i] != 255 and result[1][i] != 0:
                            ascii_miso = chr(result[1][i])
                        self.view.tbl_result.insertRow(i)
                        self.view.tbl_result.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                        self.view.tbl_result.setItem(i, 1, QTableWidgetItem(f"0x{hex(elem)[2:].upper()}"))
                        self.view.tbl_result.setItem(i, 2, QTableWidgetItem(ascii_mosi))
                        self.view.tbl_result.setItem(i, 3, QTableWidgetItem(f"0x{hex(result[1][i])[2:].upper()}"))
                        self.view.tbl_result.setItem(i, 4, QTableWidgetItem(ascii_miso))
                else:  # MOSI OR MISO
                    if self.spi.sniff == HardsploitConstant.SPISniffer.MISO:
                        for i, elem in enumerate(result):
                            ascii_miso = ""
                            if str(elem).isascii() and elem != 255 and elem != 0:
                                ascii_miso = chr(elem)
                            self.view.tbl_result.insertRow(i)
                            self.view.tbl_result.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                            self.view.tbl_result.setItem(i, 1, QTableWidgetItem('-'))
                            self.view.tbl_result.setItem(i, 2, QTableWidgetItem(""))
                            self.view.tbl_result.setItem(i, 3, QTableWidgetItem(f"0x{hex(elem)[2:].upper()}"))
                            self.view.tbl_result.setItem(i, 4, QTableWidgetItem(ascii_miso))
                    else:
                        for i, elem in enumerate(result):
                            ascii_mosi = ""
                            if str(elem).isascii() and elem != 255 and elem != 0:
                                ascii_mosi = chr(elem)
                            self.view.tbl_result.insertRow(i)
                            self.view.tbl_result.setItem(i, 0, QTableWidgetItem(str(self.view.tbl_result.rowCount() + 1)))
                            self.view.tbl_result.setItem(i, 1, QTableWidgetItem(f"0x{hex(elem)[2:].upper()}"))
                            self.view.tbl_result.setItem(i, 2, QTableWidgetItem(ascii_mosi))
                            self.view.tbl_result.setItem(i, 3, QTableWidgetItem('-'))
                            self.view.tbl_result.setItem(i, 4, QTableWidgetItem(""))

                    self.resize_to_content()
        except HardsploitError.HardsploitNotFound:
            ErrorMsg.hardsploit_not_found()
        except HardsploitError.USBError:
            ErrorMsg.usb_error()

    @Slot()
    def stop(self):
        self.view.btn_start.setEnabled(True)
        self.view.cbx_type.setEnabled(True)
        self.view.btn_stop.setEnabled(False)
        self.timer.stop()

    def closeEvent(self, event):
        if self.timer:
            self.timer.stop()

    def resize_to_content(self):
        self.view.tbl_result.resizeColumnsToContents()
        self.view.tbl_result.resizeRowsToContents()
        self.view.tbl_result.horizontalHeader().stretchLastSection = True
