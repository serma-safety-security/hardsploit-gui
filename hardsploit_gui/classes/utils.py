"""utils.py"""

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QScreen, QRegularExpressionValidator, QGuiApplication
from PySide6.QtWidgets import QApplication, QMessageBox

# Global variables
PROGRESS_BAR = None
FILE = None


def center_window(win):
    screen = QGuiApplication.primaryScreen().geometry()
    window_geometry = win.frameGeometry()
    x = (screen.width() - window_geometry.width()) // 2
    y = (screen.height() - window_geometry.height()) // 2
    win.move(x, y)


def input_restrict(line_edit, type):
    reg = None
    if type == 0:
        reg = QRegularExpression("[0-9]+")
    elif type == 1:
        reg = QRegularExpression("^[a-zA-Z_@-]+( [a-zA-Z_@-]+)*$")
    elif type == 2:
        reg = QRegularExpression("^[a-zA-Z0-9_@-]+( [a-zA-Z0-9_@-]+)*$")
    elif type == 3:
        reg = QRegularExpression("^[A-Fa-f0-9]{2}")
    elif type == 4:
        reg = QRegularExpression("^[A-Fa-f0-9]{8}")

    reg_val = QRegularExpressionValidator(reg)
    line_edit.setValidator(reg_val)


def check_for_errors(result):
    if not result.errors.messages:
        return False

    error_message = ""
    for msg in result.errors.messages:
        error_message += f"Error: {msg[0]} {msg[1][0]}\n"
    QMessageBox(icon=QMessageBox.Warning, title="Warning", msg=error_message).exec_()
    return True
