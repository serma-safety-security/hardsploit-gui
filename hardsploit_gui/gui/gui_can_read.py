# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_can_read.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Can_read(object):
    def setupUi(self, Can_read):
        if not Can_read.objectName():
            Can_read.setObjectName(u"Can_read")
        Can_read.setWindowModality(Qt.ApplicationModal)
        Can_read.resize(292, 149)
        Can_read.setMinimumSize(QSize(5, 0))
        Can_read.setMaximumSize(QSize(16777211, 16777215))
        self.gridLayout = QGridLayout(Can_read)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lie_result = QLineEdit(Can_read)
        self.lie_result.setObjectName(u"lie_result")
        self.lie_result.setEnabled(True)
        self.lie_result.setReadOnly(True)
        self.lie_result.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout_2.addWidget(self.lie_result, 3, 1, 1, 1)

        self.label = QLabel(Can_read)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.lbl_data_size = QLabel(Can_read)
        self.lbl_data_size.setObjectName(u"lbl_data_size")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_data_size)

        self.lie_data_size = QLineEdit(Can_read)
        self.lie_data_size.setObjectName(u"lie_data_size")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lie_data_size)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 2)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_read = QLabel(Can_read)
        self.lbl_read.setObjectName(u"lbl_read")

        self.hl2.addWidget(self.lbl_read)

        self.lbl_chip = QLabel(Can_read)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs)


        self.gridLayout_2.addLayout(self.hl2, 0, 0, 1, 2)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.btn_read = QPushButton(Can_read)
        self.btn_read.setObjectName(u"btn_read")
        self.btn_read.setEnabled(True)

        self.hl.addWidget(self.btn_read)


        self.gridLayout_2.addLayout(self.hl, 2, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Can_read)
        self.btn_read.clicked.connect(Can_read.read)

        QMetaObject.connectSlotsByName(Can_read)
    # setupUi

    def retranslateUi(self, Can_read):
        Can_read.setWindowTitle(QCoreApplication.translate("Can_read", u"Hardsploit - CAN read", None))
        self.lie_result.setPlaceholderText(QCoreApplication.translate("Can_read", u"reading result (hexadecimal)", None))
        self.label.setText(QCoreApplication.translate("Can_read", u"Result :", None))
        self.lbl_data_size.setText(QCoreApplication.translate("Can_read", u"Data size (bytes):", None))
        self.lie_data_size.setPlaceholderText(QCoreApplication.translate("Can_read", u"decimal value", None))
        self.lbl_read.setText(QCoreApplication.translate("Can_read", u"Read from", None))
        self.lbl_chip.setText(QCoreApplication.translate("Can_read", u"[CHIP]", None))
        self.btn_read.setText(QCoreApplication.translate("Can_read", u"Read", None))
    # retranslateUi

