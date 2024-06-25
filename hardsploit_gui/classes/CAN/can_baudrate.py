"""can_baudrate.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_can_baudrate import Ui_Can_baudrate
from hardsploit.modules.can.can_interact import HardsploitCANInteract


class CanBaudrate(QWidget):

    def __init__(self, parent_view, hardsploit_api):
        super().__init__()
        self._api = hardsploit_api
        Firmware('CAN', self._api)
        self.view = Ui_Can_baudrate()
        center_window(self)
        self.view.setupUi(self)
        self.parent_view = parent_view
        self.can = None
        self.baudrate = None

    @Slot()
    def start_detect(self):
        self.view.btn_start.setEnabled(False)
        self.can = HardsploitCANInteract(
            baud_rate=0,
            crc_poly=50585,
            crc_type=16,
            id=75610,
            n_std_ext=1,
            cmde=0,
            n_data_request=0,
            data=None,
            hardsploit_api=self._api
        )
        self.can.start_baud_rate_detection()
        self.view.btn_stop.setEnabled(True)

    @Slot()
    def stop_detect(self):
        self.view.btn_stop.setEnabled(False)
        self.baudrate = self.can.end_baud_rate_detection()
        self.view.btn_start.setEnabled(True)
        if self.baudrate:
            self.view.lbl_baudrate.setText(f"Baud rate detected: {self.baudrate} Hz")
        else:
            self.view.lbl_baudrate.setText("Baud rate detected: None.")

    @Slot()
    def copy(self):
        self.parent_view.lie_baud_rate.setText(str(self.baudrate))
        self.close()
