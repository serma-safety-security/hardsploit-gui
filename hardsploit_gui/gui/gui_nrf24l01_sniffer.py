# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_nrf24l01_sniffer.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_NrfSniffer(object):
    def setupUi(self, NrfSniffer):
        if not NrfSniffer.objectName():
            NrfSniffer.setObjectName(u"NrfSniffer")
        NrfSniffer.setWindowModality(Qt.ApplicationModal)
        NrfSniffer.resize(562, 393)
        NrfSniffer.setMinimumSize(QSize(5, 0))
        NrfSniffer.setMaximumSize(QSize(16777211, 16777215))
        self.gridLayout = QGridLayout(NrfSniffer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_recv = QLabel(NrfSniffer)
        self.lbl_recv.setObjectName(u"lbl_recv")

        self.hl2.addWidget(self.lbl_recv)

        self.lbl_chip = QLabel(NrfSniffer)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.line = QFrame(NrfSniffer)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.hl2.addWidget(self.line)

        self.lbl_channel = QLabel(NrfSniffer)
        self.lbl_channel.setObjectName(u"lbl_channel")

        self.hl2.addWidget(self.lbl_channel)

        self.lbl_separator = QLabel(NrfSniffer)
        self.lbl_separator.setObjectName(u"lbl_separator")

        self.hl2.addWidget(self.lbl_separator)

        self.lbl_address = QLabel(NrfSniffer)
        self.lbl_address.setObjectName(u"lbl_address")

        self.hl2.addWidget(self.lbl_address)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs)


        self.vl.addLayout(self.hl2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_file = QLabel(NrfSniffer)
        self.lbl_file.setObjectName(u"lbl_file")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_file)

        self.btn_file = QPushButton(NrfSniffer)
        self.btn_file.setObjectName(u"btn_file")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btn_file)

        self.lbl_selected = QLabel(NrfSniffer)
        self.lbl_selected.setObjectName(u"lbl_selected")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_selected)

        self.lbl_selected_file = QLabel(NrfSniffer)
        self.lbl_selected_file.setObjectName(u"lbl_selected_file")
        self.lbl_selected_file.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_selected_file)


        self.vl.addLayout(self.formLayout)

        self.tree_recv = QTreeWidget(NrfSniffer)
        font = QFont()
        font.setFamilies([u"Monospace"])
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setFont(0, font);
        self.tree_recv.setHeaderItem(__qtreewidgetitem)
        self.tree_recv.setObjectName(u"tree_recv")
        self.tree_recv.setFont(font)
        self.tree_recv.setItemsExpandable(True)
        self.tree_recv.setColumnCount(3)

        self.vl.addWidget(self.tree_recv)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.btn_recv = QPushButton(NrfSniffer)
        self.btn_recv.setObjectName(u"btn_recv")
        self.btn_recv.setEnabled(True)

        self.hl.addWidget(self.btn_recv)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(NrfSniffer)
        self.btn_recv.clicked.connect(NrfSniffer.recv)
        self.btn_file.clicked.connect(NrfSniffer.select_read_file)

        QMetaObject.connectSlotsByName(NrfSniffer)
    # setupUi

    def retranslateUi(self, NrfSniffer):
        NrfSniffer.setWindowTitle(QCoreApplication.translate("NrfSniffer", u"Hardsploit - Receive", None))
        self.lbl_recv.setText(QCoreApplication.translate("NrfSniffer", u"Sniffing from", None))
        self.lbl_chip.setText(QCoreApplication.translate("NrfSniffer", u"[CHIP]", None))
        self.lbl_channel.setText(QCoreApplication.translate("NrfSniffer", u"[Channel]", None))
        self.lbl_separator.setText(QCoreApplication.translate("NrfSniffer", u"-", None))
        self.lbl_address.setText(QCoreApplication.translate("NrfSniffer", u"[Address]", None))
        self.lbl_file.setText(QCoreApplication.translate("NrfSniffer", u"Result file:", None))
        self.btn_file.setText(QCoreApplication.translate("NrfSniffer", u"File...", None))
        self.lbl_selected.setText(QCoreApplication.translate("NrfSniffer", u"Selected file:", None))
        self.lbl_selected_file.setText(QCoreApplication.translate("NrfSniffer", u"None", None))
        ___qtreewidgetitem = self.tree_recv.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("NrfSniffer", u"Ascii", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("NrfSniffer", u"Data (hex)", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("NrfSniffer", u"Frames", None));
        self.btn_recv.setText(QCoreApplication.translate("NrfSniffer", u"Receive", None))
    # retranslateUi

