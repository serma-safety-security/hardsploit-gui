# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_can_baudrate.ui'
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

class Ui_Can_baudrate(object):
    def setupUi(self, Can_baudrate):
        if not Can_baudrate.objectName():
            Can_baudrate.setObjectName(u"Can_baudrate")
        Can_baudrate.resize(339, 134)
        self.gridLayout = QGridLayout(Can_baudrate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_tip = QLabel(Can_baudrate)
        self.lbl_tip.setObjectName(u"lbl_tip")

        self.verticalLayout.addWidget(self.lbl_tip)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_start = QPushButton(Can_baudrate)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(Can_baudrate)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_baudrate = QLabel(Can_baudrate)
        self.lbl_baudrate.setObjectName(u"lbl_baudrate")

        self.verticalLayout.addWidget(self.lbl_baudrate)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Can_baudrate)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.btn_close = QPushButton(Can_baudrate)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Can_baudrate)
        self.btn_start.clicked.connect(Can_baudrate.start_detect)
        self.btn_stop.clicked.connect(Can_baudrate.stop_detect)
        self.btn_close.clicked.connect(Can_baudrate.close)
        self.pushButton.clicked.connect(Can_baudrate.copy)

        QMetaObject.connectSlotsByName(Can_baudrate)
    # setupUi

    def retranslateUi(self, Can_baudrate):
        Can_baudrate.setWindowTitle(QCoreApplication.translate("Can_baudrate", u"Hardsploit - Baudrate autodetect", None))
        self.lbl_tip.setText(QCoreApplication.translate("Can_baudrate", u"Push \"Start\", restart your target then click \"Stop\"", None))
        self.btn_start.setText(QCoreApplication.translate("Can_baudrate", u"Start", None))
        self.btn_stop.setText(QCoreApplication.translate("Can_baudrate", u"Stop", None))
        self.lbl_baudrate.setText(QCoreApplication.translate("Can_baudrate", u"Baud rate detected:", None))
        self.pushButton.setText(QCoreApplication.translate("Can_baudrate", u"Copy to settings", None))
        self.btn_close.setText(QCoreApplication.translate("Can_baudrate", u"Close", None))
    # retranslateUi

