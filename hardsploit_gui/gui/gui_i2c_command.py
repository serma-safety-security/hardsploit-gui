# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_i2c_command.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_I2c_command(object):
    def setupUi(self, I2c_command):
        if not I2c_command.objectName():
            I2c_command.setObjectName(u"I2c_command")
        I2c_command.setWindowModality(Qt.ApplicationModal)
        I2c_command.resize(287, 103)
        self.gridLayout = QGridLayout(I2c_command)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fl = QFormLayout()
        self.fl.setObjectName(u"fl")
        self.lbl_size = QLabel(I2c_command)
        self.lbl_size.setObjectName(u"lbl_size")

        self.fl.setWidget(0, QFormLayout.LabelRole, self.lbl_size)

        self.lie_size = QLineEdit(I2c_command)
        self.lie_size.setObjectName(u"lie_size")

        self.fl.setWidget(0, QFormLayout.FieldRole, self.lie_size)

        self.lbl_type_cmd = QLabel(I2c_command)
        self.lbl_type_cmd.setObjectName(u"lbl_type_cmd")

        self.fl.setWidget(1, QFormLayout.LabelRole, self.lbl_type_cmd)

        self.groupBox = QGroupBox(I2c_command)
        self.groupBox.setObjectName(u"groupBox")
        self.rbn_read = QRadioButton(self.groupBox)
        self.rbn_read.setObjectName(u"rbn_read")
        self.rbn_read.setGeometry(QRect(10, -4, 61, 31))
        self.rbn_read.setChecked(True)
        self.rbn_write = QRadioButton(self.groupBox)
        self.rbn_write.setObjectName(u"rbn_write")
        self.rbn_write.setGeometry(QRect(90, 0, 61, 21))

        self.fl.setWidget(1, QFormLayout.FieldRole, self.groupBox)


        self.gridLayout.addLayout(self.fl, 1, 0, 1, 1)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(I2c_command)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.bnt_new_cmd = QPushButton(I2c_command)
        self.bnt_new_cmd.setObjectName(u"bnt_new_cmd")

        self.hl.addWidget(self.bnt_new_cmd)


        self.gridLayout.addLayout(self.hl, 2, 0, 1, 1)


        self.retranslateUi(I2c_command)
        self.btn_cancel.clicked.connect(I2c_command.close)
        self.bnt_new_cmd.clicked.connect(I2c_command.open_generic_cmd)

        QMetaObject.connectSlotsByName(I2c_command)
    # setupUi

    def retranslateUi(self, I2c_command):
        I2c_command.setWindowTitle(QCoreApplication.translate("I2c_command", u"Hardsploit - I2C Command", None))
        self.lbl_size.setText(QCoreApplication.translate("I2c_command", u"Payload size:", None))
        self.lbl_type_cmd.setText(QCoreApplication.translate("I2c_command", u"Command type:", None))
        self.groupBox.setTitle("")
        self.rbn_read.setText(QCoreApplication.translate("I2c_command", u"Read", None))
        self.rbn_write.setText(QCoreApplication.translate("I2c_command", u"Write", None))
        self.btn_cancel.setText(QCoreApplication.translate("I2c_command", u"Cancel", None))
        self.bnt_new_cmd.setText(QCoreApplication.translate("I2c_command", u"Open", None))
    # retranslateUi

