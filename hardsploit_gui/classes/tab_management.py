"""table_management.py"""

import os
import platform

from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap, QBrush
from PySide6.QtWidgets import (QTreeWidgetItem, QLabel, QMessageBox,
                                             QTableWidgetItem, QWidget, QFileDialog)

from hardsploit.core import HardsploitAPI, HardsploitConstant, HardsploitUtils

from hardsploit_gui.gui.gui_tab_management import Ui_Tab_management
from .CAN.can_settings import CanSettings
from .chip_clone import ChipClone
from .console import Console
from .error_msg import ErrorMsg
from .firmware import Firmware
from .I2C.i2c_read import I2cRead
from .I2C.i2c_settings import I2cSettings
from .I2C.i2c_write import I2cWrite
from .I2C.i2c_commands import I2cCommands
from .SPI.spi_read import SpiRead
from .SPI.spi_settings import SpiSettings
from .SPI.spi_sniffer import SpiSniffer
from .SPI.spi_write import SpiWrite
from .SPI.spi_commands import SpiCommands
from .NRF24L01.nrf_settings import NrfSettings
from .NRF24L01.nrf_scan import NrfScan
from .NRF24L01.nrf_sniffer import NrfSniffer
from .NRF24L01.nrf_commands import NrfCommands
from .export import Exportdata
from .export import Exportdata

from .signal_mapper import SignalMapper
from .wire_helper import WireHelper
from .chip_editor import ChipEditor
from .swd.swd import Swd
from .swd.swd_settings import SwdSettings
from .utils import center_window, input_restrict

from hardsploit_gui.db.models import *
from .uart.uart_console import UartConsole
from .uart.uart_settings import UartSettings



class TabManagement(QWidget):

    def __init__(self, version_gui):
        super().__init__()
        # try:
        self.view = Ui_Tab_management()
        center_window(self)
        self.view.setupUi(self)
        self.view.img_search.setPixmap(QPixmap(str(Path(__file__).parent.resolve())
                                               + "/../images/search.png"))
        input_restrict(self.view.lie_search, 2)
        self._api = None
        self.feed_chip_array()
        self.feed_manufacturer_cbx()
        self.feed_type_cbx()
        self.console = Console(self.view.tbl_console)
        self.version_gui = version_gui
        self.hardsploit_board_status = QLabel()
        self.check_hardsploit_connection()
        self.chip_clicked = None

    def set_hs_board_status(self, connected):
        if connected:
            self.hardsploit_board_status.setText("Hardsploit board: connected " +
                                                 f"- version {self._api.get_version_number()} " +
                                                 f"- api V{HardsploitConstant.VERSION.API}")
        else:
            self.hardsploit_board_status.setText("Hardsploit board: disconnected")

    def feed_type_cbx(self):
        for m in Manufacturer.select():
            self.view.cbx_manufacturer.addItem(m.name)

    def feed_manufacturer_cbx(self):
        for c in ChipType.select():
            self.view.cbx_type.addItem(c.name)

    def console_view(self):
        if self.sender().isChecked:
            self.view.tbl_console.show()
        else:
            self.view.tbl_console.hide()

    @staticmethod
    def get_chip_buses(chip):
        chip_buses = set()
        for pin in chip.pins:
            bus = Bus.select().join(Use, JOIN.LEFT_OUTER).where(
                Use.signal_id == pin.signal_id).get()
            chip_buses.add(bus.name)

        # Add special bus depending on chip types
        if chip.chip_type.name == "NRF24L01":
            chip_buses.add("NRF24L01")

        if 'NA' in chip_buses:
            chip_buses.remove("NA")
        return chip_buses

    @Slot(int, int)
    def load_tree(self, line, column):
        if column != 0:
            return 0
        self.view.tw_chip.clear()
        self.chip_clicked = Chip.get(Chip.reference == self.view.tbl_chip.item(line, column).text())
        # CHIP LEVEL
        chip_lvl = QTreeWidgetItem()
        chip_lvl.setText(0, self.view.tbl_chip.item(line, column).text())
        self.view.tw_chip.addTopLevelItem(chip_lvl)
        chip_lvl.setExpanded(True)
        # ACTION LEVEL
        action_lvl = QTreeWidgetItem()
        action_lvl.setText(0, 'Manage')
        chip_lvl.addChild(self.create_action_nodes(action_lvl))
        action_lvl.setExpanded(True)

        # BUS LEVEL(S)
        chip_bus = self.get_chip_buses(self.chip_clicked)
        for b in chip_bus:
            bus_lvl = QTreeWidgetItem()
            bus_lvl.setText(0, b)
            chip_lvl.addChild(self.create_bus_nodes(b, bus_lvl))
            if bus_lvl:
                bus_lvl.setExpanded(True)
        return None

    def create_action_nodes(self, parent_node):
        wiring_lvl = QTreeWidgetItem(["Wiring"])
        edit_lvl = QTreeWidgetItem(["Edit"])
        clone_lvl = QTreeWidgetItem(["Clone"])
        export_lvl = QTreeWidgetItem(["Export"])
        delete_lvl = QTreeWidgetItem(["Delete"])
        if not self._api:
            wiring_lvl.setDisabled(True)
            wiring_lvl.setForeground(0, QBrush(Qt.gray))
        parent_node.addChild(wiring_lvl)
        parent_node.addChild(edit_lvl)
        parent_node.addChild(clone_lvl)
        parent_node.addChild(export_lvl)
        parent_node.addChild(delete_lvl)
        return parent_node

    def create_bus_nodes(self, bus, parent_node):
        # For each bus, the list of possible actions and if hardsploitAPI is needed.
        # If HardsploitAPI is needed for a given item, it will be disabled if the
        # API is not available

        # Common busses aliases
        #       (<action_name>, <api_needed>)
        # pin_scanner = ("PIN Scanner", True)
        commands = ("Commands", False)
        settings = ("Settings", False)
        sniffer = ("Sniffer", True)
        console = ("Console", True)
        detect = ("Detect", True)
        write = ("Write", True)
        read = ("Read", True)
        erase = ("Erase", True)
        scan = ("Scan", True)

        busses = {
                "UART": [
                            settings,
                            console,
                        ],
                "SWD":  [
                            settings,
                            # pin_scanner,
                            detect,
                            write,
                            read,
                            erase,
                        ],
                "SPI":  [
                            settings,
                            commands,
                            write,
                            read,
                            sniffer,
                        ],
                "NRF24L01": [
                            settings,
                            scan,
                            sniffer,
                            commands,
                        ],
                "CAN":  [
                            settings,
                            write,
                            read,
                            sniffer,
                        ],
                "I2C":  [
                            settings,
                            # pin_scanner,
                            commands,
                            write,
                            read,
                            # sniffer,
                        ],
                "PARELLEL": [
                            settings,
                            # Write, # Not implemented yet
                            read,
                        ]
                }

        items = []
        for action, api_needed in busses[bus]:
            item = QTreeWidgetItem([action])
            if api_needed and not self._api:
                item.setDisabled(True)
                item.setForeground(0, QBrush(Qt.gray))
            items.append(item)
        parent_node.addChildren(items)

        return parent_node

    @Slot()
    def feed_chip_array(self):
        self.view.tbl_chip.clearContents()
        chips = self.filter_chips()
        self.view.tbl_chip.setRowCount(len(chips))
        # Insert chip table rows
        i = 0
        for chip in chips:
            # Reference
            item = QTableWidgetItem(chip.reference)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.view.tbl_chip.setItem(i, 0, item)

            # Chip Type
            chip_type = ChipType.get(ChipType.id == chip.chip_type_id)
            item2 = QTableWidgetItem(chip_type.name)
            item2.setFlags(Qt.ItemIsEnabled)
            self.view.tbl_chip.setItem(i, 1, item2)

            # Chip Manufacturer
            manufacturer = Manufacturer.get(Manufacturer.id == chip.manufacturer_id)
            item3 = QTableWidgetItem(manufacturer.name)
            item3.setFlags(Qt.ItemIsEnabled)
            self.view.tbl_chip.setItem(i, 2, item3)

            bus_list = self.get_chip_buses(chip)
            bus_list_str = ''

            for b in bus_list:
                bus_list_str += str(b) + ' '

                # Chip Bus(es)
                item4 = QTableWidgetItem(bus_list_str)
                item4.setFlags(Qt.ItemIsEnabled)
                self.view.tbl_chip.setItem(i, 3, item4)

            i += 1

        self.view.tbl_chip.resizeColumnsToContents()
        self.view.tbl_chip.resizeRowsToContents()
        self.view.tbl_chip.horizontalHeader().setStretchLastSection(True)
        self.view.tbl_console.horizontalHeader().setStretchLastSection(True)
        self.view.tbl_chip.verticalHeader().setStretchLastSection(False)
        self.view.tbl_console.verticalHeader().setStretchLastSection(False)

    def filter_chips(self):
        if not self.view.lie_search.text():
            chips = Chip.select()
        else:
            chips = Chip.select().where(Chip.reference.contains(self.view.lie_search.text()))

        if self.view.cbx_manufacturer.currentIndex() != 0:
            man_id = Manufacturer.get(
                Manufacturer.name == self.view.cbx_manufacturer.currentText()
            ).id
            chips = Chip.select().where(Chip.manufacturer == man_id)

        if self.view.cbx_type.currentIndex() != 0:
            type_id = ChipType.get(ChipType.name == self.view.cbx_type.currentText()).id
            chips = Chip.select().where(Chip.chip_type == type_id)

        return chips

    @Slot(QTreeWidgetItem, int)
    def load_chip_action(self, item):
        if item.childCount() != 0:
            return 0
        if item.parent().text(0) == 'Manage':
            if item.text(0) == 'Wiring' and self._api:
                self.wire_chip()
            elif item.text(0) == 'Edit':
                self.edit_chip()
            elif item.text(0) == 'Clone':
                self.clone_chip()
            elif item.text(0) == 'Export':
                Exportdata(self.chip_clicked)
            elif item.text(0) == 'Delete':
                self.delete_chip()
        else:
            if item.parent().text(0) == 'SPI':
                self.load_spi_module(item.text(0))
            elif item.parent().text(0) == 'NRF24L01':
                self.load_nrf_module(item.text(0))
            elif item.parent().text(0) == 'CAN':
                self.load_can_module(item.text(0))
            elif item.parent().text(0) == 'I2C':
                self.load_i2c_module(item.text(0))
            elif item.parent().text(0) == 'PARALLEL':
                self.load_parallel_module(item.text(0))
            elif item.parent().text(0) == 'SWD':
                self.load_swd_module(item.text(0))
            elif item.parent().text(0) == 'UART':
                self.load_uart_module(item.text(0))
        return None

    def load_spi_module(self, spi_module):
        if spi_module == 'Settings':
            self.spi_settings = SpiSettings(self.chip_clicked)
            self.spi_settings.show()
        elif spi_module == 'Read' and self._api:
            self.spi_read = SpiRead(self.chip_clicked, self._api)
            self.spi_read.show()
        elif spi_module == 'Write' and self._api:
            self.spi_write = SpiWrite(self.chip_clicked, self._api)
            self.spi_write.show()
        elif spi_module == 'Sniffer' and self._api:
            self.spi_sniffer = SpiSniffer(self.chip_clicked, self._api)
            self.spi_sniffer.show()
        elif spi_module == 'Commands':
            self.spi_commands = SpiCommands(self.chip_clicked, self._api)
            self.spi_commands.show()

    def load_nrf_module(self, nrf_module):
        if nrf_module == 'Settings':
            self.nrf_settings = NrfSettings(self.chip_clicked)
            self.nrf_settings.show()
        if nrf_module == 'Scan' and self._api:
            self.nrf_scan = NrfScan(self.chip_clicked, self._api)
            self.nrf_scan.show()
        if nrf_module == 'Sniffer' and self._api:
            self.nrf_recv = NrfSniffer(self.chip_clicked, self._api)
            self.nrf_recv.show()
        if nrf_module == 'Commands':
            self.nrf_cmds = NrfCommands(self.chip_clicked, self._api)
            self.nrf_cmds.show()

    def load_can_module(self, can_module):
        if can_module == 'Settings':
            self.can_settings = CanSettings(self.chip_clicked, self._api)
            self.can_settings.show()
        elif can_module == 'Read' and self._api:
            # self.can_read = CanRead(self.chip_clicked, self._api)
            # self.can_read.show()
            pass
        elif can_module == 'Write' and self._api:
            # self.can_write = CanWrite(self.chip_clicked, self._api)
            # self.can_write.show()
            pass
        elif can_module == 'Sniffer' and self._api:
            # self.can_sniffer = CanSniffer(self.chip_clicked, self._api)
            # self.can_sniffer.show()
            pass

    def load_i2c_module(self, i2c_module):
        if i2c_module == 'Settings':
            self.i2c_settings = I2cSettings(self.chip_clicked, self._api)
            self.i2c_settings.show()
        elif i2c_module == 'Read' and self._api:
            self.i2c_read = I2cRead(self.chip_clicked, self._api)
            self.i2c_read.show()
        elif i2c_module == 'Write' and self._api:
            self.i2c_write = I2cWrite(self.chip_clicked, self._api)
            self.i2c_write.show()
        elif i2c_module == 'PIN Scanner' and self._api:
            pass
            # I2cScanner().show()
        elif i2c_module == 'Commands':
            self.i2c_commands = I2cCommands(self.chip_clicked, self._api)
            self.i2c_commands.show()
        elif i2c_module == 'Sniffer' and self._api:
            pass
            # I2cSniffer(self.chip_clicked).show()

    def load_parallel_module(self, parallel_module):
        pass

    def load_swd_module(self, swd_module):
        if swd_module == 'Settings':
            self.swd_settings = SwdSettings(self.chip_clicked)
            self.swd_settings.show()
            self.show()
        elif swd_module == 'PIN Scanner' and self._api:
            pass
            # Swd_scanner.new.show
        elif swd_module == 'Detect' and self._api:
            Swd(self.chip_clicked, self.console, self._api).detect()
        elif swd_module == 'Write' and self._api:
            filepath = QFileDialog.getOpenFileName(self, 'Select a file', '/')[0]
            if filepath:
                Swd(self.chip_clicked, self.console, self._api).write(filepath)
        elif swd_module == 'Read' and self._api:
            filepath = QFileDialog.getSaveFileName(self, 'Select a file', '/')[0]
            if filepath:
                Swd(self.chip_clicked, self.console, self._api).read(filepath)
        elif swd_module == 'Erase' and self._api:
            Swd(self.chip_clicked, self.console, self._api).erase()

    def load_uart_module(self, uart_module):
        if uart_module == 'Settings':
            self.settings_uart = UartSettings(self.chip_clicked, self._api)
            self.settings_uart.setWindowModality(Qt.ApplicationModal)
            self.settings_uart.show()
        elif uart_module == 'Console' and self._api:
            if HardsploitUtils.get_number_of_board_available() < 1:
                return ErrorMsg.hardsploit_not_found()
            self.console_uart = UartConsole(self.chip_clicked, self._api)
            self.console_uart.setWindowModality(Qt.ApplicationModal)
            self.console_uart.show()
        return None

    @Slot()
    def add_chip(self):
        self.a_chip = ChipEditor(self, 'none', 'new')
        self.a_chip.show()

    @Slot()
    def edit_chip(self):
        try:
            if not self.chip_clicked:
                return ErrorMsg.no_chip_loaded()
            self.e_chip = ChipEditor(self, self.chip_clicked, 'edit')
            self.e_chip.show()
            return None
        except Exception as e:
            ErrorMsg.unknown(e)

    @Slot()
    def clone_chip(self):
        if not self.chip_clicked:
            return ErrorMsg.no_chip_loaded()
        self.c_chip = ChipClone(self, self.chip_clicked)
        self.c_chip.show()

    @Slot()
    def delete_chip(self):
        if not self.chip_clicked:
            return ErrorMsg.no_chip_loaded()
        msg = QMessageBox()
        msg.setWindowTitle("Delete current chip")
        msg.setText(f"Delete {self.chip_clicked.reference}? Commands will be deleted too.")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            self.chip_clicked.delete_instance()
            # self.session.query(Chip).filter_by(id=self.chip_clicked.id).delete()
            self.chip_clicked = None
            self.feed_chip_array()
            self.view.tw_chip.clear()

    @Slot()
    def wire_chip(self):
        if HardsploitUtils.get_number_of_board_available() < 1:
            self._api = None
            self.check_hardsploit_connection()
            return ErrorMsg.hardsploit_not_found()
        if not self.chip_clicked:
            return ErrorMsg.no_chip_loaded()
        self.wire_helper = WireHelper(self.chip_clicked, self._api)
        self.wire_helper.setWindowModality(Qt.ApplicationModal)
        self.wire_helper.show()

    @Slot()
    def import2(self):
        pass

    @Slot()
    def export(self):
        export = Export(1)
        export.show()
        pass


    @Slot()
    def display_current_firmware(self):
        from hardsploit_gui import HardsploitGUI
        if not HardsploitGUI.currentFirmware:
            QMessageBox(QMessageBox.Information, 'Firmware', 'No firmware loaded').exec_()
        else:
            QMessageBox(QMessageBox.Information,
                        'Firmware',
                        f"Actual firmware: {HardsploitGUI.currentFirmware}"
                        ).exec_()

    @Slot()
    def set_firmware(self):
        Firmware(self.sender().objectName()[6:len(self.sender().objectName())], self._api)
        self.display_current_firmware()

    @Slot()
    def update_uc_firmware(self):
        Firmware('uC', self._api)

    @Slot()
    def get_hardsploit_versions(self):
        if HardsploitUtils.get_number_of_board_available() > 0:
            QMessageBox(QMessageBox.Information, 'Hardsploit versions',
                        f"GUI VERSION : {self.version_gui}\n" +
                        f"API VERSION : {HardsploitConstant.VERSION.API}\n" +
                        f"BOARD : {self._api.get_version_number()}"
                        ).exec_()
        else:
            QMessageBox(QMessageBox.Information, 'Hardsploit versions',
                        f"GUI VERSION : {self.version_gui}\n" +
                        f"API VERSION : {HardsploitConstant.VERSION.API}\n").exec_()

    @Slot()
    def get_log_path(self):
        from hardsploit_gui import HardsploitGUI
        msg = QMessageBox()
        msg.setWindowTitle('Log file path')
        msg.setText(f"Path: {HardsploitGUI.LOG_FILE_PATH}")
        msg.setIcon(QMessageBox.Information)
        open_btn = msg.addButton('Open file', QMessageBox.ActionRole)
        open_btn.setObjectName('open_btn')
        msg.exec_()
        if msg.clickedButton().objectName() == 'open_btn':
            if platform.system() == "Windows":
                os.popen(f"start {HardsploitGUI.LOG_FILE_PATH}")
            else:
                os.popen(f"xdg-open {HardsploitGUI.LOG_FILE_PATH}")

    @Slot()
    def get_db_path(self):
        from hardsploit_gui import HardsploitGUI
        msg = QMessageBox()
        msg.setWindowTitle('Database path')
        msg.setText(f"Path: {HardsploitGUI.DB_FILE_PATH}\n")
        msg.setIcon(QMessageBox.Information)
        open_btn = msg.addButton('Open file', QMessageBox.ActionRole)
        open_btn.setObjectName('open_btn')
        backup_btn = msg.addButton('Create backup', QMessageBox.ActionRole)
        backup_btn.setObjectName('backup_btn')
        msg.exec_()

        if msg.clickedButton().objectName() == 'backup_btn':
            os.popen(f"cp {HardsploitGUI.DB_FILE_PATH} {HardsploitGUI.DB_FILE_PATH}.bck")
            QMessageBox(QMessageBox.Information, 'Backup status', 'db.bck created').exec_()

        if msg.clickedButton().objectName() == 'open_btn':
            if platform.system() == "Windows":
                os.popen(f"start {HardsploitGUI.DB_FILE_PATH}")
            else:
                os.popen(f"xdg-open {HardsploitGUI.DB_FILE_PATH}")

    @Slot()
    def get_hardsploit_website(self):
        QMessageBox(
            QMessageBox.Information,
            'Hardsploit website',
            'Find all the news about Hardsploit on our website:\n http://hardsploit.io'
        ).exec_()

    @Slot()
    def open_signal_mapper(self):
        self.signal_mapper = SignalMapper()
        self.signal_mapper.setWindowModality(Qt.ApplicationModal)
        self.signal_mapper.show()

    def check_hardsploit_connection(self):
        if HardsploitUtils.get_number_of_board_available() > 0:
            self._api = HardsploitAPI()

            self.console.print(f"Hardsploit board detected GUI V{self.version_gui} "
                               f"API V{HardsploitConstant.VERSION.API}"
                               f" BOARD : {self._api.get_version_number()}")
            self.console.print(f'Hardsploit #{self._api.dev.address} ready to suck chip souls !')
            self.set_hs_board_status(True)
        else:
            self.console.print('Hardsploit board unconnected: '
                               'Wiring and command execution disabled')
            self.set_hs_board_status(False)
