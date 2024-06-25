# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_nrf24l01_scan.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_NRF24L01_scan(object):
    def setupUi(self, NRF24L01_scan):
        if not NRF24L01_scan.objectName():
            NRF24L01_scan.setObjectName(u"NRF24L01_scan")
        NRF24L01_scan.setWindowModality(Qt.WindowModal)
        NRF24L01_scan.resize(319, 420)
        self.gridLayout = QGridLayout(NRF24L01_scan)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(NRF24L01_scan)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.lbl_nrf = QLabel(NRF24L01_scan)
        self.lbl_nrf.setObjectName(u"lbl_nrf")

        self.horizontalLayout_2.addWidget(self.lbl_nrf)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_addr = QLabel(NRF24L01_scan)
        self.lbl_addr.setObjectName(u"lbl_addr")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_addr)

        self.lie_addr = QLineEdit(NRF24L01_scan)
        self.lie_addr.setObjectName(u"lie_addr")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lie_addr)

        self.lbl_min_chan = QLabel(NRF24L01_scan)
        self.lbl_min_chan.setObjectName(u"lbl_min_chan")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_min_chan)

        self.spin_min_chan = QSpinBox(NRF24L01_scan)
        self.spin_min_chan.setObjectName(u"spin_min_chan")
        self.spin_min_chan.setMaximum(126)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spin_min_chan)

        self.lbl_max_chan = QLabel(NRF24L01_scan)
        self.lbl_max_chan.setObjectName(u"lbl_max_chan")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_max_chan)

        self.spin_max_chan = QSpinBox(NRF24L01_scan)
        self.spin_max_chan.setObjectName(u"spin_max_chan")
        self.spin_max_chan.setMaximum(126)
        self.spin_max_chan.setValue(126)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spin_max_chan)

        self.lbl_time_step = QLabel(NRF24L01_scan)
        self.lbl_time_step.setObjectName(u"lbl_time_step")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_time_step)

        self.dspin_time_step = QDoubleSpinBox(NRF24L01_scan)
        self.dspin_time_step.setObjectName(u"dspin_time_step")
        self.dspin_time_step.setMaximum(120.000000000000000)
        self.dspin_time_step.setSingleStep(0.500000000000000)
        self.dspin_time_step.setValue(1.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dspin_time_step)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.btn_scan = QPushButton(NRF24L01_scan)
        self.btn_scan.setObjectName(u"btn_scan")

        self.verticalLayout_2.addWidget(self.btn_scan)

        self.list_scan = QListWidget(NRF24L01_scan)
        self.list_scan.setObjectName(u"list_scan")

        self.verticalLayout_2.addWidget(self.list_scan)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(NRF24L01_scan)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(NRF24L01_scan)
        self.btn_close.clicked.connect(NRF24L01_scan.close)

        QMetaObject.connectSlotsByName(NRF24L01_scan)
    # setupUi

    def retranslateUi(self, NRF24L01_scan):
        NRF24L01_scan.setWindowTitle(QCoreApplication.translate("NRF24L01_scan", u"Hardsploit - UART settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("NRF24L01_scan", u"[CHIP]", None))
        self.lbl_nrf.setText(QCoreApplication.translate("NRF24L01_scan", u"NRF24L01 Channel Scan", None))
        self.lbl_addr.setText(QCoreApplication.translate("NRF24L01_scan", u"Address", None))
        self.lie_addr.setInputMask(QCoreApplication.translate("NRF24L01_scan", u"0xHHHHHHHHHH", None))
        self.lie_addr.setText("")
        self.lie_addr.setPlaceholderText(QCoreApplication.translate("NRF24L01_scan", u"0x1234ABCD", None))
        self.lbl_min_chan.setText(QCoreApplication.translate("NRF24L01_scan", u"From channel", None))
        self.lbl_max_chan.setText(QCoreApplication.translate("NRF24L01_scan", u"To channel", None))
        self.lbl_time_step.setText(QCoreApplication.translate("NRF24L01_scan", u"Channel sniffing time (s)", None))
        self.btn_scan.setText(QCoreApplication.translate("NRF24L01_scan", u"Scan", None))
        self.btn_close.setText(QCoreApplication.translate("NRF24L01_scan", u"Close", None))
    # retranslateUi

