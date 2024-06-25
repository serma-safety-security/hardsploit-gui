"""chip_clone.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from peewee import IntegrityError

from hardsploit_gui.classes.utils import input_restrict, center_window
from hardsploit_gui.gui.gui_chip_clone import Ui_Chip_clone
from hardsploit_gui.classes.error_msg import ErrorMsg


class ChipClone(QWidget):

    def __init__(self, parent, chip):
        super().__init__()
        self.parent = parent
        self.chip = chip
        self.view = Ui_Chip_clone()
        center_window(self)
        self.view.setupUi(self)
        input_restrict(self.view.lie_reference, 2)


    @Slot()
    def clone(self):
        try:
            pins = self.chip.pins
            # Chip
            clone = self.chip
            clone.id = None
            clone.reference = self.view.lie_reference.text()
            clone.save()
            # Pins
            for pin in pins:
                npin = pin
                npin.id = None
                npin.chip_id = clone.id
                npin.save()
        except IntegrityError:
            ErrorMsg.custom("Error", "This reference already exist.")
        except Exception as e:
            ErrorMsg.unknown(e)

        """
        #Setting(s)
        if  self.chip.parallel_setting:
            clone.parralel_setting = self.chip.parallel_setting.dup
            clone.parralel_setting.save()
        if self.chip.spi_setting:
            clone.spi_setting = self.chip.spi_setting.dup
            clone.spi_setting.save()
        if self.chip.i2c_setting:
          clone.i2c_setting = self.chip.i2c_setting.dup
          clone.i2c_setting.save()
        if self.chip.swd_setting:
            clone.swd_setting = self.chip.swd_setting.dup
            clone.swd_setting.save()
        if self.chip.uart_setting:
            clone.uart_setting = self.chip.uart_setting.dup
            clone.uart_setting.save()

        #Command(s) and cmd bytes
        if self.chip.commands:
            for cmd in self.chip.commands:
                clone_cmd = cmd.dup
                clone_cmd.chip_id = clone.id
                clone_cmd.save()
                for byte in cmd.bytes:
                    clone_byte = byte.dup
                    clone_byte.command_id = clone_cmd.id
                    clone_byte.save()

        """

        self.parent.feed_chip_array()
        self.close()
