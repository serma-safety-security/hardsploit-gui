# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_signal_scanner.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Signal_scanner(object):
    def setupUi(self, Signal_scanner):
        if not Signal_scanner.objectName():
            Signal_scanner.setObjectName(u"Signal_scanner")
        Signal_scanner.setWindowModality(Qt.ApplicationModal)
        Signal_scanner.resize(259, 368)
        self.gridLayout = QGridLayout(Signal_scanner)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_nbr_pin = QLabel(Signal_scanner)
        self.lbl_nbr_pin.setObjectName(u"lbl_nbr_pin")

        self.horizontalLayout_2.addWidget(self.lbl_nbr_pin)

        self.cbx_start = QComboBox(Signal_scanner)
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.addItem("")
        self.cbx_start.setObjectName(u"cbx_start")
        self.cbx_start.setMinimumSize(QSize(50, 0))
        self.cbx_start.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.cbx_start)

        self.label = QLabel(Signal_scanner)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 0))
        self.label.setMaximumSize(QSize(20, 16777215))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.cbx_stop = QComboBox(Signal_scanner)
        self.cbx_stop.setObjectName(u"cbx_stop")
        self.cbx_stop.setMinimumSize(QSize(50, 0))
        self.cbx_stop.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.cbx_stop)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tbl_result = QTableWidget(Signal_scanner)
        if (self.tbl_result.columnCount() < 2):
            self.tbl_result.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_result.setObjectName(u"tbl_result")
        self.tbl_result.horizontalHeader().setStretchLastSection(True)
        self.tbl_result.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tbl_result)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_scan = QPushButton(Signal_scanner)
        self.btn_scan.setObjectName(u"btn_scan")

        self.horizontalLayout.addWidget(self.btn_scan)

        self.btn_autowiring = QPushButton(Signal_scanner)
        self.btn_autowiring.setObjectName(u"btn_autowiring")

        self.horizontalLayout.addWidget(self.btn_autowiring)

        self.btn_close = QPushButton(Signal_scanner)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Signal_scanner)
        self.btn_close.clicked.connect(Signal_scanner.close)
        self.btn_scan.clicked.connect(Signal_scanner.scan)
        self.btn_autowiring.clicked.connect(Signal_scanner.autowiring)
        self.cbx_start.currentIndexChanged.connect(Signal_scanner.update_cbx)
        self.cbx_stop.currentIndexChanged.connect(Signal_scanner.update_tbl)

        QMetaObject.connectSlotsByName(Signal_scanner)
    # setupUi

    def retranslateUi(self, Signal_scanner):
        Signal_scanner.setWindowTitle(QCoreApplication.translate("Signal_scanner", u"Hardsploit - Scanner", None))
        self.lbl_nbr_pin.setText(QCoreApplication.translate("Signal_scanner", u"Pin used:", None))
        self.cbx_start.setItemText(0, QCoreApplication.translate("Signal_scanner", u"B0", None))
        self.cbx_start.setItemText(1, QCoreApplication.translate("Signal_scanner", u"B1", None))
        self.cbx_start.setItemText(2, QCoreApplication.translate("Signal_scanner", u"B2", None))
        self.cbx_start.setItemText(3, QCoreApplication.translate("Signal_scanner", u"B3", None))
        self.cbx_start.setItemText(4, QCoreApplication.translate("Signal_scanner", u"B4", None))
        self.cbx_start.setItemText(5, QCoreApplication.translate("Signal_scanner", u"B5", None))
        self.cbx_start.setItemText(6, QCoreApplication.translate("Signal_scanner", u"B6", None))

        self.label.setText(QCoreApplication.translate("Signal_scanner", u"to", None))
        ___qtablewidgetitem = self.tbl_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Signal_scanner", u"Hardsploit PIN", None));
        ___qtablewidgetitem1 = self.tbl_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Signal_scanner", u"Signal found", None));
        self.btn_scan.setText(QCoreApplication.translate("Signal_scanner", u"Scan", None))
        self.btn_autowiring.setText(QCoreApplication.translate("Signal_scanner", u"Autowiring", None))
        self.btn_close.setText(QCoreApplication.translate("Signal_scanner", u"Close", None))
    # retranslateUi

