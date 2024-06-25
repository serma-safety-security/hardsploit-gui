# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_can_sniffer.ui'
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

class Ui_CAN_sniffer(object):
    def setupUi(self, CAN_sniffer):
        if not CAN_sniffer.objectName():
            CAN_sniffer.setObjectName(u"CAN_sniffer")
        CAN_sniffer.resize(335, 158)
        self.horizontalLayout_2 = QHBoxLayout(CAN_sniffer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CAN_sniffer)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.timeout = QSpinBox(CAN_sniffer)
        self.timeout.setObjectName(u"timeout")

        self.horizontalLayout.addWidget(self.timeout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_file = QLabel(CAN_sniffer)
        self.lbl_file.setObjectName(u"lbl_file")

        self.horizontalLayout_4.addWidget(self.lbl_file)

        self.btnfile = QPushButton(CAN_sniffer)
        self.btnfile.setObjectName(u"btnfile")

        self.horizontalLayout_4.addWidget(self.btnfile)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_start = QPushButton(CAN_sniffer)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_start)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(CAN_sniffer)
        self.btn_start.clicked.connect(CAN_sniffer.start)
        self.btnfile.clicked.connect(CAN_sniffer.select_file)
        self.timeout.valueChanged.connect(CAN_sniffer.timeout)

        QMetaObject.connectSlotsByName(CAN_sniffer)
    # setupUi

    def retranslateUi(self, CAN_sniffer):
        CAN_sniffer.setWindowTitle(QCoreApplication.translate("CAN_sniffer", u"Hardsploit - CAN sniffer", None))
        self.label.setText(QCoreApplication.translate("CAN_sniffer", u"Time Out (sec)", None))
        self.lbl_file.setText(QCoreApplication.translate("CAN_sniffer", u"File :", None))
        self.btnfile.setText(QCoreApplication.translate("CAN_sniffer", u"File...", None))
        self.btn_start.setText(QCoreApplication.translate("CAN_sniffer", u"Start", None))
    # retranslateUi

