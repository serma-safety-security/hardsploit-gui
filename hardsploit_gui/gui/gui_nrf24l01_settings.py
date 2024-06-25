# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_nrf24l01_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_NRF24L01_settings(object):
    def setupUi(self, NRF24L01_settings):
        if not NRF24L01_settings.objectName():
            NRF24L01_settings.setObjectName(u"NRF24L01_settings")
        NRF24L01_settings.setWindowModality(Qt.WindowModal)
        NRF24L01_settings.resize(319, 187)
        self.gridLayout = QGridLayout(NRF24L01_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(NRF24L01_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.lbl_nrf = QLabel(NRF24L01_settings)
        self.lbl_nrf.setObjectName(u"lbl_nrf")

        self.horizontalLayout_2.addWidget(self.lbl_nrf)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_chan = QLabel(NRF24L01_settings)
        self.label_chan.setObjectName(u"label_chan")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_chan)

        self.spin_chan = QSpinBox(NRF24L01_settings)
        self.spin_chan.setObjectName(u"spin_chan")
        self.spin_chan.setMaximum(126)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spin_chan)

        self.lbl_addr = QLabel(NRF24L01_settings)
        self.lbl_addr.setObjectName(u"lbl_addr")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_addr)

        self.lie_addr = QLineEdit(NRF24L01_settings)
        self.lie_addr.setObjectName(u"lie_addr")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_addr)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.line = QFrame(NRF24L01_settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(NRF24L01_settings)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(NRF24L01_settings)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(NRF24L01_settings)
        self.pushButton.clicked.connect(NRF24L01_settings.save_settings)
        self.pushButton_2.clicked.connect(NRF24L01_settings.close)

        QMetaObject.connectSlotsByName(NRF24L01_settings)
    # setupUi

    def retranslateUi(self, NRF24L01_settings):
        NRF24L01_settings.setWindowTitle(QCoreApplication.translate("NRF24L01_settings", u"Hardsploit - UART settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("NRF24L01_settings", u"[CHIP]", None))
        self.lbl_nrf.setText(QCoreApplication.translate("NRF24L01_settings", u"NRF24L01 settings", None))
        self.label_chan.setText(QCoreApplication.translate("NRF24L01_settings", u"Channel", None))
        self.lbl_addr.setText(QCoreApplication.translate("NRF24L01_settings", u"Address", None))
        self.lie_addr.setInputMask(QCoreApplication.translate("NRF24L01_settings", u"0xHHHHHHHHHH", None))
        self.lie_addr.setText("")
        self.lie_addr.setPlaceholderText(QCoreApplication.translate("NRF24L01_settings", u"0x1234ABCD", None))
        self.pushButton_2.setText(QCoreApplication.translate("NRF24L01_settings", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("NRF24L01_settings", u"Save", None))
    # retranslateUi

