"""firmware.py"""

import os
from pathlib import Path
from time import sleep

from PySide6.QtWidgets import QMessageBox

from hardsploit_gui.classes import utils
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.progress_bar import ProgressBar
from hardsploit_gui.db.models import Bus, Use
from hardsploit.core import HardsploitConstant, HardsploitUtils


class Firmware:

    def __init__(self, firmware, hardsploit_api):
        from hardsploit_gui.main import HardsploitGUI
        if HardsploitUtils.get_number_of_board_available() < 1:
            ErrorMsg.hardsploit_not_found()
        else:
            if HardsploitGUI.currentFirmware != firmware:
                if HardsploitGUI.currentFirmware != 'uC':
                    utils.progress_bar = ProgressBar("Upload firmware :")
                    utils.progress_bar.show()
                if firmware in ['I2C', 'I2C_SNIFFER', 'SPI', 'SPI_SNIFFER', 'PARALLEL', 'MUX_PARALLEL', 'SWD', 'UART',
                                'CAN', 'CAN_INTERACT']:
                    hardsploit_api.load_firmware(firmware)
                elif firmware == 'uC':
                    msg = QMessageBox()
                    msg.setWindowTitle("Microcontroller update")
                    msg.setText("Hardsploit must be in bootloader mode and dfu-util package must be installed in order"
                                " to continue. Proceed ?")
                    msg.setIcon(QMessageBox.Question)
                    msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Cancel)
                    if msg.exec_() == QMessageBox.Ok:
                        os.system("dfu-util -D 0483:df11 -a 0 -s 0x08000000 -R --download " + str(
                            Path(__file__)) + "'/../Firmwares/UC/HARDSPLOIT_FIRMWARE_UC.bin'")
                if firmware != 'uC':
                    if firmware == "SPI_SNIFFER":
                        firmware = "SPI"
                    HardsploitGUI.currentFirmware = firmware
                utils.progress_bar.close()
                sleep(2)
            if firmware in ['PARALLEL', 'SWD', 'UART', 'I2C', 'SPI']:
                # CrossWiring
                crossvalue = []
                for i in range(64):
                    crossvalue.append(i)
                pin_group = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                current_bus = Bus.get(Bus.name == firmware)
                for s in Use.select().where(Use.bus == current_bus.id):
                    s = s.signal
                    hardsploit_pin_number = pin_group.index(s.pin[0]) * 8 + int(s.pin[1])
                    crossvalue[hardsploit_pin_number] = HardsploitConstant.get_signal_id(signal=s.name)
                    crossvalue[HardsploitConstant.get_signal_id(signal=s.name)] = hardsploit_pin_number
                hardsploit_api.set_cross_wiring(value=crossvalue)
