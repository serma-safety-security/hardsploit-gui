"""spi_write.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from hardsploit.core import HardsploitUtils
from hardsploit.modules import HardsploitSPI

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.progress_bar import ProgressBar
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.gui.gui_generic_write import Ui_Generic_write


class SpiWrite(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        self.view = Ui_Generic_write()
        self._api = hardsploit_api
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        input_restrict(self.view.lie_start, 0)
        self.chip = chip
        self.speeds = {
            '25.00': 3,
            '18.75': 4,
            '15.00': 5,
            '12.50': 6,
            '10.71': 7,
            '9.38': 8,
            '7.50': 10,
            '5.00': 15,
            '3.95': 19,
            '3.00': 25,
            '2.03': 37,
            '1.00': 75,
            '0.50': 150,
            '0.29': 255
        }
        self.filepath = ""

    @Slot()
    def select_write_file(self):
        self.filepath = QFileDialog.getOpenFileName(self, 'Select a file', '/', '*.*')[0]
        if self.filepath:
            self.view.btn_write.setEnabled(True)
            self.view.lbl_selected_file.setText(f"{self.filepath.split('/')[-1]}")

    @Slot()
    def write(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            return ErrorMsg.hardsploit_not_found()
        if not self.control_write_settings():
            return 0
        spi = HardsploitSPI(
            speed=self.speeds[self.chip.spi_settings[0].frequency],
            mode=self.chip.spi_settings[0].mode,
            hardsploit_api=self._api
        )
        Firmware('SPI', self._api)
        utils.progress_bar = ProgressBar("SPI: Writing...")
        utils.PROGRESS_BAR.show()
        flash = False
        if self.chip.spi_settings[0].is_flash:
            flash = True
        spi.spi_generic_import(
            start_address=int(self.view.lie_start.text()),
            page_size=self.chip.spi_settings[0].page_size,
            memory_size=self.chip.spi_settings[0].total_size,
            data_file=self.filepath,
            write_spi_command=self.chip.spi_settings[0].command_write,
            write_page_latency=self.chip.spi_settings[0].write_page_latency / 1000.0,
            enable_write_spi_command=self.chip.spi_settings[0].command_write_enable,
            clear_spi_command=self.chip.spi_settings[0].command_erase,
            clear_chip_time=self.chip.spi_settings[0].erase_time,
            is_flash=flash
        )

    def control_write_settings(self):
        if not self.chip.spi_settings:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI settings',
                'No settings saved for this chip'
            ).exec_()
            return 0

        if not self.chip.spi_settings[0].total_size or not self.chip.spi_settings[0].page_size:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI settings',
                'Total size or page size missing'
            ).exec_()
            return 0

        if not self.chip.spi_settings[0].command_read or not self.chip.spi_settings[0].frequency:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI settings',
                'Read command or frequency missing'
            ).exec_()
            return 0

        if not self.chip.spi_settings[0].command_write:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI settings',
                'Write command missing'
            ).exec_()
            return 0

        if not self.chip.spi_settings[0].write_page_latency:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI setting',
                'SPI write page latency missing'
            ).exec_()
            return 0

        if self.chip.spi_settings[0].is_flash is None:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI setting',
                'SPI flash nature missing'
            ).exec_()
            return 0
        else:
            if self.chip.spi_settings[0].is_flash:
                if not self.chip.spi_settings[0].erase_time or not self.chip.spi_settings[0].command_erase:
                    QMessageBox(
                        QMessageBox.Warning,
                        'Missing SPI setting',
                        'SPI erase time or command missing'
                    ).exec_()
                    return 0

        if not self.chip.spi_settings[0].mode:
            QMessageBox(
                QMessageBox.Warning,
                'Missing SPI setting',
                'Mode missing'
            ).exec_()
            return 0

        if self.view.lie_start.text() == "":
            QMessageBox(
                QMessageBox.Warning,
                'Missing start address',
                'Please fill the Start address field'
            ).exec_()
            return 0
        return 1
