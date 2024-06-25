"""nrf_settings.py"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMessageBox

from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.db.models import Nrf24l01Setting
from hardsploit_gui.gui.gui_nrf24l01_settings import Ui_NRF24L01_settings


class NrfSettings(QWidget):
    """Settings window for NRF24L01 Module"""

    def __init__(self, chip):
        # Initialize the GUI
        super().__init__()
        self.view = Ui_NRF24L01_settings()
        center_window(self)
        self.view.setupUi(self)
        self.view.lbl_chip.setText(chip.reference)

        self.chip = chip

        # Populate settings from database if available
        if chip.nrf_settings:
            self.feed_settings_form()

    @Slot()
    def save_settings(self):
        # Save new settings in database or edit existing ones
        if self.chip.nrf_settings:
            self.update()
        else:
            self.create()

    def feed_settings_form(self):
        """Fills in the settings form from the settings in the database."""
        self.view.spin_chan.setValue(self.chip.nrf_settings[0].channel)
        self.view.lie_addr.setText("0x" + str(self.chip.nrf_settings[0].address))

    def create(self):
        """Create a new setting element in the database and close the widget."""
        chip_settings = Nrf24l01Setting.create(
                channel=self.view.spin_chan.value(),
                address=self.view.lie_addr.text()[2:],
                chip_id=self.chip.id
            )
        chip_settings.save()
        QMessageBox(QMessageBox.Information, 'Success', 'NRF24L01 settings saved').exec_()
        self.close()

    def update(self):
        """Update the existing setting element in the database and close the widget."""
        nrf_settings = self.chip.nrf_settings[0]
        nrf_settings.channel = self.view.spin_chan.value()
        nrf_settings.address = self.view.lie_addr.text()[2:]
        nrf_settings.save()
        QMessageBox(QMessageBox.Information, 'Success', 'NRF24L01 settings updated').exec_()
        self.close()
