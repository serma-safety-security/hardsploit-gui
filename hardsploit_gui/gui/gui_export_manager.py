# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_export_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Export_manager(object):
    def setupUi(self, Export_manager):
        if not Export_manager.objectName():
            Export_manager.setObjectName(u"Export_manager")
        Export_manager.setWindowModality(Qt.ApplicationModal)
        Export_manager.resize(289, 601)
        self.horizontalLayout_2 = QHBoxLayout(Export_manager)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_result = QLabel(Export_manager)
        self.lbl_result.setObjectName(u"lbl_result")
        self.lbl_result.setMinimumSize(QSize(241, 16))
        self.lbl_result.setMaximumSize(QSize(240, 16))

        self.verticalLayout.addWidget(self.lbl_result)

        self.tbl_result = QTableWidget(Export_manager)
        self.tbl_result.setObjectName(u"tbl_result")
        self.tbl_result.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tbl_result.horizontalHeader().setDefaultSectionSize(100)
        self.tbl_result.horizontalHeader().setProperty("showSortIndicator", False)
        self.tbl_result.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tbl_result)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cbx_export = QComboBox(Export_manager)
        self.cbx_export.addItem("")
        self.cbx_export.addItem("")
        self.cbx_export.setObjectName(u"cbx_export")

        self.horizontalLayout.addWidget(self.cbx_export)

        self.btn_save = QPushButton(Export_manager)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Export_manager)
        self.btn_save.clicked.connect(Export_manager.save_result)

        QMetaObject.connectSlotsByName(Export_manager)
    # setupUi

    def retranslateUi(self, Export_manager):
        Export_manager.setWindowTitle(QCoreApplication.translate("Export_manager", u"Hardsploit - Export", None))
        self.lbl_result.setText(QCoreApplication.translate("Export_manager", u"Command result:", None))
        self.cbx_export.setItemText(0, QCoreApplication.translate("Export_manager", u"Debug (CSV file)", None))
        self.cbx_export.setItemText(1, QCoreApplication.translate("Export_manager", u"Data only (Read)", None))

        self.btn_save.setText(QCoreApplication.translate("Export_manager", u"Save...", None))
    # retranslateUi

