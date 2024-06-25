"""export_manager.py"""

import csv

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QFileDialog

from hardsploit_gui.classes.utils import center_window
from hardsploit_gui.gui.gui_export_manager import Ui_Export_manager


class ExportManager(QWidget):

    def __init__(self, bus, result, spi_data_sended=None):
        super().__init__()
        if spi_data_sended is None:
            spi_data_sended = []
        self.view = Ui_Export_manager()
        center_window(self)
        self.view.setupUi(self)
        self.bus = bus
        # Check the bus type to adapt the table column
        if bus == 'SPI':
            self.create_result_table('SPI')
            self.view.cbx_export.hide()
            self.view.tbl_result.setRowCount(len(result))
            for i in range(len(result)):
                self.view.tbl_result.setItem(i, 0, QTableWidgetItem(str(spi_data_sended[i])))
                self.view.tbl_result.setItem(i, 1, QTableWidgetItem(str(result[i])))

            self.view.tbl_result.horizontalHeader().setStretchLastSection(True)
        else:
            self.create_result_table('I2C')
            self.view.tbl_result.setRowCount(len(result) / 2)
            v = 0
            for i in range(0, len(result), 2):
                # (0..result.length - 1).step(2).each_with_index do |i, v|
                ascii_result = ""
                if str(result[i + 1]).isprintable() and result[i + 1] != 255 and result[i + 1] != 0:
                    ascii_result = chr(result[i + 1])
                if result[i] == 0:
                    self.view.tbl_result.setItem(v, 0, QTableWidgetItem('Write'))
                    self.view.tbl_result.setItem(v, 1, QTableWidgetItem('ACK'))
                    self.view.tbl_result.setItem(v, 2, QTableWidgetItem(str(result[i + 1])))
                    self.view.tbl_result.setItem(v, 3, QTableWidgetItem(ascii_result))
                elif result[i] == 1:
                    self.view.tbl_result.setItem(v, 0, QTableWidgetItem('Read'))
                    self.view.tbl_result.setItem(v, 1, QTableWidgetItem('ACK'))
                    self.view.tbl_result.setItem(v, 2, QTableWidgetItem(str(result[i + 1])))
                    self.view.tbl_result.setItem(v, 3, QTableWidgetItem(ascii_result))
                elif result[i] == 2:
                    self.view.tbl_result.setItem(v, 0, QTableWidgetItem('Write'))
                    self.view.tbl_result.setItem(v, 1, QTableWidgetItem('NACK'))
                    self.view.tbl_result.setItem(v, 2, QTableWidgetItem(str(result[i + 1])))
                    self.view.tbl_result.setItem(v, 3, QTableWidgetItem(ascii_result))
                else:
                    self.view.tbl_result.setItem(v, 0, QTableWidgetItem('Read'))
                    self.view.tbl_result.setItem(v, 1, QTableWidgetItem('NACK'))
                    self.view.tbl_result.setItem(v, 2, QTableWidgetItem(str(result[i + 1])))
                    self.view.tbl_result.setItem(v, 3, QTableWidgetItem(ascii_result))
                v += 1

            self.view.tbl_result.resizeColumnsToContents()
            self.view.tbl_result.resizeRowsToContents()
            self.view.tbl_result.horizontalHeader().setStretchLastSection(True)

    def create_result_table(self, bus):
        if bus == 'SPI':
            self.view.tbl_result.insertColumn(0)
            self.view.tbl_result.setHorizontalHeaderItem(0, QTableWidgetItem('Data send'))
            self.view.tbl_result.insertColumn(1)
            self.view.tbl_result.setHorizontalHeaderItem(1, QTableWidgetItem('Data receive'))
        else:
            self.view.tbl_result.insertColumn(0)
            self.view.tbl_result.setHorizontalHeaderItem(0, QTableWidgetItem('R/W'))
            self.view.tbl_result.insertColumn(1)
            self.view.tbl_result.setHorizontalHeaderItem(1, QTableWidgetItem('(N)ACK)'))
            self.view.tbl_result.insertColumn(2)
            self.view.tbl_result.setHorizontalHeaderItem(2, QTableWidgetItem('DATA'))
            self.view.tbl_result.insertColumn(3)
            self.view.tbl_result.setHorizontalHeaderItem(3, QTableWidgetItem('ASCII'))

    @Slot()
    def save_result(self):
        result_file = QFileDialog.getSaveFileName(self, 'Create a file', '/', 'All files (*)')[0]
        if result_file:
            if self.bus == 'I2C':
                if self.view.cbx_export.currentIndex() == 0:
                    self.save_i2c_csv(result_file)
                else:
                    self.save_i2c(result_file)
            else:
                self.save_spi(result_file)

    def save_i2c_csv(self, result_file):
        f = open(result_file, 'wb')
        writer = csv.writer(f)
        header = ['R/W', '(N)ACK', 'DATA']
        writer.writerow(header)
        for i in range(self.view.tbl_result.rowCount()):
            writer.writerow([self.view.tbl_result.item(i, 0).text(), self.view.tbl_result.item(i, 1).text(),
                             self.view.tbl_result.item(i, 2).text()])
        f.close()

    def save_i2c(self, result_file):
        file = open(result_file, 'wb')
        result = []
        for i in range(self.view.tbl_result.rowCount()):
            if self.view.tbl_result.item(i, 0).text() == 'Read' and self.view.tbl_result.item(i, 1).text() == 'ACK':
                result.append(int(self.view.tbl_result.item(i, 2).text()))
        file.write(bytes(result))
        file.close()

    def save_spi(self, result_file):
        file = open(result_file, 'wb')
        result = []
        for i in range(self.view.tbl_result.rowCount()):
            result.append(int(self.view.tbl_result.item(i, 1).text()))
        file.write(bytes(result))
        file.close()
