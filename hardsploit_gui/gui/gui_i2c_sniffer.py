# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_i2c_sniffer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_I2c_sniffer(object):
    def setupUi(self, I2c_sniffer):
        if not I2c_sniffer.objectName():
            I2c_sniffer.setObjectName(u"I2c_sniffer")
        I2c_sniffer.resize(303, 128)
        self.horizontalLayout_2 = QHBoxLayout(I2c_sniffer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(I2c_sniffer)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.timeout = QSpinBox(I2c_sniffer)
        self.timeout.setObjectName(u"timeout")

        self.horizontalLayout.addWidget(self.timeout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_file = QLabel(I2c_sniffer)
        self.lbl_file.setObjectName(u"lbl_file")

        self.horizontalLayout_4.addWidget(self.lbl_file)

        self.btnfile = QPushButton(I2c_sniffer)
        self.btnfile.setObjectName(u"btnfile")

        self.horizontalLayout_4.addWidget(self.btnfile)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_start = QPushButton(I2c_sniffer)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(I2c_sniffer)
        self.btn_start.clicked.connect(I2c_sniffer.start)
        self.btnfile.clicked.connect(I2c_sniffer.select_file)
        self.timeout.valueChanged.connect(I2c_sniffer.timeout)

        QMetaObject.connectSlotsByName(I2c_sniffer)
    # setupUi

    def retranslateUi(self, I2c_sniffer):
        I2c_sniffer.setWindowTitle(QCoreApplication.translate("I2c_sniffer", u"Hardsploit - I2C sniffer", None))
        self.label.setText(QCoreApplication.translate("I2c_sniffer", u"Time Out (sec)", None))
        self.lbl_file.setText(QCoreApplication.translate("I2c_sniffer", u"File :", None))
        self.btnfile.setText(QCoreApplication.translate("I2c_sniffer", u"File...", None))
        self.btn_start.setText(QCoreApplication.translate("I2c_sniffer", u"Start", None))
    # retranslateUi

