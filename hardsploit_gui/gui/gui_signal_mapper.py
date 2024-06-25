# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_signal_mapper.ui'
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
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Signal_mapper(object):
    def setupUi(self, Signal_mapper):
        if not Signal_mapper.objectName():
            Signal_mapper.setObjectName(u"Signal_mapper")
        Signal_mapper.resize(268, 411)
        self.gridLayout = QGridLayout(Signal_mapper)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.lbl_bus = QLabel(Signal_mapper)
        self.lbl_bus.setObjectName(u"lbl_bus")

        self.hl.addWidget(self.lbl_bus)

        self.cbx_bus = QComboBox(Signal_mapper)
        self.cbx_bus.addItem("")
        self.cbx_bus.setObjectName(u"cbx_bus")

        self.hl.addWidget(self.cbx_bus)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)


        self.vl.addLayout(self.hl)

        self.map_table = QTableWidget(Signal_mapper)
        if (self.map_table.columnCount() < 2):
            self.map_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.map_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.map_table.setObjectName(u"map_table")
        self.map_table.horizontalHeader().setStretchLastSection(True)
        self.map_table.verticalHeader().setVisible(False)

        self.vl.addWidget(self.map_table)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs2)

        self.btn_cancel = QPushButton(Signal_mapper)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl2.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(Signal_mapper)
        self.btn_save.setObjectName(u"btn_save")

        self.hl2.addWidget(self.btn_save)


        self.vl.addLayout(self.hl2)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Signal_mapper)
        self.btn_cancel.clicked.connect(Signal_mapper.close)
        self.btn_save.clicked.connect(Signal_mapper.save_signal_mapping)
        self.cbx_bus.currentIndexChanged.connect(Signal_mapper.update_map_table)
        self.map_table.itemChanged.connect(Signal_mapper.check_mapping_value)

        QMetaObject.connectSlotsByName(Signal_mapper)
    # setupUi

    def retranslateUi(self, Signal_mapper):
        Signal_mapper.setWindowTitle(QCoreApplication.translate("Signal_mapper", u"Signal mapper", None))
        self.lbl_bus.setText(QCoreApplication.translate("Signal_mapper", u"Select a bus", None))
        self.cbx_bus.setItemText(0, QCoreApplication.translate("Signal_mapper", u"Bus...", None))

        ___qtablewidgetitem = self.map_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Signal_mapper", u"Signal Name", None));
        ___qtablewidgetitem1 = self.map_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Signal_mapper", u"Associated Pin", None));
        self.btn_cancel.setText(QCoreApplication.translate("Signal_mapper", u"Close", None))
        self.btn_save.setText(QCoreApplication.translate("Signal_mapper", u"Save", None))
    # retranslateUi

