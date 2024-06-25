"""spi_commands.py"""

from hardsploit_gui.classes.firmware import Firmware
from hardsploit_gui.classes.generic_commands import GenericCommands
from hardsploit.modules import HardsploitSPI


class SpiCommands(GenericCommands):
    """Custom commands window for SPI commands."""
    def __init__(self, chip, hardsploit_api):
        GenericCommands.__init__(self, chip, "SPI", hardsploit_api)

        # TODO: Put this conversion array at only one place
        self.speeds = {'25.00': 3, '18.75': 4, '15.00': 5, '12.50': 6, '10.71': 7, '9.38': 8, '7.50': 10,
                       '5.00': 15, '3.95': 19, '3.00': 25, '2.03': 37, '1.00': 75, '0.50': 150, '0.29': 255}

        if self.chip.spi_settings:
            self.chip_settings = self.chip.spi_settings[0]

    def _exec_cmd(self, array_sent):
        Firmware(self.bus_name, self._api)

        spi = HardsploitSPI(
            speed=self.speeds[self.chip.spi_settings[0].frequency],
            mode=self.chip.spi_settings[0].mode,
            hardsploit_api=self._api
        )
        # TODO: Manage multiple interaction (n > 1)
        return spi.spi_interact(payload=array_sent)


    
