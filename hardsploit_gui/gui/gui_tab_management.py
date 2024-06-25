# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_tab_management.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Tab_management(object):
    def setupUi(self, Tab_management):
        if not Tab_management.objectName():
            Tab_management.setObjectName(u"Tab_management")
        Tab_management.resize(710, 589)
        Tab_management.setMinimumSize(QSize(710, 450))
        self.gridLayout = QGridLayout(Tab_management)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hl_main = QHBoxLayout()
        self.hl_main.setObjectName(u"hl_main")
        self.tw_chip = QTreeWidget(Tab_management)
        self.tw_chip.setObjectName(u"tw_chip")
        self.tw_chip.setMinimumSize(QSize(200, 0))
        self.tw_chip.setMaximumSize(QSize(150, 16777215))

        self.hl_main.addWidget(self.tw_chip)

        self.vl_body = QVBoxLayout()
        self.vl_body.setObjectName(u"vl_body")
        self.hl_filters = QHBoxLayout()
        self.hl_filters.setObjectName(u"hl_filters")
        self.img_search = QLabel(Tab_management)
        self.img_search.setObjectName(u"img_search")

        self.hl_filters.addWidget(self.img_search)

        self.lie_search = QLineEdit(Tab_management)
        self.lie_search.setObjectName(u"lie_search")

        self.hl_filters.addWidget(self.lie_search)

        self.cbx_manufacturer = QComboBox(Tab_management)
        self.cbx_manufacturer.addItem("")
        self.cbx_manufacturer.setObjectName(u"cbx_manufacturer")
        self.cbx_manufacturer.setMinimumSize(QSize(87, 0))
        self.cbx_manufacturer.setMaximumSize(QSize(16777215, 16777215))

        self.hl_filters.addWidget(self.cbx_manufacturer)

        self.cbx_type = QComboBox(Tab_management)
        self.cbx_type.addItem("")
        self.cbx_type.setObjectName(u"cbx_type")
        self.cbx_type.setMinimumSize(QSize(87, 0))
        self.cbx_type.setMaximumSize(QSize(100, 16777215))

        self.hl_filters.addWidget(self.cbx_type)


        self.vl_body.addLayout(self.hl_filters)

        self.vl_array = QVBoxLayout()
        self.vl_array.setObjectName(u"vl_array")
        self.tbl_chip = QTableWidget(Tab_management)
        if (self.tbl_chip.columnCount() < 4):
            self.tbl_chip.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_chip.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_chip.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_chip.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_chip.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_chip.setObjectName(u"tbl_chip")
        self.tbl_chip.horizontalHeader().setStretchLastSection(True)
        self.tbl_chip.verticalHeader().setStretchLastSection(True)

        self.vl_array.addWidget(self.tbl_chip)


        self.vl_body.addLayout(self.vl_array)

        self.hl_options = QHBoxLayout()
        self.hl_options.setObjectName(u"hl_options")
        self.lbl_info = QLabel(Tab_management)
        self.lbl_info.setObjectName(u"lbl_info")

        self.hl_options.addWidget(self.lbl_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl_options.addItem(self.horizontalSpacer)

        self.btn_add = QPushButton(Tab_management)
        self.btn_add.setObjectName(u"btn_add")

        self.hl_options.addWidget(self.btn_add)


        self.vl_body.addLayout(self.hl_options)


        self.hl_main.addLayout(self.vl_body)


        self.gridLayout.addLayout(self.hl_main, 2, 0, 1, 1)

        self.tbl_console = QTableWidget(Tab_management)
        if (self.tbl_console.columnCount() < 2):
            self.tbl_console.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_console.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_console.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tbl_console.setObjectName(u"tbl_console")
        self.tbl_console.setMinimumSize(QSize(0, 100))
        self.tbl_console.setMaximumSize(QSize(16777215, 100))
        self.tbl_console.horizontalHeader().setStretchLastSection(True)
        self.tbl_console.verticalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tbl_console, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_show_console = QPushButton(Tab_management)
        self.btn_show_console.setObjectName(u"btn_show_console")
        self.btn_show_console.setCheckable(True)
        self.btn_show_console.setChecked(True)

        self.horizontalLayout.addWidget(self.btn_show_console)

        self.btn_clear_console = QPushButton(Tab_management)
        self.btn_clear_console.setObjectName(u"btn_clear_console")

        self.horizontalLayout.addWidget(self.btn_clear_console)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)


        self.retranslateUi(Tab_management)
        self.tbl_chip.cellDoubleClicked.connect(Tab_management.load_tree)
        self.lie_search.textEdited.connect(Tab_management.feed_chip_array)
        self.cbx_manufacturer.currentIndexChanged.connect(Tab_management.feed_chip_array)
        self.cbx_type.currentIndexChanged.connect(Tab_management.feed_chip_array)
        self.btn_add.clicked.connect(Tab_management.add_chip)
        self.tw_chip.itemDoubleClicked.connect(Tab_management.load_chip_action)
        self.btn_clear_console.clicked.connect(self.tbl_console.clearContents)
        self.btn_show_console.toggled.connect(Tab_management.console_view)

        QMetaObject.connectSlotsByName(Tab_management)
    # setupUi

    def retranslateUi(self, Tab_management):
        Tab_management.setWindowTitle(QCoreApplication.translate("Tab_management", u"Hardsploit - Tab management", None))
        ___qtreewidgetitem = self.tw_chip.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Tab_management", u"Current chip", None));
        self.img_search.setText(QCoreApplication.translate("Tab_management", u"Search", None))
        self.cbx_manufacturer.setItemText(0, QCoreApplication.translate("Tab_management", u"Manufacturer...", None))

        self.cbx_type.setItemText(0, QCoreApplication.translate("Tab_management", u"Type...", None))

        ___qtablewidgetitem = self.tbl_chip.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tab_management", u"Reference", None));
        ___qtablewidgetitem1 = self.tbl_chip.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tab_management", u"Type", None));
        ___qtablewidgetitem2 = self.tbl_chip.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tab_management", u"Manufacturer", None));
        ___qtablewidgetitem3 = self.tbl_chip.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tab_management", u"BUS", None));
        self.lbl_info.setText(QCoreApplication.translate("Tab_management", u"Double click a chip reference to load it", None))
        self.btn_add.setText(QCoreApplication.translate("Tab_management", u"Create component", None))
        ___qtablewidgetitem4 = self.tbl_console.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tab_management", u"Date / Time", None));
        ___qtablewidgetitem5 = self.tbl_console.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Tab_management", u"Message", None));
        self.btn_show_console.setText(QCoreApplication.translate("Tab_management", u"Console", None))
        self.btn_clear_console.setText(QCoreApplication.translate("Tab_management", u"Clear", None))
    # retranslateUi

