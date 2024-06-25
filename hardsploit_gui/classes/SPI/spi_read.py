"""spi_read.py"""

from pathlib import Path

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QFileDialog
from hardsploit.core import HardsploitUtils
from hardsploit.modules import HardsploitSPI

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.progress_bar import ProgressBar
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.gui.gui_generic_read import Ui_Generic_read



class SpiRead(QWidget):

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

    @Slot()
    def select_read_file(self):
        self.filepath = QFileDialog.getSaveFileName(self, 'Select a file', '/', '*.*')[0]
        if self.filepath:
            self.view.btn_read.setEnabled(True)
            self.view.lbl_selected_file.setText(f"{self.filepath.split('/')[-1]}")

    @Slot()
    def read(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            raise ErrorMsg.hardsploit_not_found()
        if self.filepath:
            utils.file = open(self.filepath, 'wb')
        if self.view.rbn_full.isChecked():
            if not self.control_read_settings('full'):
                return False
            start = 0
            stop = self.chip.spi_settings[0].total_size - 1
            control = self.chip.spi_settings[0].total_size
        else:
            if not self.control_read_settings('partial'):
                return False
            start = int(self.view.lie_start.text())
            stop = int(self.view.lie_stop.text())
            control = (stop - start) + 1

        Firmware('SPI', self._api)
        utils.progress_bar = ProgressBar("SPI: Reading...")
        utils.progress_bar.show()
        spi = HardsploitSPI(
            speed=self.speeds[self.chip.spi_settings[0].frequency],
            mode=self.chip.spi_settings[0].mode,
            hardsploit_api=self._api
        )
        spi.spi_generic_dump(
            read_spi_command=self.chip.spi_settings[0].command_read,
            start_address=start,
            stop_address=stop,
            size_max=int(self.chip.spi_settings[0].total_size)
        )
        utils.file.close()
        if control != Path(self.filepath).stat().st_size:
            raise ErrorMsg.filesize_error
        # except Exception as e:
        #    ErrorMsg.unknown(e)

    def control_read_settings(self, type):
        try:
            if not (self.chip.spi_settings and len(self.chip.spi_settings) > 0 and self.chip.spi_settings[0]):
                return ErrorMsg.settings_missing()
            if not self.chip.spi_settings[0].frequency:
                return ErrorMsg.frequency_missing()
            if not self.chip.spi_settings[0].command_read:
                return ErrorMsg.mode_missing()
            if not self.chip.spi_settings[0].total_size:
                return ErrorMsg.full_size_error()
            if not self.chip.spi_settings[0].total_size:
                return ErrorMsg.full_size_error()
            if type == 'partial':
                if self.view.lie_start.text() == "":
                    return ErrorMsg.start_stop_missing()
                if self.view.lie_stop.text() == "":
                    return ErrorMsg.start_stop_missing()
                start = int(self.view.lie_start.text())
                stop = int(self.view.lie_stop.text())
                total_size = self.chip.spi_settings[0].total_size
                if start == stop:
                    return ErrorMsg.start_neq_stop()
                if start > stop:
                    return ErrorMsg.start_inf_to_stop()
                if start > (total_size - 1):
                    return ErrorMsg.inf_to_total_size()
                if stop > (total_size - 1):
                    return ErrorMsg.inf_to_total_size()
            return True
        except Exception as e:
            ErrorMsg.unknown(e)
