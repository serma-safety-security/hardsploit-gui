"""chip_editor.py"""

from PySide6.QtCore import Slot, QObject, SIGNAL, SLOT, Qt
from PySide6.QtWidgets import QWidget, QComboBox, QTableWidgetItem, QMessageBox

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.utils import input_restrict, center_window
from hardsploit_gui.gui.gui_chip_editor import Ui_Chip_editor
from hardsploit_gui.db.models import *


class ChipEditor(QWidget):

    def __init__(self, parent, chip, action):
        # try:
        super().__init__()
        self.view = Ui_Chip_editor()
        center_window(self)
        self.view.setupUi(self)
        self.parent = parent
        self.chip = chip
        self.action = action
        self.manufacturer = None
        self.package = None
        self.chip_type = None
        self.voltage = None
        self.shape = None
        self.is_editing = False

        input_restrict(self.view.lie_pack_name, 2)
        input_restrict(self.view.lie_pack_pin, 0)
        input_restrict(self.view.lie_manu_name, 2)
        input_restrict(self.view.lie_type_name, 2)
        input_restrict(self.view.lie_reference, 2)
        input_restrict(self.view.lie_description, 2)

        # Combobox
        for p in Package.select():
            self.view.cbx_package.addItem(p.name)

        for m in Manufacturer.select():
            self.view.cbx_manufacturer.addItem(m.name)

        for c in ChipType.select():
            self.view.cbx_type.addItem(c.name)

        if action != 'new':
            package_name = chip.package.name
            manufacturer_name = chip.manufacturer.name
            chip_type_name = chip.chip_type.name
            self.view.cbx_package.setCurrentIndex(self.view.cbx_package.findText(package_name))
            self.view.lie_pack_name.setText(package_name)
            self.view.lie_pack_name.setEnabled(False)
            self.view.cbx_manufacturer.setCurrentIndex(self.view.cbx_manufacturer.findText(manufacturer_name))
            self.view.lie_manu_name.setText(manufacturer_name)
            self.view.lie_manu_name.setEnabled(False)
            self.view.cbx_type.setCurrentIndex(self.view.cbx_type.findText(chip_type_name))
            self.view.lie_type_name.setText(chip_type_name)
            self.view.lie_type_name.setEnabled(False)
            self.view.rbn_rectangular.setEnabled(False)
            self.view.rbn_square.setEnabled(False)
            if chip.voltage == 0:
                self.view.rbn_5v.setChecked(True)
            else:
                self.view.rbn_3v.setChecked(True)
            if chip.package.shape == 0:
                self.view.rbn_square.setChecked(True)
            else:
                self.view.rbn_rectangular.setChecked(True)

            if action == 'edit':
                self.view.lie_reference.setText(self.chip.reference)
            self.fill_pin_table('edit')
            self.view.lie_description.setText(self.chip.description)

        # Array struct
        self.view.tbl_pins.horizontalHeader().stretchLastSection = True
        self.view.tbl_pins.verticalHeader().setVisible(False)

        # Button text
        if action == 'edit':
            self.view.btn_add.setText('Edit')
            QObject.connect(self.view.btn_add, SIGNAL('clicked()'), self, SLOT('edit_chip()'))
        else:
            self.view.btn_add.setText('Add')
            QObject.connect(self.view.btn_add, SIGNAL('clicked()'), self, SLOT('add_chip()'))


    def close_event(self, event):
        if self.chip == "none" or Chip.select().where(Chip.id == self.chip.id).exists():
            self.parent.view.tw_chip.clear()

    def prepare_rq(self):
        lie_reference = self.view.lie_reference.text() if self.view.lie_reference.text() else None
        manufacturer_name = self.view.lie_manu_name.text() if self.view.lie_manu_name.text() else None
        package_name = self.view.lie_pack_name.text() if self.view.lie_pack_name.text() else None
        chip_type = self.view.lie_type_name.text()if self.view.lie_type_name.text() else None
        lie_pack_pin = self.view.lie_pack_pin.text() if self.view.lie_pack_pin.text() else None
        if lie_reference:
            if not Chip.select().where(Chip.reference.contains(lie_reference)).exists() or self.is_editing:
                if manufacturer_name and package_name and chip_type and lie_pack_pin:
                    # Manufacturer
                    self.manufacturer, created = Manufacturer.get_or_create(name=manufacturer_name)
                    # Package
                    if self.view.rbn_square.isChecked():
                        self.shape = 0
                    else:
                        self.shape = 1
                    self.package, created = Package.get_or_create(
                        name=package_name,
                        pin_number=lie_pack_pin,
                        shape=self.shape
                    )
                    # Type
                    self.chip_type, created = ChipType.get_or_create(name=chip_type)
                    # Voltage
                    if self.view.rbn_3v.isChecked():
                        self.voltage = 1
                    else:
                        self.voltage = 0
                    return True
                else:
                    if manufacturer_name is None:
                        ErrorMsg.custom("Value Missing", "Manufacturer missing")
                    elif package_name is None:
                        ErrorMsg.custom("Value Missing", "Package missing")
                    elif chip_type is None:
                        ErrorMsg.custom("Value Missing", "Chip type missing")
                    elif lie_pack_pin is None:
                        ErrorMsg.custom("Value Missing", "Package pin number missing")
                    return False
            ErrorMsg.custom("Error", "This reference already exist")
            return False
        else:
            ErrorMsg.custom("Value Missing", "Reference missing")
            return False

    @Slot()
    def add_chip(self):
        if self.prepare_rq():
            self.chip = Chip.create(
                reference=self.view.lie_reference.text(),
                description=self.view.lie_description.text(),
                voltage=self.voltage,
                manufacturer_id=self.manufacturer.id,
                package_id=self.package.id,
                chip_type_id=self.chip_type.id
            )
            self.chip.save()
            self.add_pins()

    @Slot()
    def edit_chip(self):
        self.is_editing = True
        if self.prepare_rq():
            self.chip.reference = self.view.lie_reference.text()
            self.chip.description = self.view.lie_description.text()
            self.chip.voltage = self.voltage
            self.chip.manufacturer_id = self.manufacturer.id
            self.chip.package_id = self.package.id
            self.chip.chip_type_id = self.chip_type.id
            self.chip.save()
            Pin.delete().where(Pin.chip == self.chip).execute()
            self.add_pins()


    def add_pins(self):
        for i in range(int(self.view.lie_pack_pin.text())):
            pin_num = self.view.tbl_pins.item(i, 0)
            pin_signal = self.view.tbl_pins.cellWidget(i, 2)
            pin_bus = self.view.tbl_pins.cellWidget(i, 1)
            signal = 1
            if pin_bus.currentIndex() != 0 and True:
                signal = Signal.get(Signal.name == pin_signal.currentText())
            pin = Pin.create(
                number=int(pin_num.text()),
                chip_id=self.chip.id,
                signal_id=signal
              )
            pin.save()
        self.parent.feed_chip_array()
        self.close()

    @Slot()
    def select_package(self):
        if self.view.cbx_package.currentIndex() != 0:
            selected_package = Package.get(Package.name == self.view.cbx_package.currentText())
            self.view.lie_pack_name.setEnabled(False)
            self.view.lie_pack_name.setText(selected_package.name)
            self.view.lie_pack_pin.setEnabled(False)
            self.view.lie_pack_pin.setText(str(selected_package.pin_number))
            self.view.rbn_square.setEnabled(False)
            self.view.rbn_rectangular.setEnabled(False)
            if selected_package.shape == 0:
                self.view.rbn_square.setChecked(True)
            else:
                self.view.rbn_rectangular.setChecked(True)
            self.fill_pin_table()
        else:
            self.view.lie_pack_name.setEnabled(True)
            self.view.lie_pack_name.clear()
            self.view.lie_pack_pin.setEnabled(True)
            self.view.lie_pack_pin.clear()
            self.view.rbn_square.setChecked(True)
            self.view.rbn_rectangular.setEnabled(True)
            self.view.rbn_square.setEnabled(True)
            self.view.tbl_pins.clear()
            self.view.tbl_pins.setRowCount(0)

    @Slot()
    def select_manufacturer(self):
        if self.view.cbx_manufacturer.currentIndex() != 0:
            self.view.lie_manu_name.setEnabled(False)
            self.view.lie_manu_name.setText(self.view.cbx_manufacturer.currentText())
        else:
            self.view.lie_manu_name.setEnabled(True)
            self.view.lie_manu_name.setText('')

    @Slot()
    def select_type(self):
        if self.view.cbx_type.currentIndex() != 0:
            self.view.lie_type_name.setEnabled(False)
            self.view.lie_type_name.setText(self.view.cbx_type.currentText())
        else:
            self.view.lie_type_name.setEnabled(True)
            self.view.lie_type_name.setText('')

    @Slot()
    def fill_pin_table(self, action=''):
        try:
            if 144 >= int(self.view.lie_pack_pin.text()) >= 4:
                self.view.tbl_pins.setRowCount(int(self.view.lie_pack_pin.text()))
                full_bus_list = Bus.select()
                for i in range(int(self.view.lie_pack_pin.text())):
                    cbx_bus = QComboBox()
                    cbx_bus.setProperty('row', str(i))
                    self.view.tbl_pins.setCellWidget(i, 1, cbx_bus)
                    cbx_signal = QComboBox()
                    self.view.tbl_pins.setCellWidget(i, 2, cbx_signal)
                    item = QTableWidgetItem()
                    item.setFlags(Qt.ItemIsEnabled)
                    item.setData(0, str(i + 1))
                    self.view.tbl_pins.setItem(i, 0, item)
                    cbx_bus.addItem('Bus...')
                    for b in full_bus_list:
                        cbx_bus.addItem(b.name)
                    if action == 'edit':
                        pin = Pin.select().where((Pin.number == i + 1) & (Pin.chip_id == self.chip.id)).first()
                        if pin.signal_id != 1:
                            current_bus = Bus.select().join(Use, JOIN.LEFT_OUTER).where(
                                Use.signal_id == pin.signal_id).first()
                            cbx_bus.setCurrentIndex(cbx_bus.findText(current_bus.name))
                            for s in Use.select().where(Use.bus == current_bus):
                                cbx_signal.addItem(s.signal.name)
                            cbx_signal.setCurrentIndex(cbx_signal.findText(pin.signal.name))
                    QObject.connect(cbx_bus, SIGNAL('currentIndexChanged(int)'), self, SLOT('filter_cbx()'))
            else:
                self.view.lie_pack_pin.clear()
                raise ValueError
        except ValueError:
            ErrorMsg.invalid_pin_nbr()
        except Exception as e:
            ErrorMsg.unknown(e)

    @Slot()
    def delete_cbx_element(self):
        msg = QMessageBox()
        msg.setWindowTitle('Delete element')
        msg.setText('Chips and commands associated with it will be deleted too.')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        if msg.exec_() == QMessageBox.Ok:
            if self.sender().objectName() == 'btn_delete_package':
                if self.view.cbx_package.currentIndex() == 0:
                    return False
                Package.delete().where(Package.name == self.view.cbx_package.currentText()).execute()
                self.view.cbx_package.removeItem(self.view.cbx_package.currentIndex())
                self.view.cbx_package.setCurrentIndex(0)
            elif self.sender().objectName() == 'btn_delete_manufacturer':
                if self.view.cbx_manufacturer.currentIndex() == 0:
                    return False
                Manufacturer.delete().where(Manufacturer.name == self.view.cbx_manufacturer.currentText()).execute()
                self.view.cbx_manufacturer.removeItem(self.view.cbx_manufacturer.currentIndex())
                self.view.cbx_manufacturer.setCurrentIndex(0)
            elif self.sender().objectName() == 'btn_delete_type':
                if self.view.cbx_type.currentIndex() == 0:
                    return False
                ChipType.delete().where(ChipType.name == self.view.cbx_type.currentText()).execute()
                self.view.cbx_type.removeItem(self.view.cbx_type.currentIndex())
                self.view.cbx_type.setCurrentIndex(0)
            self.parent.feed_chip_array()

    @Slot()
    def filter_cbx(self):
        bus_item_row = int(self.sender().property('row'))
        bus_item = self.view.tbl_pins.cellWidget(bus_item_row, 1)
        associated_signal_item = self.view.tbl_pins.cellWidget(bus_item_row, 2)
        associated_signal_item.clear()
        if bus_item.currentText() != 'Bus...':
            bus = Bus.get(Bus.name == bus_item.currentText()).id
            filtered_signal_list = Use.select().where(Use.bus_id == bus).execute()
            for s in filtered_signal_list:
                signal_name = Signal.get(s.signal_id).name
                associated_signal_item.addItem(signal_name)
