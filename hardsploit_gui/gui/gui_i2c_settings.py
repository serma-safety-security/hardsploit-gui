# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_i2c_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_I2c_settings(object):
    def setupUi(self, I2c_settings):
        if not I2c_settings.objectName():
            I2c_settings.setObjectName(u"I2c_settings")
        I2c_settings.resize(339, 504)
        self.gridLayout = QGridLayout(I2c_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_chip = QLabel(I2c_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.lbl_parameters = QLabel(I2c_settings)
        self.lbl_parameters.setObjectName(u"lbl_parameters")

        self.hl2.addWidget(self.lbl_parameters)

        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs2)


        self.vl.addLayout(self.hl2)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_address_w = QLabel(I2c_settings)
        self.lbl_address_w.setObjectName(u"lbl_address_w")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_address_w)

        self.lie_address_w = QLineEdit(I2c_settings)
        self.lie_address_w.setObjectName(u"lie_address_w")
        self.lie_address_w.setMaxLength(2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lie_address_w)

        self.lbl_address_r = QLabel(I2c_settings)
        self.lbl_address_r.setObjectName(u"lbl_address_r")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_address_r)

        self.lie_address_r = QLineEdit(I2c_settings)
        self.lie_address_r.setObjectName(u"lie_address_r")
        self.lie_address_r.setMaxLength(2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lie_address_r)


        self.vl.addLayout(self.formLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(I2c_settings)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.btn_bus_scan = QPushButton(I2c_settings)
        self.btn_bus_scan.setObjectName(u"btn_bus_scan")

        self.horizontalLayout.addWidget(self.btn_bus_scan)


        self.vl.addLayout(self.horizontalLayout)

        self.tbl_bus_scan = QTableWidget(I2c_settings)
        if (self.tbl_bus_scan.columnCount() < 2):
            self.tbl_bus_scan.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_bus_scan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_bus_scan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_bus_scan.setObjectName(u"tbl_bus_scan")
        self.tbl_bus_scan.horizontalHeader().setDefaultSectionSize(85)
        self.tbl_bus_scan.horizontalHeader().setStretchLastSection(True)
        self.tbl_bus_scan.verticalHeader().setVisible(False)

        self.vl.addWidget(self.tbl_bus_scan)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_frequency = QLabel(I2c_settings)
        self.lbl_frequency.setObjectName(u"lbl_frequency")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_frequency)

        self.cbx_frequency = QComboBox(I2c_settings)
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.setObjectName(u"cbx_frequency")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cbx_frequency)

        self.lbl_write_page_latency = QLabel(I2c_settings)
        self.lbl_write_page_latency.setObjectName(u"lbl_write_page_latency")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_write_page_latency)

        self.lie_write_page_latency = QLineEdit(I2c_settings)
        self.lie_write_page_latency.setObjectName(u"lie_write_page_latency")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lie_write_page_latency)

        self.lbl_page_size = QLabel(I2c_settings)
        self.lbl_page_size.setObjectName(u"lbl_page_size")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_page_size)

        self.lbl_full_size = QLabel(I2c_settings)
        self.lbl_full_size.setObjectName(u"lbl_full_size")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_full_size)

        self.lie_page_size = QLineEdit(I2c_settings)
        self.lie_page_size.setObjectName(u"lie_page_size")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_page_size)

        self.lie_total_size = QLineEdit(I2c_settings)
        self.lie_total_size.setObjectName(u"lie_total_size")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lie_total_size)


        self.vl.addLayout(self.formLayout)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(I2c_settings)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(I2c_settings)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))

        self.hl.addWidget(self.btn_save)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(I2c_settings)
        self.btn_cancel.clicked.connect(I2c_settings.close)
        self.btn_save.clicked.connect(I2c_settings.save_settings)
        self.btn_bus_scan.clicked.connect(I2c_settings.bus_scan)

        QMetaObject.connectSlotsByName(I2c_settings)
    # setupUi

    def retranslateUi(self, I2c_settings):
        I2c_settings.setWindowTitle(QCoreApplication.translate("I2c_settings", u"Hardsploit - I\u00b2C settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("I2c_settings", u"[CHIP]", None))
        self.lbl_parameters.setText(QCoreApplication.translate("I2c_settings", u"PARAMETERS", None))
        self.lbl_address_w.setText(QCoreApplication.translate("I2c_settings", u"Base address (W):", None))
        self.lie_address_w.setPlaceholderText(QCoreApplication.translate("I2c_settings", u"in hexadecimal", None))
        self.lbl_address_r.setText(QCoreApplication.translate("I2c_settings", u"Base address (R):", None))
        self.lie_address_r.setPlaceholderText(QCoreApplication.translate("I2c_settings", u"in hexadecimal", None))
        self.label.setText(QCoreApplication.translate("I2c_settings", u"You don't know the addresses? Try a scan:", None))
        self.btn_bus_scan.setText(QCoreApplication.translate("I2c_settings", u"Launch", None))
        ___qtablewidgetitem = self.tbl_bus_scan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("I2c_settings", u"Address", None));
        ___qtablewidgetitem1 = self.tbl_bus_scan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("I2c_settings", u"R/W", None));
        self.lbl_frequency.setText(QCoreApplication.translate("I2c_settings", u"Frequency (Khz):", None))
        self.cbx_frequency.setItemText(0, QCoreApplication.translate("I2c_settings", u"100", None))
        self.cbx_frequency.setItemText(1, QCoreApplication.translate("I2c_settings", u"400", None))
        self.cbx_frequency.setItemText(2, QCoreApplication.translate("I2c_settings", u"1000", None))

        self.lbl_write_page_latency.setText(QCoreApplication.translate("I2c_settings", u"Write page latency:", None))
        self.lie_write_page_latency.setPlaceholderText(QCoreApplication.translate("I2c_settings", u"in miliseconds", None))
        self.lbl_page_size.setText(QCoreApplication.translate("I2c_settings", u"Page size:", None))
        self.lbl_full_size.setText(QCoreApplication.translate("I2c_settings", u"Total size:", None))
        self.lie_page_size.setText("")
        self.lie_page_size.setPlaceholderText(QCoreApplication.translate("I2c_settings", u"in byte", None))
        self.lie_total_size.setPlaceholderText(QCoreApplication.translate("I2c_settings", u"in byte, to a maximum of 4Go", None))
        self.btn_cancel.setText(QCoreApplication.translate("I2c_settings", u"Close", None))
        self.btn_save.setText(QCoreApplication.translate("I2c_settings", u"Save", None))
    # retranslateUi

