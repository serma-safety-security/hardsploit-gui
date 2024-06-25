"""uart_baudrate.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_uart_baudrate import Ui_Uart_baudrate
from hardsploit.modules import HardsploitUART


class UartBaudrate(QWidget):

    def __init__(self, parent_view, hardsploit_api):
        super().__init__()
        Firmware('UART', hardsploit_api)
        self._api = hardsploit_api
        self.view = Ui_Uart_baudrate()
        center_window(self)
        self.view.setupUi(self)
        self.parent_view = parent_view
        self.uart = None
        self.baudrate = None

    @Slot()
    def start_detect(self):
        self.view.btn_start.setEnabled(False)
        # HardsploitGUI.app.processEvents()
        self.uart = HardsploitUART(
                        baud_rate=115200,
                        word_width=8,
                        use_parity_bit=0,
                        parity_type=0,
                        nb_stop_bits=1,
                        idle_line_level=1,
                        hardsploit_api=self._api)

        self.uart.enable_measure_baud_rate()
        self.view.btn_stop.setEnabled(True)

    @Slot()
    def stop_detect(self):
        self.view.btn_stop.setEnabled(False)
        self.baudrate = self.uart.measure_baud_rate()
        self.uart.disable_measure_baud_rate()
        self.view.btn_start.setEnabled(True)
        if self.baudrate != 0:
            self.view.lbl_baudrate.setText(f"Baud rate detected: {self.baudrate} Hz")
        else:
            self.view.lbl_baudrate.setText("Baud rate detected: None.")

    @Slot()
    def copy(self):
        self.parent_view.lie_baud_rate.setText(str(self.baudrate))
        self.close()
