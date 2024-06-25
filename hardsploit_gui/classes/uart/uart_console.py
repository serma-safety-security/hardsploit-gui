"""uart_console.py"""

from hardsploit.modules import HardsploitUART
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import QWidget, QScrollBar

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.uart.uart_settings import UartSettings
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_uart_console import Ui_Uart_console


class UartConsole(QWidget):

    def __init__(self, chip, hardsploit_api):
        super().__init__()
        Firmware('UART', hardsploit_api)
        self._api = hardsploit_api
        self.view = Ui_Uart_console()
        self.timer = QTimer(self)
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)
        self.chip = chip
        self.data = ''
        self.uart = None
        self.settings_uart = None

    def closeEvent(self, event):
        if self.timer:
            self.timer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.send()

    @Slot()
    def connect(self):
        try:
            self.uart = HardsploitUART(
                baud_rate=self.chip.uart_settings[0].baud_rate,
                word_width=self.chip.uart_settings[0].word_size,
                use_parity_bit=self.chip.uart_settings[0].parity_bit,
                parity_type=self.chip.uart_settings[0].parity_type,
                nb_stop_bits=self.chip.uart_settings[0].stop_bits_nbr,
                idle_line_level=self.chip.uart_settings[0].idle_line,
                hardsploit_api=self._api
            )
            self.timer.timeout.connect(self.update)
            # QObject.connect(self.timer, SIGNAL('timeout()'), self, SLOT('update()'))
            self.timer.start(100)
            self.data += 'Listening and ready to go !' + chr(0x0d)
            self.view.console.setPlainText(self.data)
            self.scroll_down()
            self.sender().setEnabled(False)
            self.view.btn_disconnect.setEnabled(True)
        except Exception as e:
            ErrorMsg.custom("Error", "Check UART settings")

    @Slot()
    def disconnect(self):
        self.timer.stop()
        self.data += 'Disconnected' + chr(0x0d)
        self.view.console.setPlainText(self.data)
        self.scroll_down()
        self.sender().setEnabled(False)
        self.view.btn_connect.setEnabled(True)

    @Slot()
    def send(self):
        if not self.uart or not self.timer:
            return False
        input_text = self.view.lie_cmd.text()
        if self.view.mode_select.currentText() == 'Advanced mode':
            try:
                input_text = eval(input_text, {"__builtins__": {}}, {})
            except (NameError, SyntaxError):
                return ErrorMsg.wrong_syntax()
        elif not self.view.lie_cmd.text().isascii():
            return ErrorMsg.ascii_only()
        packet = []
        for x in input_text:
            packet.append(ord(x))
        if self.chip.uart_settings[0].return_type == 0:
            packet.append(13)
        elif self.chip.uart_settings[0].return_type == 1:
            packet.append(10)
        elif self.chip.uart_settings[0].return_type == 2:
            packet.append(13)
            packet.append(10)
        self.view.lie_cmd.clear()
        self.uart.write(payload=packet)

    @Slot()
    def select_mode(self):
        if self.view.mode_select.currentText() == 'Advanced mode':
            self.view.lie_cmd.setStyleSheet(
                "QLineEdit { background: rgb(255, 226, 187); selection-background-color: rgb(233, 99, 0); }")
        else:
            self.view.lie_cmd.setStyleSheet(
                "QLineEdit { background: rgb(255, 255, 255); }")

    @Slot()
    def update(self):
        # received = @uart.sendAndReceived.collect{|i| i.chr}
        received = self.uart.send_and_received()
        if len(received) > 0 and bytes(received):
            try:
                self.data += bytes(received).decode()
            except UnicodeDecodeError:
                self.data += "Can't decode: " + str(bytes(received)) + "\n"
            self.view.console.setPlainText(self.data)
        self.scroll_down()

    @Slot()
    def clear_console(self):
        self.view.console.clear()
        self.data = ''

    @Slot()
    def open_settings(self):
        self.settings_uart = UartSettings(self.chip, self._api)
        self.settings_uart.setWindowModality(Qt.ApplicationModal)
        self.settings_uart.show()

    def scroll_down(self):
        sb = self.view.console.verticalScrollBar()
        sb.setValue(sb.maximum())
