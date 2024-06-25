"""chip_management.py"""

import os
import platform

import usb
from PySide6.QtCore import Slot, Qt, QTimer
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QLabel, QMessageBox, QApplication
from hardsploit_gui.classes.export import Exportdata
from hardsploit_gui.classes.import_datas import Importdata

from hardsploit.core import HardsploitConstant, HardsploitUtils

from hardsploit_gui.gui.gui_chip_management import Ui_Chip_management
from .firmware import Firmware

from .signal_mapper import SignalMapper
from .tab_management import TabManagement
from .chip_editor import ChipEditor
from .utils import center_window



class ChipManagement(QMainWindow):

    def __init__(self, version_gui):
        super().__init__()
        self.view = Ui_Chip_management()
        self.view.setupUi(self)
        self.tabs = self.view.tabWidget
        self.versionGUI = version_gui
        self.display_tabs()
        self.hardsploit_board_status = QLabel()
        self.statusBar().addWidget(self.hardsploit_board_status)
        self.a_chip = None
        self.signal_mapper = None
        self.import_data = None
        self.export_data = None
        self.center_window()

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

    def set_hs_board_status(self, connected):
        if connected:
            self.hardsploit_board_status.setText("Hardsploit board: connected " +
                                                 f"- version {self.tabs.currentWidget()._api.get_version_number()} " +
                                                 f"- api V{HardsploitConstant.VERSION.API}")
        else:
            self.hardsploit_board_status.setText("Hardsploit board: disconnected")


    @Slot()
    def add_chip(self):
        self.a_chip = ChipEditor(self, 'none', 'new')
        self.a_chip.show()


    @Slot()
    def import2(self):
        self.import_data = Importdata()
        self.import_data.show()
        pass

    @Slot()
    def export(self):
        self.export_data = Exportdata()
        self.export_data.show()
        pass

    @Slot()
    def display_current_firmware(self):
        from hardsploit_gui.main import HardsploitGUI
        if not HardsploitGUI.currentFirmware:
            QMessageBox(QMessageBox.Information, 'Firmware', 'No firmware loaded').exec_()
        else:
            QMessageBox(QMessageBox.Information, 'Firmware', f"Actual firmware: {HardsploitGUI.currentFirmware}").exec_()

    @Slot()
    def set_firmware(self):
        Firmware(self.sender().objectName()[6:len(self.sender().objectName())], self.tabs.currentWidget()._api)
        self.display_current_firmware()

    @Slot()
    def update_uc_firmware(self):
        Firmware('uC', self.tabs.currentWidget()._api)

    @Slot()
    def get_hardsploit_versions(self):
        if HardsploitUtils.get_number_of_board_available() > 0:
            QMessageBox(QMessageBox.Information, 'Hardsploit versions',
                        f"GUI VERSION : {self.versionGUI}\n" +
                        f"API VERSION : {HardsploitConstant.VERSION.API}\n" +
                        f"BOARD : {self.tabs.currentWidget()._api.get_version_number()}"
                        ).exec_()
        else:
            QMessageBox(QMessageBox.Information, 'Hardsploit versions',
                        f"GUI VERSION : {self.versionGUI}\n" +
                        f"API VERSION : {HardsploitConstant.VERSION.API}\n").exec_()

    @Slot()
    def get_log_path(self):
        from hardsploit_gui.main import HardsploitGUI
        msg = QMessageBox()
        msg.setWindowTitle('Log file path')
        msg.setText(f"Path: {HardsploitGUI.LOG_FILE_PATH}")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
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
        from hardsploit_gui.main import HardsploitGUI
        msg = QMessageBox()
        msg.setWindowTitle('Database path')
        msg.setText(f"Path: {HardsploitGUI.DB_FILE_PATH}\n")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        open_btn = msg.addButton('Open file', QMessageBox.ActionRole)
        open_btn.setObjectName('open_btn')
        backup_btn = msg.addButton('Create backup', QMessageBox.ActionRole)
        backup_btn.setObjectName('backup_btn')
        msg.exec_()
        if msg.clickedButton().objectName() == 'backup_btn':
            os.popen(f"cp {HardsploitGUI.DB_FILE_PATH} {HardsploitGUI.DB_FILE_PATH}.bck")
            QMessageBox(QMessageBox.Information, 'Backup status', f'{HardsploitGUI.DB_FILE_PATH}.bck created').exec_()

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

    def display_tabs(self):
        # Remove the 2 auto generated default Tab
        self.tabs.removeTab(0)
        self.tabs.removeTab(0)
        devices = list(usb.core.find(idVendor=0x0483, idProduct=0xFFFF, find_all=True))
        if len(devices) == 0:
            self.tabs.addTab(TabManagement(self.versionGUI), "No Board connected")
        else:
            for device in devices:
                self.tabs.addTab(TabManagement(self.versionGUI), f"Hardsploit #{device.address}")
