"""command_table.py"""

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from hardsploit.core import HardsploitUtils
from hardsploit_gui.classes.error_msg import ErrorMsg

# TODO: Improve integration by inheriting the class as QTable
#       and insert the widget in place of the QTable in the CommandEditor


class CommandTable(QWidget):
    """Wrapper class around QTable to provide inner logic
    in the context of the custom command edition.
    """
    def __init__(self, cmd_table, bus):
        super().__init__()
        self.cmd_table = cmd_table
        self.bus = bus

        # Column indices
        self.col_byte = 0
        self.col_desc = 1

        # Create columns
        self.cmd_table.insertColumn(0)
        self.cmd_table.insertColumn(0)
        self.cmd_table.setHorizontalHeaderItem(self.col_byte, QTableWidgetItem('Byte (Hexa)'))
        self.cmd_table.setHorizontalHeaderItem(self.col_desc, QTableWidgetItem('Description'))

        self.col_rep = None

    def build_spi(self):
        """Specific columns for SPI bus."""
        self.col_rep = self.col_desc
        self.col_rep += 1

        self.cmd_table.insertColumn(self.col_rep)
        self.cmd_table.setHorizontalHeaderItem(self.col_rep, QTableWidgetItem('Repetition'))

    def fill_byte_table(self, byte_list):
        """Load the bytes of a command in the table."""
        for i, b in enumerate(byte_list):
            self.cmd_table.insertRow(self.cmd_table.rowCount())
            self.cmd_table.setItem(i, self.col_byte, QTableWidgetItem(b.value))
            if self.bus == 'SPI':
                self.cmd_table.setItem(i, self.col_rep, QTableWidgetItem(str(b.iteration)))
            self.cmd_table.setItem(i, self.col_desc, QTableWidgetItem(b.description))

    def add_row(self):
        """Action to execute when the user want to add a new row in the table."""
        self._add_row()

    def add_text_rows(self, txt):
        """Action to execute when the user want to add multiple row from ascii text."""
        if not txt.isascii():
            # TODO: prefer txt.isalnum()
            # (and even check for hexa)
            return ErrorMsg.ascii_only()

        # Get a list of each pair of characters in 'txt'
        txt_bytes = [txt[i:i+2] for i in range(0, len(txt), 2)]

        for hexpair in txt_bytes:
            self._add_row(hexpair)

    def _add_row(self, byte_val='00', description='', rep='0'):
        """Lower level function to add a row in the given fields
        in the table.
        """
        row = self.cmd_table.rowCount()
        self.cmd_table.insertRow(row)
        self.cmd_table.setItem(row, self.col_byte, QTableWidgetItem(byte_val))
        if self.bus == 'SPI':
            self.cmd_table.setItem(row, self.col_rep, QTableWidgetItem(rep))
        self.cmd_table.setItem(row, self.col_desc, QTableWidgetItem(description))
        self.cmd_table.scrollToBottom()

    def clone_rows(self):
        """Clone selected rows and add them in the table."""
        # TODO: Double check the function logic, it doesn't behave as expected
        if not self.cmd_table.currentItem():
            return 0

        rows_to_clone = []
        for item in self.cmd_table.selectedItems():
            rows_to_clone.append(item.row())
        rows_to_clone = list(dict.fromkeys(rows_to_clone))
        for i, row in enumerate(rows_to_clone):
            last_row = self.cmd_table.rowCount() - 1
            self.cmd_table.insertRow(last_row + 1)
            if self.cmd_table.item(row, self.col_byte):
                self.cmd_table.setItem(last_row + 1, self.col_byte,
                                       QTableWidgetItem(self.cmd_table.item(row, self.col_byte).text()))
            if self.bus == 'SPI' and self.cmd_table.item(row, self.col_rep):
                self.cmd_table.setItem(last_row + 1, self.col_rep,
                                       QTableWidgetItem(self.cmd_table.item(row, self.col_rep).text()))
            if self.cmd_table.item(row, self.col_desc) is not None:
                self.cmd_table.setItem(last_row + 1, self.col_desc,
                                       QTableWidgetItem(self.cmd_table.item(row, self.col_desc).text()))

    def remove_rows(self):
        """Remove selected rows from the table."""
        if not self.cmd_table.currentItem():
            return 0
        rows_to_delete = []
        for item in (self.cmd_table.selectedItems()):
            rows_to_delete.append(item.row())
        rows_to_delete = list(dict.fromkeys(rows_to_delete))
        for i, row in enumerate(rows_to_delete):
            self.cmd_table.removeRow(int(row) - i)

    def i2c_read_cmd(self, write_address, cmd_size):
        # Byte array size
        self.cmd_table.setRowCount(3)
        # Size 1
        self.cmd_table.setItem(0, self.col_byte, QTableWidgetItem(hex(HardsploitUtils.low_byte(word=cmd_size))[2:].upper()))
        self.cmd_table.setItem(0, self.col_desc, QTableWidgetItem('Payload size - low'))
        # Size 2
        self.cmd_table.setItem(1, self.col_byte, QTableWidgetItem(hex(HardsploitUtils.high_byte(word=cmd_size))[2:].upper()))
        self.cmd_table.setItem(1, self.col_desc, QTableWidgetItem('Payload size - high'))
        # Address
        self.cmd_table.setItem(2, self.col_byte, QTableWidgetItem(write_address))
        self.cmd_table.setItem(2, self.col_desc, QTableWidgetItem('Read address (control byte)'))

    def i2c_write_cmd(self, write_address, cmd_size):
        # Byte array size
        self.cmd_table.setrowCount(3 + cmd_size)
        # Payload size low
        # -byte
        item_lb1 = QTableWidgetItem(chr(HardsploitUtils.low_byte(word=cmd_size)).upper())
        self.cmd_table.setItem(0, self.col_byte, item_lb1)
        # -description
        item_lb3 = QTableWidgetItem('Payload size - low')
        self.cmd_table.setItem(0, self.col_desc, item_lb3)
        # Payload size high
        # -byte
        item_hb1 = QTableWidgetItem(chr(HardsploitUtils.high_byte(word=cmd_size)).upper())
        self.cmd_table.setItem(1, self.col_byte, item_hb1)
        # -description
        item_hb3 = QTableWidgetItem('Payload size - high')
        self.cmd_table.setItem(1, self.col_desc, item_hb3)
        # Address
        # -byte
        item_a1 = QTableWidgetItem(write_address)
        self.cmd_table.setItem(2, self.col_byte, item_a1)
        # -description
        item_a3 = QTableWidgetItem('Write address (control byte)')
        self.cmd_table.setItem(2, self.col_desc, item_a3)
        # Payload bytes
        for i in range(3, cmd_size+3):
            self.cmd_table.setItem(i, self.col_byte, QTableWidgetItem(''))
            self.cmd_table.setItem(i, self.col_desc, QTableWidgetItem('Payload byte'))

    def resize_to_content(self):
        self.cmd_table.resizeColumnsToContents()
        self.cmd_table.resizeRowsToContents()
        self.cmd_table.horizontalHeader().setStretchLastSection(True)

    def count_total_repetition(self):
        """Count the total number of repetition including eventual repetition
        of bytes inside the table.
        """
        if self.bus == "SPI":
            repetition_value = 0
            for i in range(self.cmd_table.rowCount()):
                if self.cmd_table.item(i, self.col_rep).text():
                    repetition_value += int(self.cmd_table.item(i, self.col_rep).text())
                else:
                    raise ValueError(i+1)
        else:
            repetition_value = self.cmd_table.rowCount()

        return repetition_value

    def empty_data_exist(self):
        """Check in the table if any mandatory information is missing.
        Returns 'True' in that case."""
        # Check that the actual table isn't empty
        if self.cmd_table.rowCount() == 0:
            QMessageBox(QMessageBox.Warning, 'Bytes array empty', 'The bytes array is empty').exec_()
            return True

        # For each cell, check for missing information
        for i in range(self.cmd_table.rowCount()):
            # EMPTY BYTE CELL
            if not self.cmd_table.item(i, self.col_byte):
                self.cmd_table.setCurrentItem(self.cmd_table.item(i, self.col_byte))
                QMessageBox(QMessageBox.Warning, 'Empty byte', 'Empty byte cell detected').exec_()
                return True
            if self.bus == 'SPI':
                # EMPTY REPETITION CELL
                if int(self.cmd_table.item(i, self.col_rep).text()) < 1:
                    self.cmd_table.setCurrentItem(self.cmd_table.item(i, self.col_rep))
                    ErrorMsg.repetition_value(i+1)
                    return True
        return False
