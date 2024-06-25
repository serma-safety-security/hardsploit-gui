"""progress_bar.py"""

from PySide6.QtWidgets import QWidget

from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_progress_bar import Ui_Progress_bar


class ProgressBar(QWidget):

    def __init__(self, status):
        super().__init__()
        self.pgb_ui = Ui_Progress_bar()
        center_window(self)
        self.pgb_ui.setupUi(self)
        self.update_status(status)
        self.pgb_ui.lbl_close.setEnabled(True)
        self.display_time("Total duration:")

    def update_status(self, status):
        self.pgb_ui.lbl_status.setText(status)

    def update_value(self, value):
        if 100 >= value >= 0:
            self.pgb_ui.pgb.setValue(value)

    def display_time(self, time):
        self.pgb_ui.lbl_time.setText(time)
