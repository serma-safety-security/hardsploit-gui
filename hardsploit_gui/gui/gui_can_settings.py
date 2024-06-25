# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_can_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_CAN_settings(object):
    def setupUi(self, CAN_settings):
        if not CAN_settings.objectName():
            CAN_settings.setObjectName(u"CAN_settings")
        CAN_settings.setWindowModality(Qt.WindowModal)
        CAN_settings.resize(370, 290)
        self.gridLayout = QGridLayout(CAN_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(CAN_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.lbl_can = QLabel(CAN_settings)
        self.lbl_can.setObjectName(u"lbl_can")

        self.horizontalLayout_2.addWidget(self.lbl_can)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setVerticalSpacing(6)
        self.label = QLabel(CAN_settings)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lie_baud_rate = QLineEdit(CAN_settings)
        self.lie_baud_rate.setObjectName(u"lie_baud_rate")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_baud_rate)

        self.label_8 = QLabel(CAN_settings)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.pushButton_autodetection = QPushButton(CAN_settings)
        self.pushButton_autodetection.setObjectName(u"pushButton_autodetection")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_autodetection)

        self.label_2 = QLabel(CAN_settings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lie_crc_polynom = QLineEdit(CAN_settings)
        self.lie_crc_polynom.setObjectName(u"lie_crc_polynom")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lie_crc_polynom)

        self.label_3 = QLabel(CAN_settings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lie_crc_type = QLineEdit(CAN_settings)
        self.lie_crc_type.setObjectName(u"lie_crc_type")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lie_crc_type)

        self.label_4 = QLabel(CAN_settings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lie_id = QLineEdit(CAN_settings)
        self.lie_id.setObjectName(u"lie_id")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lie_id)

        self.label_7 = QLabel(CAN_settings)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rbn_standard = QRadioButton(CAN_settings)
        self.rbn_standard.setObjectName(u"rbn_standard")
        self.rbn_standard.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rbn_standard)

        self.rbn_extended = QRadioButton(CAN_settings)
        self.rbn_extended.setObjectName(u"rbn_extended")

        self.horizontalLayout_3.addWidget(self.rbn_extended)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(CAN_settings)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.pushButton_save = QPushButton(CAN_settings)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(CAN_settings)
        self.pushButton_save.clicked.connect(CAN_settings.save_settings)
        self.pushButton_cancel.clicked.connect(CAN_settings.close)
        self.pushButton_autodetection.clicked.connect(CAN_settings.autodetect)

        QMetaObject.connectSlotsByName(CAN_settings)
    # setupUi

    def retranslateUi(self, CAN_settings):
        CAN_settings.setWindowTitle(QCoreApplication.translate("CAN_settings", u"Hardsploit - CAN settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("CAN_settings", u"[CHIP]", None))
        self.lbl_can.setText(QCoreApplication.translate("CAN_settings", u"CAN settings", None))
        self.label.setText(QCoreApplication.translate("CAN_settings", u"Baud rate (manual):", None))
        self.lie_baud_rate.setText("")
        self.lie_baud_rate.setPlaceholderText(QCoreApplication.translate("CAN_settings", u"Bits par seconde", None))
        self.label_8.setText(QCoreApplication.translate("CAN_settings", u"Baud rate (auto):", None))
        self.pushButton_autodetection.setText(QCoreApplication.translate("CAN_settings", u"Autodetection", None))
        self.label_2.setText(QCoreApplication.translate("CAN_settings", u"CRC polynom:", None))
        self.lie_crc_polynom.setText("")
        self.lie_crc_polynom.setPlaceholderText(QCoreApplication.translate("CAN_settings", u"Decimal value", None))
        self.label_3.setText(QCoreApplication.translate("CAN_settings", u"CRC type:", None))
        self.lie_crc_type.setPlaceholderText(QCoreApplication.translate("CAN_settings", u"Decimal value", None))
        self.label_4.setText(QCoreApplication.translate("CAN_settings", u"ID:", None))
        self.lie_id.setPlaceholderText(QCoreApplication.translate("CAN_settings", u"Hexadecimal value", None))
        self.label_7.setText(QCoreApplication.translate("CAN_settings", u"Frame format:", None))
        self.rbn_standard.setText(QCoreApplication.translate("CAN_settings", u"Standard", None))
        self.rbn_extended.setText(QCoreApplication.translate("CAN_settings", u"Extended", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("CAN_settings", u"Cancel", None))
        self.pushButton_save.setText(QCoreApplication.translate("CAN_settings", u"Save", None))
    # retranslateUi

