"""command_editor.py"""

from PySide6.QtCore import QObject, SIGNAL, SLOT, QRegularExpression, Slot
from PySide6.QtGui import QRegularExpressionValidator, QValidator
from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

from hardsploit_gui.classes.command_table import CommandTable
from hardsploit_gui.classes.error_msg import ErrorMsg
from hardsploit_gui.classes.utils import center_window, input_restrict
from hardsploit_gui.db.models import Bus, Command, Byte
from hardsploit_gui.gui.gui_command_editor import Ui_Command_editor

# TODO: Extract specific logic (SPI & I2C) in dediceted inherited class.


class CommandEditor(QWidget):
    """Custom command edition window.

    This class implements generic functionalities
    for command edition. Each bus should inherits from it and
    implements any specific functionalities in inherited class."""

    def __init__(self, action, cmd_id, cmd_name, chip, bus_id, parent, **bus_param):
        super().__init__()
        self.view = Ui_Command_editor()
        center_window(self)
        self.view.setupUi(self)
        self.bus = Bus.get(bus_id)
        self.chip_id = chip.id
        self.cmd_id = cmd_id
        self.cmd_name = cmd_name
        self.bus_id = bus_id
        self.parent = parent
        self.cmd = None
        self.cmd_table = CommandTable(self.view.tbl_bytes, self.bus.name)
        input_restrict(self.view.lie_name, 2)
        input_restrict(self.view.lie_description, 2)
        self.view.lbl_chip_val.setText(chip.reference)
        if self.bus.name == 'SPI':
            self.cmd_table.build_spi()
        else:
            self.view.lie_text_2_bytes.hide()

        if action == 0:
            # Add
            self.view.lbl_cmd_val.setText('-')
            QObject.connect(self.view.btn_validate, SIGNAL('clicked()'), self, SLOT('add_cmd()'))
        elif action == 1:
            # Template
            self.view.lbl_cmd_val.setText(cmd_name)
            self.feed_editor_form()
            self.view.lie_name.setText('')
            QObject.connect(self.view.btn_validate, SIGNAL('clicked()'), self, SLOT('add_cmd()'))
        else:
            # Edit
            self.view.lbl_cmd_val.setText(cmd_name)
            self.feed_editor_form()
            self.view.btn_validate.setText('Edit')
            QObject.connect(self.view.btn_validate, SIGNAL('clicked()'), self, SLOT('edit_cmd()'))
        if len(bus_param) > 0:
            self.feed_i2c_cmd_array(bus_param)

    def feed_i2c_cmd_array(self, bus_param):
        if bus_param['mode'] == 'w':
            self.cmd_table.i2c_write_cmd(bus_param['addr'], int(bus_param['size']))
        else:
            self.cmd_table.i2c_read_cmd(bus_param['addr'], int(bus_param['size']))

    @Slot()
    def add_cmd(self):

        # Check that the command name isn't empty
        if not self.view.lie_name.text():
            QMessageBox(QMessageBox.Warning, 'Command name', 'The command name is empty').exec_()
            return False

        # Check bytes array
        if self.cmd_table.empty_data_exist() or not self.is_cmd_size_valid():
            return False

        self.cmd = Command.create(
            name=self.view.lie_name.text(),
            description=self.view.lie_description.text(),
            bus_id=self.bus_id,
            chip_id=self.chip_id
        )
        self.add_bytes()
        self.parent.feed_cmd_array()
        self.close()


    @Slot()
    def edit_cmd(self):
        """Edit an existing command."""
        # Check that the command name isn't empty
        if not self.view.lie_name.text():
            QMessageBox(QMessageBox.Warning, 'Command name', 'The command name is empty').exec_()
            return False

        # Check bytes array
        if self.cmd_table.empty_data_exist() or not self.is_cmd_size_valid():
            return False

        # Save edited command
        self.cmd = Command.select().where((Command.id == self.cmd_id) & (Command.chip_id == self.chip_id)).first()
        self.cmd.name = self.view.lie_name.text()
        self.cmd.description = self.view.lie_description.text()
        self.cmd.save()

        # Remove previous bytes entries in the database
        Byte.delete().where(Byte.command_id == self.cmd.id).execute()

        # ... and write new bytes in place
        self.add_bytes()
        self.parent.feed_cmd_array()
        self.close()

    def add_bytes(self):
        """Register the bytes in the database."""
        col_byte = self.cmd_table.col_byte
        col_desc = self.cmd_table.col_desc
        col_rep = None
        if self.bus.name == "SPI":
            col_rep = self.cmd_table.col_rep

        for i in range(self.view.tbl_bytes.rowCount()):
            byte_val = self.view.tbl_bytes.item(i, col_byte).text()
            description = self.view.tbl_bytes.item(i, col_desc).text()
            if self.bus.name == 'SPI':
                iteration = self.view.tbl_bytes.item(i, col_rep).text()
            else:
                iteration = None

            Byte.create(
                position=i+1,
                value=byte_val,
                iteration=iteration,
                description=description,
                command_id=self.cmd.id
            )
        QMessageBox(QMessageBox.Information, 'Command status', 'Command saved').exec_()

    @Slot(QTableWidgetItem)
    def check_cell_content(self, item):
        """Sanity check for the content of the cells."""

        if self.view.tbl_bytes.horizontalHeaderItem(item.column()).text() == 'Repetition':
            # Repetition field should be > 0
            if item.text() and not item.text().isdigit():
                item.setText('')
                ErrorMsg.int_cell_value()
            elif int(item.text()) < 0:
                item.setData(0, 0)
                ErrorMsg.positive_cell_value()
        elif self.view.tbl_bytes.horizontalHeaderItem(item.column()).text() == 'Byte (Hexa)':
            # Data contains only valid hexadecimal character
            reg = QRegularExpression("^[A-Fa-f0-9]{2}")
            reg_val = QRegularExpressionValidator(reg)
            if reg_val.validate(item.text(), len(item.text()))[0] == QValidator.Invalid or not item.text():
                ErrorMsg.hexa_cell_value()
                item.setText('')
        elif self.view.tbl_bytes.horizontalHeaderItem(item.column()).text() == 'Description':
            # Text should be valid ascii
            if item.text() and not item.text().isascii():
                item.setText('')
                ErrorMsg.char_cell_value()


    def is_cmd_size_valid(self):
        try:
            byte_table_size = self.view.tbl_bytes.rowCount()
            if self.bus.name == 'SPI':
                cmd_size = byte_table_size + self.cmd_table.count_total_repetition()
                if cmd_size < 4000:
                    return True
                return ErrorMsg.spi_cmd_too_long()
            # Need to be updated, doesn't work
            elif self.bus.name == 'I2C':
                """ TODO: Correct wrong verif
                while i <= byte_table_size - 1:
                    low_byte = self.view.tbl_bytes.item(i, 1)
                    high_byte = self.view.tbl_bytes.item(i + 1, 1)
                    command_byte = self.view.tbl_bytes.item(i + 2, 1)
                    if not low_byte:
                        return ErrorMsg.lowbyte_missing()
                    if not high_byte:
                        return ErrorMsg.highbyte_missing()
                    if not command_byte:
                        return ErrorMsg.mode_missing()
                    current_count = HardsploitUtils.BytesToInt(
                        lByte=int(low_byte.text(), 16),
                        hByte=int(high_byte.text(), 16)
                    )
                    count += current_count
                    if int(command_byte.text(), 16) % 2 == 0:
                        i += current_count + 3
                    else:
                        i += 3
                if i != byte_table_size:
                    return ErrorMsg.size_neq_row_number()
                if count > 2000:
                    return ErrorMsg.i2c_cmd_too_long()
                """
                return True
            # TODO: Add verification for NRF24L01C
            return True
        except ValueError as Ve:
            ErrorMsg.custom("Value error", f"Invalid repetition value on line :  {Ve}")
        except Exception as e:
            ErrorMsg.unknown(e)


    def feed_editor_form(self):
        """Fills the command table with the current command."""
        cmd = Command.get(Command.id == self.cmd_id)
        self.view.lie_name.setText(self.cmd_name)
        self.view.lie_description.setText(cmd.description)

        # Order the retrieved bytes from the database
        byte_list = cmd.bytes.order_by(Byte.position)
        self.cmd_table.fill_byte_table(byte_list)

    @Slot()
    def add_row(self):
        """Action to execute when user wants to add a new row."""
        if self.view.lie_text_2_bytes.text() == "":
            self.cmd_table.add_row()
        else:
            self.cmd_table.add_text_rows(self.view.lie_text_2_bytes.text())
            self.view.lie_text_2_bytes.setText('')

    @Slot()
    def clone_row(self):
        self.cmd_table.clone_rows()

    @Slot()
    def remove_row(self):
        self.cmd_table.remove_rows()
