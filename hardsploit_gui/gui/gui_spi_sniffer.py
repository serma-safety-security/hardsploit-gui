# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_spi_sniffer.ui'
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
    QHeaderView, QLayout, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Spi_sniffer(object):
    def setupUi(self, Spi_sniffer):
        if not Spi_sniffer.objectName():
            Spi_sniffer.setObjectName(u"Spi_sniffer")
        Spi_sniffer.resize(435, 604)
        self.gridLayout = QGridLayout(Spi_sniffer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_start = QPushButton(Spi_sniffer)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout.addWidget(self.btn_start)

        self.cbx_type = QComboBox(Spi_sniffer)
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.addItem("")
        self.cbx_type.setObjectName(u"cbx_type")

        self.horizontalLayout.addWidget(self.cbx_type)

        self.btn_stop = QPushButton(Spi_sniffer)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_stop)

        self.btn_close = QPushButton(Spi_sniffer)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tbl_result = QTableWidget(Spi_sniffer)
        if (self.tbl_result.columnCount() < 5):
            self.tbl_result.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_result.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tbl_result.setObjectName(u"tbl_result")
        self.tbl_result.setSortingEnabled(True)
        self.tbl_result.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_result.horizontalHeader().setMinimumSectionSize(25)
        self.tbl_result.horizontalHeader().setDefaultSectionSize(80)
        self.tbl_result.horizontalHeader().setHighlightSections(True)
        self.tbl_result.horizontalHeader().setStretchLastSection(True)
        self.tbl_result.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tbl_result)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Spi_sniffer)
        self.btn_close.clicked.connect(Spi_sniffer.close)
        self.btn_start.clicked.connect(Spi_sniffer.start)
        self.btn_stop.clicked.connect(Spi_sniffer.stop)

        QMetaObject.connectSlotsByName(Spi_sniffer)
    # setupUi

    def retranslateUi(self, Spi_sniffer):
        Spi_sniffer.setWindowTitle(QCoreApplication.translate("Spi_sniffer", u"Hardsploit - SPI sniffer", None))
        self.btn_start.setText(QCoreApplication.translate("Spi_sniffer", u"Start", None))
        self.cbx_type.setItemText(0, QCoreApplication.translate("Spi_sniffer", u"Both", None))
        self.cbx_type.setItemText(1, QCoreApplication.translate("Spi_sniffer", u"MOSI", None))
        self.cbx_type.setItemText(2, QCoreApplication.translate("Spi_sniffer", u"MISO", None))

        self.btn_stop.setText(QCoreApplication.translate("Spi_sniffer", u"Stop", None))
        self.btn_close.setText(QCoreApplication.translate("Spi_sniffer", u"Close", None))
        ___qtablewidgetitem = self.tbl_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Spi_sniffer", u"Number", None));
        ___qtablewidgetitem1 = self.tbl_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Spi_sniffer", u"MOSI", None));
        ___qtablewidgetitem2 = self.tbl_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Spi_sniffer", u"ASCII", None));
        ___qtablewidgetitem3 = self.tbl_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Spi_sniffer", u"MISO", None));
        ___qtablewidgetitem4 = self.tbl_result.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Spi_sniffer", u"ASCII", None));
    # retranslateUi

