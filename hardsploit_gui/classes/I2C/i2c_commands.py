"""i2c_commands.py"""

from PySide6.QtCore import Slot

from hardsploit_gui.db.models import Command
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.generic_commands import GenericCommands
from hardsploit_gui.classes.I2C.i2c_command import I2cCommand

from hardsploit.modules import HardsploitI2c


class I2cCommands(GenericCommands):
    """Custom commands window for I2C commands."""
    def __init__(self, chip, hardsploit_api):
        GenericCommands.__init__(self, chip, "I2C", hardsploit_api)

        if self.chip.i2c_settings:
            self.chip_settings = self.chip.i2c_settings[0]

    def _get_context_actions(self):
        return (self.view.actionExecute,
                self.view.actionEdit,
                self.view.actionConcatenate,
                self.view.actionTemplate,
                self.view.actionDelete,
                )

    @Slot()
    def create(self):
        create_cmd = I2cCommand(self.chip, self.bus_id, self)
        create_cmd.show()

    def _concatenate(self):
        """Action to execute when the user wants to concatenate 2 commands."""
        if self.bus_name != "I2C":
            return ErrorMsg.concat_disallow()
        if len(self.view.tbl_cmd.selectedItems()) != 2:
            return ErrorMsg.concat_nbr()
        cmd1 = Command.get(Command.name == self.view.tbl_cmd.selectedItems()[0].text())
        cmd2 = Command.get(Command.name == self.view.tbl_cmd.selectedItems()[1].text())
        if not self.check_concatenation_size(cmd1.bytes, cmd2.bytes):
            return False

        Command.create(
            name='New concatenation',
            description=f"Concatenation of {cmd1.name} and {cmd2.name} commands",
            bus_id=self.bus_id,
            chip_id=self.chip.id
        )

    @staticmethod
    def check_concatenation_size(bytes_cmd_1, bytes_cmd_2):
        try:
            check_size = []
            for b1 in bytes_cmd_1:
                check_size.append(b1.value)
            for b2 in bytes_cmd_2:
                check_size.append(b2.value)
            count = 0
            i = 0
            while i <= len(check_size) - 1:
                low_byte = check_size[i]
                high_byte = check_size[i + 1]
                command_type = check_size[i + 2]
                count += (int(low_byte, 16) + (int(high_byte, 16) << 8))
                if int(command_type, 16) % 2 == 0:  # WRITE
                    i += ((int(low_byte, 16) + (int(high_byte, 16) << 8)) + 3)
                else:  # READ
                    i = (i + 3)
            if count > 2000:
                raise ValueError()
            return True
        except ValueError:
            ErrorMsg.i2c_cmd_too_long()
        except Exception as e:
            ErrorMsg.unknown(e)


    def _exec_cmd(self, array_sent, _n=1):
        Firmware(self.bus_name, self._api)
        speed = None
        # TODO: else case
        if self.chip.i2c_settings[0].frequency in [40, 100, 400, 1000]:
            if self.chip.i2c_settings[0].frequency == 100:
                speed = 0
            elif self.chip.i2c_settings[0].frequency == 400:
                speed = 1
            elif self.chip.i2c_settings[0].frequency == 1000:
                speed = 2
            elif self.chip.i2c_settings[0].frequency == 40:
                speed = 3

            i2c = HardsploitI2c(speed=speed, hardsploit_api=self._api)

            # TODO: Multiple interaction (n > 1)
            return i2c.i2c_interact(payload=array_sent)
