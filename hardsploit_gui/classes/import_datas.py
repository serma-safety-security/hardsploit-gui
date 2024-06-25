
import json
import sqlite3
import os
from PySide6.QtCore import Slot, Qt
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.db.models import *
from hardsploit_gui.gui.gui_import import Ui_Import
from PySide6.QtWidgets import QWidget,  QFileDialog, QMessageBox


class Importdata(QWidget):

    def __init__(self):
        super().__init__()
        self.import_ui = Ui_Import()
        self.import_ui.setupUi(self)
        self.file_path = None
        self.file = None
        self.chip = None
        self.old_new_chip_id = None
        self.old_and_new_chip_id = {}
        self.old_and_new_bus_id = {}
        self.old_and_new_chip_type_id = {}
        self.old_and_new_command_id = {}
        self.old_and_new_manufacturer_id = {}
        self.old_and_new_package_id = {}
        self.old_and_new_signal_id = {}

    @Slot()
    def import_data(self):
        import_done = False
        if self.file_path is not None:
            file_extension = os.path.splitext(self.file_path)[1]
            if file_extension == '.json':
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    if self.import_ui.rbn_comp.isChecked():
                        import_done = self.import_chip(data['chips'])
                    elif self.import_ui.rbn_cmds.isChecked():
                        import_done = self.import_commands(data["commands"])
                    else:
                        self.import_chip(data['chips'])
                        import_done = self.import_commands(data["commands"])
            elif file_extension == '.sqlite3':
                import_done = self.import_from_ruby_db()
            if import_done:
                QMessageBox.information(None, 'Import status', 'Import finished')
            self.close()
        else:
            QMessageBox.warning(None, 'File missing', 'Choose a file before importing')
        pass

    @Slot()
    def select_file(self):
        self.old_new_chip_id = {}
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(
            None,
            'Select a file',
            '/',
            'JSON or Database files (*.json *.sqlite3)',
            options=options
        )

    def import_chip(self, chips):
        for chip_ref, chip_info in chips.items():
            try:
                if Chip.select().where(Chip.reference == chip_ref).exists():
                    pass
                else:
                    chip_id = self.add_chip_to_db(chip_ref, chip_info)
                    for pin in chip_info["pins"]:
                        self.add_pin_to_db(pin, chip_id)
                    for setting_name in chip_info["settings"]:
                        setting = chip_info["settings"][setting_name]
                        if self.add_setting_to_db(setting_name, setting, chip_ref, chip_id):
                            break
            except Exception as e:
                ErrorMsg.custom("Import error", f"An error occurred while importing chip {chip_ref}")
                return False
        return True

    def import_commands(self, commands):
        for command_info in commands.items():
            try:
                chip_id = Chip.select().where(Chip.reference == command_info[1]["chip_ref"]).get().id
                if not Command.select().where((Command.name == command_info[0]) & (Command.chip_id == chip_id)).exists():
                    command = Command(
                        name=command_info[0],
                        description=command_info[1]["description"],
                        chip_id=chip_id,
                        bus_id=command_info[1]["bus_id"]
                    )
                    command.save()
                command_id = Command.select().where((Command.name == command_info[0]) & (Command.chip_id == chip_id)).get()
                self.import_bytes(command_info[1]['bytes'], command_id)
            except Exception as e:
                ErrorMsg.custom("Import error", f"An error occurred while importing commands")
                return False
        return True

    @staticmethod
    def import_bytes(bytes, command_id):
        for byte_info in bytes:
            if not Byte.select().where((Byte.command_id == command_id) & (Byte.description == byte_info["description"])).exists():
                byte = Byte(
                    position=byte_info["position"],
                    value=byte_info["value"],
                    description=byte_info["description"],
                    iteration=byte_info["iteration"],
                    command_id=command_id
                )
                byte.save()

    @staticmethod
    def add_chip_to_db(chip_ref, chip_info):
        chip = Chip(
            reference=chip_ref,
            description=chip_info['description'],
            voltage=chip_info['voltage'],
            manufacturer=chip_info['manufacturer'],
            chip_type=chip_info['chip_type'],
            package=chip_info['package'],
        )
        chip.save()
        chip = Chip.get(Chip.reference == chip_ref)
        chip_id = chip.id
        return chip_id

    @staticmethod
    def add_pin_to_db(pin_info, chip_id):
        pin = Pin(
            number=pin_info["number"],
            chip=chip_id,
            signal=pin_info["signal"]
        )
        pin.save()

    @staticmethod
    def add_setting_to_db(setting_name, setting_info, chip_ref, chip_id):
        setting = None
        if setting_info != {}:
            if setting_name == "spi":
                setting = SpiSetting(
                    mode=setting_info["mode"],
                    frequency=setting_info["frequency"],
                    write_page_latency=setting_info["write_page_latency"],
                    command_read=setting_info["command_read"],
                    command_write=setting_info["command_write"],
                    command_write_enable=setting_info["command_write_enable"],
                    command_erase=setting_info["command_erase"],
                    erase_time=setting_info["erase_time"],
                    page_size=setting_info["page_size"],
                    total_size=setting_info["total_size"],
                    is_flash=setting_info["is_flash"],
                    chip=chip_id
                )
            elif setting_name == "i2c":
                setting = I2cSetting(
                    address_w=setting_info["address_w"],
                    address_r=setting_info["address_r"],
                    frequency=setting_info["frequency"],
                    write_page_latency=setting_info["write_page_latency"],
                    page_size=setting_info["page_size"],
                    total_size=setting_info["total_size"],
                    chip=chip_id
                )
            elif setting_name == "swd":
                setting = SwdSetting(
                    cpu_id_address=setting_info["cpu_id_address"],
                    device_id_address=setting_info["device_id_address"],
                    memory_size_address=setting_info["memory_size_address"],
                    memory_start_address=setting_info["memory_start_address"],
                    chip=chip_id
                )
            elif setting_name == "uart":
                setting = UartSetting(
                    baud_rate=setting_info["baud_rate"],
                    idle_line=setting_info["idle_line"],
                    word_size=setting_info["word_size"],
                    parity_bit=setting_info["parity_bit"],
                    parity_type=setting_info["parity_type"],
                    stop_bits_nbr=setting_info["stop_bits_nbr"],
                    return_type=setting_info["return_type"],
                    chip=chip_id
                )
            if setting is None:
                ErrorMsg.custom("Error", f"An error occurred while importing commands for chip: {chip_ref}")
                return True
            else:
                setting.save()
        return False

    def import_from_ruby_db(self):
        try:
            con = sqlite3.connect(self.file_path)
            cur = con.cursor()
            chip_types = cur.execute("SELECT * FROM chip_types").fetchall()
            self.import_chip_types_from_db(chip_types)
            manufacturers = cur.execute("SELECT * FROM manufacturers").fetchall()
            self.import_manufacturers_from_db(manufacturers)
            packages = cur.execute("SELECT * FROM packages").fetchall()
            self.import_packages_from_db(packages)
            chips = cur.execute("SELECT * FROM chips").fetchall()
            self.import_chips_from_db(chips)
            commands = cur.execute("SELECT * FROM commands").fetchall()
            self.import_commands_from_db(commands)
            bytes = cur.execute("SELECT * FROM bytes").fetchall()
            self.import_bytes_from_db(bytes)
            i2c_settings = cur.execute("SELECT * FROM i2c_settings").fetchall()
            self.import_i2c_settings_from_db(i2c_settings)
            parallel_settings = cur.execute("SELECT * FROM parallel_settings").fetchall()
            self.import_parallel_settings_from_db(parallel_settings)
            spi_settings = cur.execute("SELECT * FROM spi_settings").fetchall()
            self.import_spi_settings_from_db(spi_settings)
            swd_settings = cur.execute("SELECT * FROM swd_settings").fetchall()
            self.import_swd_settings_from_db(swd_settings)
            uart_settings = cur.execute("SELECT * FROM uart_settings").fetchall()
            self.import_uart_settings_from_db(uart_settings)
            pins = cur.execute("SELECT * FROM pins").fetchall()
            self.import_pins_from_db(pins)
            return True
        except sqlite3.OperationalError as e:
            if "no such table" in str(e):
                ErrorMsg.custom('Database error', f"An error occurred while trying to import: {self.file_path}")

    def import_chip_types_from_db(self, chip_types):
        for chip_type_info in chip_types:
            old_id = chip_type_info[0]
            if not ChipType.select().where(ChipType.name == chip_type_info[1]).exists():
                chip_type = ChipType(
                    name=chip_type_info[1]
                )
                chip_type.save()
            new_id = ChipType.select().where(ChipType.name == chip_type_info[1]).get().id
            self.old_and_new_chip_type_id[old_id] = new_id

    def import_chips_from_db(self, chips):
        for chip_info in chips:
            old_id = chip_info[0]
            if not Chip.select().where(Chip.reference == chip_info[1]).exists():
                try:
                    chip_type_id = self.old_and_new_chip_type_id[chip_info[6]]
                except:
                    chip_type_id = chip_info[5]
                chip = Chip(
                    reference=chip_info[1],
                    description=chip_info[2],
                    voltage=chip_info[3],
                    manufacturer_id=chip_info[4],
                    package_id=chip_info[5],
                    chip_type_id=chip_type_id
                )
                chip.save()
            new_id = Chip.select().where(Chip.reference == chip_info[1]).get().id
            self.old_and_new_chip_id[old_id] = new_id

    def import_bytes_from_db(self, bytes):
        for byte_info in bytes:
            if not Byte.select().where((Byte.position == byte_info[1]) & (Byte.value == byte_info[2]) & (
                    Byte.command_id == byte_info[5])).exists():
                try:
                    command_id = self.old_and_new_command_id[byte_info[5]]
                except:
                    command_id = byte_info[6]
                byte = Byte(
                    position=byte_info[1],
                    value=byte_info[2],
                    description=byte_info[3],
                    iteration=byte_info[4],
                    command_id=command_id
                )
                byte.save()

    def import_commands_from_db(self, commands):
        for command_info in commands:
            old_id = command_info[0]
            if not Command.select().where(Command.name == command_info[1]).exists():
                try:
                    chip_id = self.old_and_new_chip_id[command_info[4]]
                except:
                    chip_id = command_info[4]
                try:
                    bus_id = self.old_and_new_bus_id[command_info[3]]
                except:
                    bus_id = command_info[3]
                command = Command(
                    name=command_info[1],
                    description=command_info[2],
                    chip_id=chip_id,
                    bus_id=bus_id
                )
                command.save()
            new_id = Command.select().where(Command.name == command_info[1]).get().id
            self.old_and_new_command_id[old_id] = new_id

    def import_i2c_settings_from_db(self, i2c_settings):
        for i2c_setting_info in i2c_settings:
            try:
                chip_id = self.old_and_new_chip_id[i2c_setting_info[7]]
            except:
                chip_id = i2c_setting_info[7]
            if not I2cSetting.select().where(I2cSetting.chip_id == chip_id).exists():
                i2csetting = I2cSetting(
                    address_w=i2c_setting_info[1],
                    address_r=i2c_setting_info[2],
                    frequency=i2c_setting_info[3],
                    write_page_latency=i2c_setting_info[4],
                    page_size=i2c_setting_info[5],
                    total_size=i2c_setting_info[6],
                    chip_id=chip_id
                )
                i2csetting.save()

    def import_manufacturers_from_db(self, manufacturers):
        for manufacturer_info in manufacturers:
            old_id = manufacturer_info[0]
            if not Manufacturer.select().where(Manufacturer.name == manufacturer_info[1]).exists():
                manufacturer = Manufacturer(
                    name=manufacturer_info[1]
                )
                manufacturer.save()
            new_id = Manufacturer.select().where(Manufacturer.name == manufacturer_info[1]).get().id
            self.old_and_new_manufacturer_id[old_id] = new_id

    def import_packages_from_db(self, packages):
        for package_info in packages:
            old_id = package_info[0]
            if not Package.select().where(Package.name == package_info[1]).exists():
                package = Package(
                    name=package_info[1],
                    pin_number=package_info[2],
                    shape=package_info[3]
                )
                package.save()
            new_id = Package.select().where(Package.name == package_info[1]).get().id
            self.old_and_new_package_id[old_id] = new_id

    def import_parallel_settings_from_db(self, parallel_settings):
        for parallel_setting_info in parallel_settings:
            try:
                chip_id = self.old_and_new_chip_id[parallel_setting_info[6]]
            except:
                chip_id = parallel_setting_info[6]
            if not ParallelSetting.select().where(ParallelSetting.chip_id == chip_id).exists():
                parallel_setting = ParallelSetting(
                    id=parallel_setting_info[1],
                    total_size=parallel_setting_info[2],
                    page_size=parallel_setting_info[3],
                    read_latency=parallel_setting_info[4],
                    write_latency=parallel_setting_info[5],
                    chip_id=chip_id
                )
                parallel_setting.save()

    def import_pins_from_db(self, pins):
        for pin_info in pins:
            if pin_info[2] in self.old_and_new_chip_id:
                try:
                    chip_id = self.old_and_new_chip_id[pin_info[2]]
                except:
                    chip_id = pin_info[2]
                try:
                    signal_id = self.old_and_new_signal_id[pin_info[3]]
                except:
                    signal_id = pin_info[3]
                if not Pin.select().where((Pin.number == pin_info[1]) & (Pin.chip_id == chip_id) & (
                        Pin.signal_id == signal_id)).exists():
                    pin = Pin(
                        number=pin_info[1],
                        chip_id=chip_id,
                        signal_id=signal_id
                    )
                    pin.save()

    def import_spi_settings_from_db(self, spi_settings):
        for spi_setting_info in spi_settings:
            try:
                chip_id = self.old_and_new_chip_id[spi_setting_info[12]]
            except:
                chip_id = spi_setting_info[12]
            if not SpiSetting.select().where(SpiSetting.chip_id == chip_id).exists():
                spi_setting = SpiSetting(
                    mode=spi_setting_info[1],
                    frequency=spi_setting_info[2],
                    write_page_latency=spi_setting_info[3],
                    command_read=spi_setting_info[4],
                    command_write=spi_setting_info[5],
                    command_write_enable=spi_setting_info[6],
                    command_erase=spi_setting_info[7],
                    erase_time=spi_setting_info[8],
                    page_size=spi_setting_info[9],
                    total_size=spi_setting_info[10],
                    is_flash=spi_setting_info[11],
                    chip_id=chip_id
                )
                spi_setting.save()

    def import_swd_settings_from_db(self, swd_settings):
        for swd_setting_info in swd_settings:
            try:
                chip_id = self.old_and_new_chip_id[swd_setting_info[5]]
            except:
                chip_id = swd_setting_info[5]
            if not SwdSetting.select().where(SwdSetting.chip_id == chip_id).exists():
                swd_setting_info = SwdSetting(
                    cpu_id_address=swd_setting_info[1],
                    device_id_address=swd_setting_info[2],
                    memory_size_address=swd_setting_info[3],
                    memory_start_address=swd_setting_info[4],
                    chip_id=chip_id
                )
                swd_setting_info.save()

    def import_uart_settings_from_db(self, uart_settings):
        for uart_setting_info in uart_settings:
            try:
                chip_id = self.old_and_new_chip_id[uart_setting_info[8]]
            except:
                chip_id = uart_setting_info[8]
            if not UartSetting.select().where(UartSetting.chip_id == chip_id).exists():
                uart_setting = UartSetting(
                    baud_rate=uart_setting_info[1],
                    idle_line=uart_setting_info[2],
                    parity_bit=uart_setting_info[3],
                    parity_type=uart_setting_info[4],
                    stop_bits_nbr=uart_setting_info[5],
                    word_size=uart_setting_info[6],
                    return_type=uart_setting_info[7],
                    chip_id=chip_id
                )
                uart_setting.save()
