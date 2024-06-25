"""wire_helper.py"""

import math

from PySide6.QtCore import QRectF, Slot, Qt
from PySide6.QtGui import QCursor, QColor, QFont
from PySide6.QtWidgets import QGraphicsTextItem, QWidget, QGraphicsScene

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.db.models import *
from hardsploit_gui.gui.gui_wire_helper import Ui_Wire_helper
from hardsploit_gui.classes.utils import center_window
from hardsploit.core import HardsploitError

PIN_ENABLED = None


class WireHelper(QWidget):

    def __init__(self, chip, hardsploit_api):
        # try:
        super().__init__()

        global PIN_ENABLED
        self.wire_helper_gui = Ui_Wire_helper()
        center_window(self)
        self.wire_helper_gui.setupUi(self)
        self.chip = chip
        self._api = hardsploit_api
        PIN_ENABLED = None
        self._api.set_wiring_leds(value=0x0000000000000000)
        self.scene = QGraphicsScene()
        self.wire_helper_gui.lbl_chip.setText(f"Your chip ({chip.reference}):")
        if chip.package.shape:
            self.draw_rect()
        else:
            self.draw_square()
        self.wire_helper_gui.gView.setScene(self.scene)

        """
        except HardsploitError.HARDSPLOIT_NOT_FOUND:
            ErrorMsg.hardsploit_not_found()
        except HardsploitError.USB_ERROR:
            ErrorMsg.usb_error()
        except Exception as msg:
            ErrorMsg.unknown(msg)
        """

    def close_event(self):
        try:
            self._api.set_wiring_leds(value=0xFF00FF00FF00FF00)
        except HardsploitError.HardsploitNotFound:
            ErrorMsg.hardsploit_not_found()
        except HardsploitError.USBError:
            ErrorMsg.usb_error()
        except Exception as msg:
            ErrorMsg.unknown(msg)

    @Slot()
    def rotate_scene(self):
        self.wire_helper_gui.gView.rotate(90)
    
    def draw_square(self):
        total_pin_nbr = len(self.chip.pins)
        pin_by_side = math.ceil(total_pin_nbr / 4)
        c_height = 14*(pin_by_side + 4)  # Chip's height (+4 because we add a space equal to one pin for each corner)
        self.scene.addRect(QRectF(0, 0, c_height, c_height))
        y = 32
        y2 = c_height - 38
        x = 32
        x2 = c_height - 38
        for i in range(1, total_pin_nbr+1):
            # Face 1
            if i <= pin_by_side:
                y_sig = y
                y_num = y
                UniqPin(self.scene, i, self.chip, -70, y_sig - 12, 0, y_num - 12, 0, y, -20, 6, False, self._api)
                y = y + 14  # Space between each pin
            elif pin_by_side < i <= math.ceil(total_pin_nbr / 2):
                # Face 2
                x_sig2 = x
                x_num2 = x
                UniqPin(self.scene, i, self.chip, x_sig2 - 12, c_height + 55, x_num2 - 12, c_height, x, c_height, 6, 20, True, self._api)
                x = x + 14
            elif total_pin_nbr / 2 < i <= (total_pin_nbr - pin_by_side):
                # Face 3
                x_sig = c_height + 24
                y_sig = y2
                y_num = y2
    
                if i < 10:
                    x_num = c_height - 20
                elif 10 <= i < 100:
                    x_num = c_height - 25
                else:
                    x_num = c_height - 35
                UniqPin(self.scene, i, self.chip, x_sig, y_sig - 12, x_num, y_num - 12, c_height, y2, 20, 6, False, self._api)
                y2 = y2 - 14
            else:
                # Face 4
                x_sig2 = x2
                x_num2 = x2

                if i < 10:
                    y_num2 = 20
                elif 10 <= i < 100:
                    y_num2 = 30
                else:
                    y_num2 = 40
                UniqPin(self.scene, i, self.chip, x_sig2 - 12, -20, x_num2 - 12, y_num2, x2, 0, 6, -20, True, self._api)
                x2 = x2 - 14

    def draw_rect(self):
        total_pin_nbr = len(self.chip.pins)
        pin_by_side = total_pin_nbr / 2
        c_height = 14 * (pin_by_side + 2)  # +2 because we add a space equal to one pin for each corner
        self.scene.addRect(QRectF(0, 0, c_height, c_height))
        # Add the pins + text
        y = 18
        y2 = c_height - 24
        for i in range(1, total_pin_nbr+1):
            # Face 1
            if i <= total_pin_nbr / 2:
                y_sig = y
                y_num = y
                UniqPin(self.scene, i, self.chip, -70, y_sig - 12, 0, y_num - 12, 0, y, -20, 6, False, self._api)
                y = y + 14
            # Face 2
            else:
                x_sig = c_height + 24
                y_sig = y2
                y_num = y2

                if i < 10:
                    x_num = c_height - 20
                elif 10 <= i < 100:
                    x_num = c_height - 25
                else:
                    x_num = c_height - 35

                UniqPin(self.scene, i, self.chip, x_sig, y_sig - 12, x_num, y_num - 12, c_height, y2, 20, 6, False, self._api)
                y2 = y2 - 14

#
# Custom Item - To trigger events on the graphics text items
#


class CustomItem(QGraphicsTextItem):

    def __init__(self, value, hardsploit_api):
        super().__init__(value)
        self._api = hardsploit_api
        self.u_pin = None
        self.api_value = None

    def set_pin(self, upin, api_value):
        self.u_pin = upin
        self.api_value = api_value

    @staticmethod
    def bounding_rect():
        rect = QRectF()
        rect.setHeight(20)
        rect.setWidth(65)
        rect.setTop(5)
        return rect

    def mousePressEvent(self, _):
        pin = self.u_pin
        pin.set_color()
        pin.signal_txt.clearFocus()
        pin.nbr_txt.clearFocus()
        if self.api_value.name == 'NA':
            self._api.set_wiring_leds(value=0x0000000000000000)
            return False
        pin_group = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        hardsploit_pin_number = pin_group.index(self.api_value.pin[0]) * 8 + int(self.api_value.pin[1])
        self._api.set_wiring_leds(value=2 ** hardsploit_pin_number)
        return True

    def mouseDoubleClickEvent(self, _):
        pin = self.u_pin
        pin.signal_txt.clearFocus()
        pin.nbr_txt.clearFocus()

#
# UniqPin - Contain all data linked to one pin on the graphic
#


class UniqPin:
    
    def __init__(self, scene, pin_num, pin_chip, x_sig, y_sig, x_num, y_num, x_rect, y_rect, w_rect, h_rect, rotation, hardsploit_api):
        signal = Pin.select().where((Pin.chip == pin_chip.id) & (Pin.number == pin_num)).first().signal
        self.signal_txt = CustomItem(signal.name, hardsploit_api)
        self.signal_txt.cursor = QCursor(Qt.PointingHandCursor)
        self.signal_txt.set_pin(self, signal)
        self.signal_txt.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.signal_txt.setX(x_sig)
        self.signal_txt.setY(y_sig)
        self.on = None
        self.off = None
        self.bold = None
        if rotation:
            self.signal_txt.setRotation(270.00)
        scene.addItem(self.signal_txt)

        self.nbr_txt = CustomItem(str(pin_num), hardsploit_api)
        self.nbr_txt.cursor = QCursor(Qt.PointingHandCursor)
        self.nbr_txt.set_pin(self, signal)
        self.nbr_txt.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.nbr_txt.setX(x_num)
        self.nbr_txt.setY(y_num)
        if rotation:
            self.nbr_txt.setRotation(270.00)
        scene.addItem(self.nbr_txt)
        self.pin_graph_item = scene.addRect(x_rect, y_rect, w_rect, h_rect)

    def set_color(self):
        global PIN_ENABLED
        # Colors
        self.on = QColor(0, 0, 255)
        self.off = QColor(0, 0, 0)
        # Disable the pin if another pin is already enabled
        if PIN_ENABLED:
            PIN_ENABLED.unset_color()
        # Light the new pin
        self.nbr_txt.setDefaultTextColor(self.on)
        self.signal_txt.setDefaultTextColor(self.on)
        self.bold = QFont()
        self.bold.setBold(True)
        self.signal_txt.setFont(self.bold)
        PIN_ENABLED = self

    def unset_color(self):
        self.nbr_txt.setDefaultTextColor(self.off)
        self.signal_txt.setDefaultTextColor(self.off)
        self.bold.setBold(False)
        self.signal_txt.setFont(self.bold)
