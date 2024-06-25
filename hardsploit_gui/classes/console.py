"""console.py"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
import time


class Console(QTableWidget):

    def __init__(self, console):
        super().__init__()
        self.console = console

    def print(self, msg):
        self.console.insertRow(self.console.rowCount())
        t = QTableWidgetItem(str(time.strftime('%d/%m %H:%M')))
        t.setFlags(Qt.ItemIsEnabled)
        msg = QTableWidgetItem(msg)
        msg.setFlags(Qt.ItemIsEnabled)
        self.console.setItem(self.console.rowCount() - 1, 0, t)
        self.console.setItem(self.console.rowCount() - 1, 1, msg)
        self.console.scrollToItem(t, QAbstractItemView.EnsureVisible)
