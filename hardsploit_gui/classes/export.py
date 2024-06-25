import json

from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.db.models import *
from hardsploit_gui.gui.gui_export import Ui_Export
from PySide6.QtWidgets import QWidget,  QFileDialog, QMessageBox
from PySide6.QtCore import Slot, Qt


class Exportdata(QWidget):

    def __init__(self, chip_list=None):
        super().__init__()
        self.export_ui = Ui_Export()
        self.export_ui.setupUi(self)
        if chip_list is None:
            self.chip_list = Chip.select()
            self.commands = Command.select()
        else:
            self.chip_list = Chip.select().where(Chip.id == chip_list)
            self.select_file()
            self.export_data(chip_list.reference)
        self.file_path = None
        self.file = None
        self.chip = None

    @Slot()
    def select_file(self):
        self.file_path = QFileDialog.getSaveFileName(self, 'Select a file', '/')[0]
        return None

    @Slot()
    def export_data(self, chip_reference=None):
        if self.file_path is not None:
            with open(f"{self.file_path}.json", 'w') as self.file:
                self.file.write("{\n")
                self.file.write('"chips":{\n')
                for index, self.chip in enumerate(self.chip_list):
                    if index + 1 < len(self.chip_list):
                        self.export_chip()
                    else:
                        self.export_chip()
                    if index + 1 < len(self.chip_list):
                        self.file.write("\t},\n")
                    else:
                        self.file.write("\t}\n")
                self.file.write("},\n")
                self.export_commands(self.file, chip_reference)
                self.file.write("}")
            QMessageBox.information(None, 'Export status', 'Export finished')
        else:
            QMessageBox.warning(None, 'File missing', 'Choose a file before exporting')

    def export_chip(self):
        self.write_commons()
        self.write_settings()
        self.write_pins()

    def write_commons(self):
        self.file.write(f'\t"{self.chip.reference}": {{\n')
        self.file.write(f'\t\t\"description\": "{self.chip.description}",\n')
        self.file.write(f"\t\t\"voltage\": {self.chip.voltage},\n")
        manufacturer = Manufacturer.select().where(Manufacturer.id == self.chip.manufacturer).get()
        self.file.write(f'\t\t"manufacturer": "{manufacturer}",\n')
        chip_type = ChipType.select().where(ChipType.id == self.chip.chip_type).get()
        self.file.write(f"\t\t\"chip_type\": {chip_type},\n")
        package = Package.select().where(Package.id == self.chip.package).get()
        self.file.write(f"\t\t\"package\": {package},\n")

    def write_settings(self):
        self.file.write("\t\t\"settings\":{\n")
        if SpiSetting.select().where(SpiSetting.chip_id == self.chip.id).exists():
            json_data = self.convert_to_json(SpiSetting.select().where(SpiSetting.chip_id == self.chip.id).get())
            self.file.write(f"\t\t\t\"spi\": {json_data},\n")
        else:
            self.file.write("\t\t\t\"spi\": {},\n")

        if I2cSetting.select().where(I2cSetting.chip_id == self.chip.id).exists():
            json_data = self.convert_to_json(I2cSetting.select().where(I2cSetting.chip_id == self.chip.id).get())
            self.file.write(f"\t\t\t\"i2c\": {json_data},\n")
        else:
            self.file.write("\t\t\t\"i2c\": {},\n")

        if SwdSetting.select().where(SwdSetting.chip_id == self.chip.id).exists():
            json_data = self.convert_to_json(SwdSetting.select().where(SwdSetting.chip_id == self.chip.id).get())
            self.file.write(f"\t\t\t\"swd\": {json_data},\n")
        else:
            self.file.write("\t\t\t\"swd\": {},\n")

        if UartSetting.select().where(UartSetting.chip_id == self.chip.id).exists():
            json_data = self.convert_to_json(UartSetting.select().where(UartSetting.chip_id == self.chip.id).get())
            self.file.write(f"\t\t\t\"uart\": {json_data}\n")
        else:
            self.file.write("\t\t\t\"uart\": {}\n")
        self.file.write("\t\t},\n")

    def write_pins(self):
        self.file.write("\t\t\"pins\":[\n")
        pins = list(Pin.select().where(Pin.chip_id == self.chip.id))
        if pins:
            for index, pin in enumerate(pins):
                pin = self.convert_to_json(pin)
                if index + 1 < len(pins):
                    self.file.write(f"\t\t\t{pin},\n")
                else:
                    self.file.write(f"\t\t\t{pin}\n")
        self.file.write("\t\t]\n")

    def export_commands(self, file, chip_reference):
        if chip_reference is None:
            commands = list(Command.select())
        else:
            chip_id = Chip.select().where(Chip.reference == chip_reference).get().id
            commands = list(Command.select().where(Command.chip_id == chip_id))
        file.write('"commands": {\n')
        if commands:
            for index, command in enumerate(commands):
                chip = Chip.select().where(Chip.id == command.chip_id).get()
                chip_ref = chip.reference
                file.write(f'\t"{command.name}": {{\n')
                self.file.write(f'\t\t"id": "{command.id}",\n')
                self.file.write(f'\t\t"description": "{command.description}",\n')
                self.file.write(f'\t\t"chip_ref": "{chip_ref}",\n')
                self.file.write(f'\t\t"bus_id": "{command.bus_id}",\n')
                self.write_bytes(command.id)
                if index+1 >= len(commands):
                    file.write('\t}\n')
                else:
                    file.write('\t},\n')
        file.write('}\n')


    def write_bytes(self, cmd_id):
        self.file.write("\t\t\"bytes\":[\n")
        bytes = list(Byte.select().where(Byte.command_id == cmd_id))
        if bytes:
            for index, byte in enumerate(bytes):
                byte = self.convert_to_json(byte)
                if index + 1 >= len(bytes):
                    self.file.write(f"\t\t\t\t{byte}\n")
                else:
                    self.file.write(f"\t\t\t\t{byte},\n")
            self.file.write("\t\t\t]\n")
        pass

    @staticmethod
    def convert_to_json(datas):
        dic = datas.__dict__
        clear_dic = dic.pop('__data__')
        json_data = json.dumps(clear_dic)
        return json_data
