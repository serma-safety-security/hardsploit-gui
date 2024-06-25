from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from .classes import utils
from .classes.chip_management import ChipManagement
from .classes.utils import center_window
from hardsploit.core import HardsploitAPI


class HardsploitGUI:
    VERSION = "0.1.0"
    currentFirmware = None
    LOG_FILE_PATH = str(Path(__file__).parent.resolve()) + "/logs/error.log"
    DB_FILE_PATH = str(Path(__file__).parent.resolve()) + "/db/hardsploit.db"

    def __init__(self):
        HardsploitAPI.callbackProgress = self.callback_progress
        HardsploitAPI.callbackData = self.callback_data
        self.file = None
        self.app = QApplication([])
        self.ui = ChipManagement(self.VERSION)
        center_window(self.ui)
        app_icon = QIcon("hardsploit.png")
        self.ui.setWindowIcon(app_icon)
        self.ui.show()
        sys.exit(self.app.exec_())

    def callback_progress(self, percent, start_time, end_time):
        if utils.progress_bar:
            utils.progress_bar.update_value(percent)
            if percent == 100:
                duration = round(end_time - start_time, 2)
                utils.progress_bar.display_time("Total duration: {} second(s)".format(duration))
        self.app.processEvents()

    @staticmethod
    def callback_data(receive_data):
        utils.file.write(bytes(receive_data))


if __name__ == "__main__":
    HardsploitGUI()
