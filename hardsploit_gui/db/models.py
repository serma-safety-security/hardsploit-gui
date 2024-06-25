
from pathlib import Path
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase(str(Path(__file__).parent.resolve()) + "/hardsploit.db", pragmas=(
    ('journal_mode', 'wal'),  # Use WAL-mode (you should always use this!).
    ('foreign_keys', 1)  # Enforce foreign-key constraints.
))

class BaseModel(Model):
    class Meta:
        database = db


class Bus(BaseModel):
    name = CharField(max_length=25, unique=True)


class ChipType(BaseModel):
    name = CharField(max_length=20, unique=True)


class Manufacturer(BaseModel):
    name = CharField(max_length=25, unique=True)


class Package(BaseModel):
    name = CharField(max_length=25, unique=True)
    pin_number = IntegerField(constraints=[Check('pin_number > 3')])
    shape = BooleanField()


class Chip(BaseModel):
    reference = CharField(max_length=25, unique=True)
    description = CharField(max_length=140, null=True)
    voltage = IntegerField()
    manufacturer = ForeignKeyField(Manufacturer, backref='chip', on_delete='CASCADE')
    package = ForeignKeyField(Package, backref='chip', on_delete='CASCADE')
    chip_type = ForeignKeyField(ChipType, backref='chip', on_delete='CASCADE')


class Signal(BaseModel):
    name = CharField(max_length=10)
    pin = CharField(max_length=4)


class Use(BaseModel):
    signal = ForeignKeyField(Signal, backref='use')
    bus = ForeignKeyField(Bus, backref='use')
    class Meta:
        primary_key = CompositeKey('signal', 'bus')


class Pin(BaseModel):
    number = IntegerField(constraints=[Check('number >= 0')])
    chip = ForeignKeyField(Chip, backref='pins', on_delete='CASCADE')
    signal = ForeignKeyField(Signal)


class Command(BaseModel):
    name = CharField(max_length=25)
    description = CharField(max_length=140, null=True)
    chip = ForeignKeyField(Chip, backref='commands', on_delete='CASCADE')
    bus = ForeignKeyField(Bus, backref='commands', on_delete='CASCADE')

    def delete_instance(self, recursive=False, delete_nullable=False):
        super().__init__(Command, self).delete_instance()
        Byte.delete().where(Byte.command == self.id).execute()


class Byte(BaseModel):
    position = IntegerField(constraints=[Check('position >= 0')])
    value = CharField(max_length=25)
    description = CharField(max_length=140, null=True)
    iteration = IntegerField(null=True, constraints=[Check('iteration >= 0')])
    command = ForeignKeyField(Command, backref='bytes', on_delete='CASCADE')


class UartSetting(BaseModel):
    baud_rate = IntegerField()
    idle_line = IntegerField(constraints=[Check('idle_line <= 8')])
    parity_bit = IntegerField(constraints=[Check('parity_bit <= 8')])
    parity_type = IntegerField(constraints=[Check('parity_type <= 8')])
    stop_bits_nbr = IntegerField(constraints=[Check('stop_bits_nbr <= 8')])
    word_size = IntegerField(constraints=[Check('word_size <= 8')])
    return_type = IntegerField(constraints=[Check('return_type <= 2')])
    chip = ForeignKeyField(Chip, backref='uart_settings', on_delete='CASCADE')
    
    
class I2cSetting(BaseModel):
    address_w = CharField()
    address_r = CharField()
    frequency = IntegerField(constraints=[Check('frequency >= 100 AND frequency <= 1000')])
    write_page_latency = IntegerField(constraints=[Check('write_page_latency >= 0')])
    page_size = IntegerField(constraints=[Check('page_size >= 0')])
    total_size = IntegerField(constraints=[Check('total_size >= 0')])
    chip = ForeignKeyField(Chip, backref='i2c_settings', on_delete='CASCADE')


class SpiSetting(BaseModel):
    mode = IntegerField(constraints=[Check('mode >= 0 AND mode <= 3')])
    frequency = CharField(max_length=10, null=True)
    write_page_latency = IntegerField(null=True, constraints=[Check('write_page_latency >= 0')])
    command_read = IntegerField(null=True, constraints=[Check('command_read >= 0')])
    command_write = IntegerField(null=True, constraints=[Check('command_write >= 0')])
    command_write_enable = IntegerField(null=True, constraints=[Check('command_write_enable >= 0')])
    command_erase = IntegerField(null=True, constraints=[Check('command_erase >= 0')])
    erase_time = IntegerField(null=True, constraints=[Check('erase_time >= 0')])
    page_size = IntegerField(null=True, constraints=[Check('page_size >= 0')])
    total_size = IntegerField(null=True, constraints=[Check('total_size >= 0')])
    is_flash = IntegerField(null=True, constraints=[Check('is_flash >= 0')])
    chip = ForeignKeyField(Chip, backref='spi_settings', on_delete='CASCADE')

class Nrf24l01Setting(BaseModel):
    channel = IntegerField(constraints=[Check('channel >= 0 AND channel <= 126')])
    address = CharField(max_length=10, null=True)
    chip = ForeignKeyField(Chip, backref='nrf_settings', on_delete='CASCADE')

class SwdSetting(BaseModel):
    cpu_id_address = CharField(max_length=8, null=True, constraints=[Check('length(cpu_id_address) == 8')])
    device_id_address = CharField(max_length=8, null=True, constraints=[Check('length(device_id_address) == 8')])
    memory_size_address = CharField(max_length=8, null=True, constraints=[Check('length(memory_size_address) == 8')])
    memory_start_address = CharField(max_length=8, null=True, constraints=[Check('length(memory_start_address) == 8')])
    chip = ForeignKeyField(Chip, backref='swd_settings', on_delete='CASCADE')


class CanSetting(BaseModel):
    baud_rate = IntegerField(null=True)
    crc_poly = IntegerField(null=True)
    crc_type = IntegerField(null=True)
    identifier = IntegerField(null=True)
    return_frame_format = BooleanField(null=True)
    chip = ForeignKeyField(Chip, backref='can_settings', on_delete='CASCADE')


class ParallelSetting(BaseModel):
    total_size = IntegerField(null=True, constraints=[Check('total_size >= 0')])
    page_size = IntegerField(null=True, constraints=[Check('page_size >= 0')])
    word_size = IntegerField(null=True, constraints=[Check('word_size >= 0')])
    read_latency = IntegerField(null=True, constraints=[Check('read_latency >= 0')])
    write_latency = IntegerField(null=True, constraints=[Check('write_latency >= 0')])
    chip = ForeignKeyField(Chip, backref='parallel_settings', on_delete='CASCADE')

def create_tables():
    with db:
        db.create_tables([Bus, Manufacturer, Package, ChipType, Chip, Signal, Pin, Use, Command, Byte,
                          UartSetting, I2cSetting, SpiSetting, SwdSetting, CanSetting, Nrf24l01Setting,
                          ParallelSetting])


def fill_tables():
    buses = [{'name': 'NA'}, {'name': 'PARALLEL'}, {'name': 'I2C'}, {'name': 'SPI'},
             {'name': 'UART'}, {'name': 'SWD'}, {'name': 'CAN'}, {'name': 'NRF24L01'}]
    chips_type = [{'name': 'MEMORY'}, {'name': 'MICROCONTROLLER'}, {'name': 'TRANSCEIVER'}, {'name': 'NRF24L01'}]
    manufacturers = [{'name': 'Microchip'}, {'name': 'ST Microelectronics'}, {'name': 'Nuvoton'},
                     {'name': 'On Semiconductor'}, {'name': 'Texas Instruments'}, {'name': 'Lapis Semiconductor'},
                     {'name': 'Adesto Technologies'}, {'name': 'Nordic Semiconductor'}]
    packages = [('TSOP', 8, 1), ('LQFP', 64, 0), ('QFN', 33, 0), ('SOIC', 8, 1)]
    chips = [('25LC080', 'Hello SPI', 0, 1, 1, 1), ('24LC64', 'More details here', 0, 1, 1, 1),
             ('STM32F10X', '', 1, 2, 2, 2), ('25160D', 'SPI Memory', 1, 4, 1, 1),
             ('NRF24L01', '', 0, 8, 1, 4)]
    signals = [('NA', 'A0'), ('A0', 'A0'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'),
               ('A6', 'A6'), ('A7', 'A7'), ('A8', 'B0'), ('A9', 'B1'), ('A10', 'B2'), ('A11', 'B3'), ('A12', 'B4'),
               ('A13', 'B5'), ('A14', 'B6'), ('A15', 'B7'), ('A16', 'C0'), ('A17', 'C1'), ('A18', 'C2'), ('A19', 'C3'),
               ('A20', 'C4'), ('A21', 'C5'), ('A22', 'C6'), ('A23', 'C7'), ('A24', 'E0'), ('A25', 'E1'), ('A26', 'E2'),
               ('A27', 'E3'), ('A28', 'E4'), ('A29', 'E5'), ('A30', 'E6'), ('A31', 'E7'), ('D0', 'F0'), ('D1', 'F1'),
               ('D2', 'F2'), ('D3', 'F3'), ('D4', 'F4'), ('D5', 'F5'), ('D6', 'F6'), ('D7', 'F7'), ('D8', 'G0'),
               ('D9', 'G1'), ('D10', 'G2'), ('D11', 'G3'), ('D12', 'G4'), ('D13', 'G5'), ('D14', 'G6'), ('D15', 'G7'),
               ('RST', 'H0'), ('CE', 'H1'), ('OE', 'H2'), ('WE', 'H3'), ('WP', 'H5'), ('ADV', 'H6'), ('PARA_CLK', 'H4'),
               ('SDA', 'A0'), ('I2C_CLK', 'A1'), ('CS', 'A0'), ('MOSI', 'A2'), ('MISO', 'A3'), ('SPI_CLK', 'A1'),
               ('PULSE', 'A4'), ('TX', 'A0'), ('RX', 'A1'), ('SWD_CLK', 'A0'), ('SWD_IO', 'A1'), ('CAN_RX', 'A0'),
               ('CAN_TX', 'A1')]
    pins = [(1, 1, 59), (2, 1, 61), (3, 1, 1), (4, 1, 1), (5, 1, 60), (6, 1, 62), (7, 1, 1), (8, 1, 1), (1, 2, 1),
            (2, 2, 1), (3, 2, 1), (4, 2, 1), (5, 2, 57), (6, 2, 58), (7, 2, 1), (8, 2, 1), (1, 3, 1), (2, 3, 1),
            (3, 3, 1), (4, 3, 1), (5, 3, 1), (6, 3, 1), (7, 3, 1), (8, 3, 1), (9, 3, 1), (10, 3, 1), (11, 3, 1),
            (12, 3, 1), (13, 3, 1), (14, 3, 1), (15, 3, 1), (16, 3, 64), (17, 3, 65), (18, 3, 1), (19, 3, 1),
            (20, 3, 1), (21, 3, 1), (22, 3, 1), (23, 3, 1), (24, 3, 1), (25, 3, 1), (26, 3, 1), (27, 3, 1), (28, 3, 1),
            (29, 3, 1), (30, 3, 1), (31, 3, 1), (32, 3, 1), (33, 3, 1), (34, 3, 1), (35, 3, 1), (36, 3, 1), (37, 3, 1),
            (38, 3, 1), (39, 3, 1), (40, 3, 1), (41, 3, 1), (42, 3, 1), (43, 3, 1), (44, 3, 1), (45, 3, 1), (46, 3, 67),
            (47, 3, 1), (48, 3, 1), (49, 3, 66), (50, 3, 1), (51, 3, 1), (52, 3, 1), (53, 3, 1), (54, 3, 1), (55, 3, 1),
            (56, 3, 1), (57, 3, 1), (58, 3, 1), (59, 3, 1), (60, 3, 1), (61, 3, 1), (62, 3, 1), (63, 3, 1), (64, 3, 1),
            (1, 4, 59), (2, 4, 61), (3, 4, 1), (4, 4, 1), (5, 4, 60), (6, 4, 62), (7, 4, 1), (8, 4, 1),
            (1, 5, 1), (2, 5, 63), (3, 5, 62), (4, 5, 61), (5, 5, 1), (6, 5, 60), (7, 5, 59), (8, 5, 1)]
    uses = [(1, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13),
            (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 24), (2, 25),
            (2, 26), (2, 27), (2, 28), (2, 29), (2, 30), (2, 31), (2, 32), (2, 33), (2, 34), (2, 35), (2, 36), (2, 37),
            (2, 38), (2, 39), (2, 40), (2, 41), (2, 42), (2, 43), (2, 44), (2, 45), (2, 46), (2, 47), (2, 48), (2, 49),
            (2, 50), (2, 51), (2, 52), (2, 53), (2, 54), (2, 55), (2, 56), (3, 57), (3, 58), (4, 59), (4, 60), (4, 61),
            (4, 62), (4, 63), (5, 64), (5, 65), (6, 66), (6, 67), (7, 68), (7, 69)]
    commands = [('Write pointer', '', 2, 3), ('Read code', '', 2, 3), ('Write test', '', 2, 3),
                ('Arm Drone', 'Send a arming request to the drone', 5, 8),
                ('Keep alive Drone', 'Send a keep alive frame to the drone', 5, 8),
               ]
    bytes_ = [(1, '02', 'Payload size - low', None, 1), (2, '00', 'Payload size - high', None, 1),
             (3, 'A6', 'Write address (control byte)', None, 1), (4, '00', 'Payload byte', None, 1),
             (5, '00', 'Payload byte', None, 1), (1, '04', 'Payload size - low', None, 2),
             (2, '00', 'Payload size - high', None, 2), (3, 'A7', 'Read address (control byte)', None, 2),
             (1, '04', 'Payload size - low', None, 3), (2, '00', 'Payload size - high', None, 3),
             (3, 'A6', 'Write address (control byte)', None, 3), (4, '08', 'Payload byte', None, 3),
             (5, '02', 'Payload byte', None, 3), (6, '78', 'Payload byte', None, 3), (7, '64', 'Payload byte', None, 3),
             *[(i+1, f"{b:02x}", '', None, 4) for i, b in enumerate([23, 3, 97, 100, 109, 105, 110, 0, 0, 24, 99, 36, 163, 0, 0, 128])],
             *[(i+1, f"{b:02x}", '', None, 5) for i, b in enumerate([0, 0, 128, 128, 128, 0, 0, 0, 0, 24, 99, 36, 163, 0, 0, 128])],
             ]
    uart_settings = [(57600, 1, 0, 0, 1, 8, 0, 3)]
    i2c_settings = [('A6', 'A7', 100, 4, 32, 8192, 2)]
    nrf_settings = [(64, '6688686868', 5)]

    with db.atomic():
        Bus.insert_many(buses).execute()
        ChipType.insert_many(chips_type).execute()
        Manufacturer.insert_many(manufacturers).execute()
        Package.insert_many(packages, fields=[Package.name, Package.pin_number, Package.shape]).execute()
        Chip.insert_many(chips, fields=[Chip.reference, Chip.description, Chip.voltage, Chip.manufacturer,
                                        Chip.package, Chip.chip_type]).execute()
        Signal.insert_many(signals, fields=[Signal.name, Signal.pin]).execute()
        Pin.insert_many(pins, fields=[Pin.number, Pin.chip, Pin.signal]).execute()
        Use.insert_many(uses, fields=[Use.bus, Use.signal]).execute()
        Command.insert_many(commands, fields=[Command.name, Command.description, Command.chip, Command.bus]).execute()
        Byte.insert_many(bytes_, fields=[Byte.position, Byte.value, Byte.description, Byte.iteration, Byte.command])\
            .execute()
        UartSetting.insert_many(uart_settings, fields=[UartSetting.baud_rate, UartSetting.idle_line,
                                                       UartSetting.parity_bit, UartSetting.parity_type,
                                                       UartSetting.stop_bits_nbr,
                                                       UartSetting.word_size, UartSetting.return_type,
                                                       UartSetting.chip]).execute()
        I2cSetting.insert_many(i2c_settings, fields=[I2cSetting.address_w, I2cSetting.address_r,
                                                       I2cSetting.frequency, I2cSetting.write_page_latency,
                                                       I2cSetting.page_size, I2cSetting.total_size,
                                                       I2cSetting.chip]).execute()
        Nrf24l01Setting.insert_many(nrf_settings,
                               fields=[Nrf24l01Setting.channel, Nrf24l01Setting.address, Nrf24l01Setting.chip]
                               ).execute()

if __name__ == "__main__":
    create_tables()
    fill_tables()
