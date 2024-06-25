"""signal_mapper.py"""

from PySide6.QtCore import QRegularExpression, Slot, Qt
from PySide6.QtGui import QRegularExpressionValidator, QValidator
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.db.models import *
from hardsploit_gui.gui.gui_signal_mapper import Ui_Signal_mapper


class SignalMapper(QWidget):

    def __init__(self):
        super().__init__()
        self.view = Ui_Signal_mapper()
        center_window(self)
        self.view.setupUi(self)
        self.init_bus_list()


    def init_bus_list(self):
        for b in Bus.select():
            if b.name != "NA":
                self.view.cbx_bus.addItem(b.name)

    @Slot(QTableWidgetItem)
    def check_mapping_value(self, item):
        if item.column() == 1:
            item.setText(item.text().upper())
            reg = QRegularExpression("^[A-H]{1}[0-7]{1}$")
            reg_val = QRegularExpressionValidator(reg)
            if reg_val.validate(item.text(), len(item.text()))[0] == QValidator.Invalid and item.text():
                item.setText('')
                QMessageBox(QMessageBox.Warning, 'Wrong data', 'Only values from A0 to H7 are accepted in this cell').exec_()


    @Slot()
    def update_map_table(self, bus_name):
        if bus_name != 'Bus...':
            self.view.map_table.clearContents()
            self.view.map_table.setRowCount(0)
            for s in Use.select().where(Use.bus == bus_name+1):
                s = s.signal
                self.view.map_table.insertRow(self.view.map_table.rowCount())
                signal_cell = QTableWidgetItem(s.name)
                signal_cell.setFlags(Qt.ItemIsEnabled)
                self.view.map_table.setItem(self.view.map_table.rowCount() - 1, 0, signal_cell)
                pin_cell = QTableWidgetItem(s.pin)
                self.view.map_table.setItem(self.view.map_table.rowCount() - 1, 1, pin_cell)
            self.resize_to_content()

    @Slot()
    def save_signal_mapping(self):
        if not self.are_values_ok():
            return 0
        for i in range(self.view.map_table.rowCount()):
            current_signal = Signal.get(Signal.name == self.view.map_table.item(i, 0).text())
            if current_signal.name != self.view.map_table.item(i, 1).text():
                current_signal.pin = self.view.map_table.item(i, 1).text()
                current_signal.save()
        QMessageBox(QMessageBox.Information, 'Save mapping', 'Pin mapping saved successfully').exec_()
        self.close()

    def are_values_ok(self):
        pins = []
        for i in range(self.view.map_table.rowCount()):
            pins.append(self.view.map_table.item(i, 1).text())
        if self.check_empty(pins) and self.check_duplicate(pins):
            return True

    def check_empty(self, pins):
        if '' not in pins:
            return True
        self.view.map_table.setCurrentItem(self.view.map_table.item(pins.index(''), 1))
        QMessageBox(QMessageBox.Warning, 'Empty pin', 'Empty pin value detected').exec_()
        return False
    
    def check_duplicate(self, pins):
        for pin in pins:
            if pins.count(pin) > 1:
                self.view.map_table.setCurrentItem(self.view.map_table.item(pins.index(pin), 1))
                QMessageBox(QMessageBox.Warning, 'Wrong value', f"Duplicate values detected: {pin}").exec_()
                return False
        return True
    
    def resize_to_content(self):
        self.view.map_table.resizeColumnsToContents()
        self.view.map_table.resizeRowsToContents()
        self.view.map_table.horizontalHeader().setStretchLastSection(True)
