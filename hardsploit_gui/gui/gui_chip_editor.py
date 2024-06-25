# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_chip_editor.ui'
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
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Chip_editor(object):
    def setupUi(self, Chip_editor):
        if not Chip_editor.objectName():
            Chip_editor.setObjectName(u"Chip_editor")
        Chip_editor.setWindowModality(Qt.ApplicationModal)
        Chip_editor.resize(414, 594)
        self.gridLayout = QGridLayout(Chip_editor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tbl_pins = QTableWidget(Chip_editor)
        if (self.tbl_pins.columnCount() < 3):
            self.tbl_pins.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_pins.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_pins.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_pins.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbl_pins.setObjectName(u"tbl_pins")
        self.tbl_pins.setMinimumSize(QSize(0, 200))
        self.tbl_pins.setMaximumSize(QSize(16777215, 16777215))
        self.tbl_pins.horizontalHeader().setStretchLastSection(True)
        self.tbl_pins.verticalHeader().setVisible(False)
        self.tbl_pins.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tbl_pins, 1, 0, 1, 1)

        self.lbl_advice = QLabel(Chip_editor)
        self.lbl_advice.setObjectName(u"lbl_advice")

        self.gridLayout.addWidget(self.lbl_advice, 2, 0, 1, 1)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(Chip_editor)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_add = QPushButton(Chip_editor)
        self.btn_add.setObjectName(u"btn_add")

        self.hl.addWidget(self.btn_add)


        self.gridLayout.addLayout(self.hl, 3, 0, 1, 1)

        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.fl = QFormLayout()
        self.fl.setObjectName(u"fl")
        self.lbl_ref = QLabel(Chip_editor)
        self.lbl_ref.setObjectName(u"lbl_ref")

        self.fl.setWidget(0, QFormLayout.LabelRole, self.lbl_ref)

        self.lie_reference = QLineEdit(Chip_editor)
        self.lie_reference.setObjectName(u"lie_reference")
        self.lie_reference.setMaxLength(30)

        self.fl.setWidget(0, QFormLayout.FieldRole, self.lie_reference)

        self.lbl_description = QLabel(Chip_editor)
        self.lbl_description.setObjectName(u"lbl_description")

        self.fl.setWidget(1, QFormLayout.LabelRole, self.lbl_description)

        self.lie_description = QLineEdit(Chip_editor)
        self.lie_description.setObjectName(u"lie_description")
        self.lie_description.setMaxLength(200)

        self.fl.setWidget(1, QFormLayout.FieldRole, self.lie_description)

        self.lbl_voltage = QLabel(Chip_editor)
        self.lbl_voltage.setObjectName(u"lbl_voltage")

        self.fl.setWidget(2, QFormLayout.LabelRole, self.lbl_voltage)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.groupBox = QGroupBox(Chip_editor)
        self.groupBox.setObjectName(u"groupBox")
        self.rbn_3v = QRadioButton(self.groupBox)
        self.rbn_3v.setObjectName(u"rbn_3v")
        self.rbn_3v.setGeometry(QRect(10, 0, 70, 21))
        self.rbn_3v.setChecked(True)
        self.rbn_3v.setAutoExclusive(True)
        self.rbn_5v = QRadioButton(self.groupBox)
        self.rbn_5v.setObjectName(u"rbn_5v")
        self.rbn_5v.setGeometry(QRect(90, 0, 109, 21))
        self.rbn_5v.setAutoExclusive(True)

        self.hl2.addWidget(self.groupBox)


        self.fl.setLayout(2, QFormLayout.FieldRole, self.hl2)

        self.lbl_manu = QLabel(Chip_editor)
        self.lbl_manu.setObjectName(u"lbl_manu")

        self.fl.setWidget(3, QFormLayout.LabelRole, self.lbl_manu)

        self.hl4 = QHBoxLayout()
        self.hl4.setObjectName(u"hl4")
        self.cbx_manufacturer = QComboBox(Chip_editor)
        self.cbx_manufacturer.addItem("")
        self.cbx_manufacturer.setObjectName(u"cbx_manufacturer")

        self.hl4.addWidget(self.cbx_manufacturer)

        self.btn_delete_manufacturer = QPushButton(Chip_editor)
        self.btn_delete_manufacturer.setObjectName(u"btn_delete_manufacturer")
        self.btn_delete_manufacturer.setMaximumSize(QSize(30, 16777215))

        self.hl4.addWidget(self.btn_delete_manufacturer)


        self.fl.setLayout(3, QFormLayout.FieldRole, self.hl4)

        self.lie_manu_name = QLineEdit(Chip_editor)
        self.lie_manu_name.setObjectName(u"lie_manu_name")
        self.lie_manu_name.setMaxLength(30)

        self.fl.setWidget(4, QFormLayout.FieldRole, self.lie_manu_name)

        self.lbl_type = QLabel(Chip_editor)
        self.lbl_type.setObjectName(u"lbl_type")

        self.fl.setWidget(5, QFormLayout.LabelRole, self.lbl_type)

        self.hl5 = QHBoxLayout()
        self.hl5.setObjectName(u"hl5")
        self.cbx_type = QComboBox(Chip_editor)
        self.cbx_type.addItem("")
        self.cbx_type.setObjectName(u"cbx_type")

        self.hl5.addWidget(self.cbx_type)

        self.btn_delete_type = QPushButton(Chip_editor)
        self.btn_delete_type.setObjectName(u"btn_delete_type")
        self.btn_delete_type.setMaximumSize(QSize(30, 16777215))

        self.hl5.addWidget(self.btn_delete_type)


        self.fl.setLayout(5, QFormLayout.FieldRole, self.hl5)

        self.lie_type_name = QLineEdit(Chip_editor)
        self.lie_type_name.setObjectName(u"lie_type_name")
        self.lie_type_name.setMaxLength(30)

        self.fl.setWidget(6, QFormLayout.FieldRole, self.lie_type_name)

        self.lbl_package = QLabel(Chip_editor)
        self.lbl_package.setObjectName(u"lbl_package")

        self.fl.setWidget(7, QFormLayout.LabelRole, self.lbl_package)

        self.hl1 = QHBoxLayout()
        self.hl1.setObjectName(u"hl1")
        self.cbx_package = QComboBox(Chip_editor)
        self.cbx_package.addItem("")
        self.cbx_package.setObjectName(u"cbx_package")

        self.hl1.addWidget(self.cbx_package)

        self.btn_delete_package = QPushButton(Chip_editor)
        self.btn_delete_package.setObjectName(u"btn_delete_package")
        self.btn_delete_package.setMaximumSize(QSize(30, 16777215))

        self.hl1.addWidget(self.btn_delete_package)


        self.fl.setLayout(7, QFormLayout.FieldRole, self.hl1)

        self.lbl_name = QLabel(Chip_editor)
        self.lbl_name.setObjectName(u"lbl_name")

        self.fl.setWidget(8, QFormLayout.LabelRole, self.lbl_name)

        self.lie_pack_name = QLineEdit(Chip_editor)
        self.lie_pack_name.setObjectName(u"lie_pack_name")
        self.lie_pack_name.setMaxLength(30)

        self.fl.setWidget(8, QFormLayout.FieldRole, self.lie_pack_name)

        self.lbl_pack_pin = QLabel(Chip_editor)
        self.lbl_pack_pin.setObjectName(u"lbl_pack_pin")

        self.fl.setWidget(9, QFormLayout.LabelRole, self.lbl_pack_pin)

        self.lie_pack_pin = QLineEdit(Chip_editor)
        self.lie_pack_pin.setObjectName(u"lie_pack_pin")
        self.lie_pack_pin.setMaxLength(3)

        self.fl.setWidget(9, QFormLayout.FieldRole, self.lie_pack_pin)

        self.lbl_pack_shape = QLabel(Chip_editor)
        self.lbl_pack_shape.setObjectName(u"lbl_pack_shape")

        self.fl.setWidget(10, QFormLayout.LabelRole, self.lbl_pack_shape)

        self.hl3 = QHBoxLayout()
        self.hl3.setObjectName(u"hl3")
        self.groupBox_2 = QGroupBox(Chip_editor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.rbn_square = QRadioButton(self.groupBox_2)
        self.rbn_square.setObjectName(u"rbn_square")
        self.rbn_square.setGeometry(QRect(10, 0, 81, 20))
        self.rbn_square.setChecked(True)
        self.rbn_square.setAutoExclusive(True)
        self.rbn_rectangular = QRadioButton(self.groupBox_2)
        self.rbn_rectangular.setObjectName(u"rbn_rectangular")
        self.rbn_rectangular.setGeometry(QRect(110, 0, 109, 20))
        self.rbn_rectangular.setChecked(False)
        self.rbn_rectangular.setAutoExclusive(True)

        self.hl3.addWidget(self.groupBox_2)


        self.fl.setLayout(10, QFormLayout.FieldRole, self.hl3)


        self.vl.addLayout(self.fl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Chip_editor)
        self.lie_pack_pin.editingFinished.connect(Chip_editor.fill_pin_table)
        self.btn_delete_manufacturer.clicked.connect(Chip_editor.delete_cbx_element)
        self.btn_delete_type.clicked.connect(Chip_editor.delete_cbx_element)
        self.btn_delete_package.clicked.connect(Chip_editor.delete_cbx_element)
        self.cbx_package.currentIndexChanged.connect(Chip_editor.select_package)
        self.cbx_type.currentIndexChanged.connect(Chip_editor.select_type)
        self.cbx_manufacturer.currentIndexChanged.connect(Chip_editor.select_manufacturer)
        self.btn_cancel.clicked.connect(Chip_editor.close)

        QMetaObject.connectSlotsByName(Chip_editor)
    # setupUi

    def retranslateUi(self, Chip_editor):
        Chip_editor.setWindowTitle(QCoreApplication.translate("Chip_editor", u"Hardsploit - Chip editor", None))
        ___qtablewidgetitem = self.tbl_pins.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Chip_editor", u"Pin Number", None));
        ___qtablewidgetitem1 = self.tbl_pins.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Chip_editor", u"Bus", None));
        ___qtablewidgetitem2 = self.tbl_pins.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Chip_editor", u"Signal", None));
        self.lbl_advice.setText(QCoreApplication.translate("Chip_editor", u"To complete this form, please report to the component datasheet.", None))
        self.btn_cancel.setText(QCoreApplication.translate("Chip_editor", u"Cancel", None))
        self.btn_add.setText(QCoreApplication.translate("Chip_editor", u"Add", None))
        self.lbl_ref.setText(QCoreApplication.translate("Chip_editor", u"Name / Reference:", None))
        self.lie_reference.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"30 chars max", None))
        self.lbl_description.setText(QCoreApplication.translate("Chip_editor", u"Description:", None))
        self.lie_description.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"200 chars max", None))
        self.lbl_voltage.setText(QCoreApplication.translate("Chip_editor", u"Voltage:", None))
        self.groupBox.setTitle("")
        self.rbn_3v.setText(QCoreApplication.translate("Chip_editor", u"3,3V", None))
        self.rbn_5v.setText(QCoreApplication.translate("Chip_editor", u"5V", None))
        self.lbl_manu.setText(QCoreApplication.translate("Chip_editor", u"Manufacturer:", None))
        self.cbx_manufacturer.setItemText(0, QCoreApplication.translate("Chip_editor", u"Select...", None))

        self.btn_delete_manufacturer.setText(QCoreApplication.translate("Chip_editor", u"X", None))
        self.lie_manu_name.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"Other...", None))
        self.lbl_type.setText(QCoreApplication.translate("Chip_editor", u"Type:", None))
        self.cbx_type.setItemText(0, QCoreApplication.translate("Chip_editor", u"Select...", None))

        self.btn_delete_type.setText(QCoreApplication.translate("Chip_editor", u"X", None))
        self.lie_type_name.setText("")
        self.lie_type_name.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"Other...", None))
        self.lbl_package.setText(QCoreApplication.translate("Chip_editor", u"Package:", None))
        self.cbx_package.setItemText(0, QCoreApplication.translate("Chip_editor", u"Select...", None))

        self.btn_delete_package.setText(QCoreApplication.translate("Chip_editor", u"X", None))
        self.lbl_name.setText(QCoreApplication.translate("Chip_editor", u"Package name:", None))
        self.lie_pack_name.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"30 chars max", None))
        self.lbl_pack_pin.setText(QCoreApplication.translate("Chip_editor", u"Package pin number:", None))
        self.lie_pack_pin.setInputMask("")
        self.lie_pack_pin.setPlaceholderText(QCoreApplication.translate("Chip_editor", u"4-144", None))
        self.lbl_pack_shape.setText(QCoreApplication.translate("Chip_editor", u"Package shape:", None))
        self.groupBox_2.setTitle("")
        self.rbn_square.setText(QCoreApplication.translate("Chip_editor", u"Square", None))
        self.rbn_rectangular.setText(QCoreApplication.translate("Chip_editor", u"Rectangular", None))
    # retranslateUi

