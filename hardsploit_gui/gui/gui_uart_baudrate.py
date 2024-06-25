# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_uart_baudrate.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Uart_baudrate(object):
    def setupUi(self, Uart_baudrate):
        if not Uart_baudrate.objectName():
            Uart_baudrate.setObjectName(u"Uart_baudrate")
        Uart_baudrate.resize(259, 114)
        self.gridLayout = QGridLayout(Uart_baudrate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_tip = QLabel(Uart_baudrate)
        self.lbl_tip.setObjectName(u"lbl_tip")

        self.verticalLayout.addWidget(self.lbl_tip)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_start = QPushButton(Uart_baudrate)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(Uart_baudrate)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_baudrate = QLabel(Uart_baudrate)
        self.lbl_baudrate.setObjectName(u"lbl_baudrate")

        self.verticalLayout.addWidget(self.lbl_baudrate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Uart_baudrate)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.btn_close = QPushButton(Uart_baudrate)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Uart_baudrate)
        self.btn_start.clicked.connect(Uart_baudrate.start_detect)
        self.btn_stop.clicked.connect(Uart_baudrate.stop_detect)
        self.btn_close.clicked.connect(Uart_baudrate.close)
        self.pushButton.clicked.connect(Uart_baudrate.copy)

        QMetaObject.connectSlotsByName(Uart_baudrate)
    # setupUi

    def retranslateUi(self, Uart_baudrate):
        Uart_baudrate.setWindowTitle(QCoreApplication.translate("Uart_baudrate", u"Hardsploit - Baudrate autodetect", None))
        self.lbl_tip.setText(QCoreApplication.translate("Uart_baudrate", u"Push \"Start\", restart your target then click \"Stop\"", None))
        self.btn_start.setText(QCoreApplication.translate("Uart_baudrate", u"Start", None))
        self.btn_stop.setText(QCoreApplication.translate("Uart_baudrate", u"Stop", None))
        self.lbl_baudrate.setText(QCoreApplication.translate("Uart_baudrate", u"Baud rate detected:", None))
        self.pushButton.setText(QCoreApplication.translate("Uart_baudrate", u"Copy to settings", None))
        self.btn_close.setText(QCoreApplication.translate("Uart_baudrate", u"Close", None))
    # retranslateUi

