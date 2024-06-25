# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_generic_commands.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Generic_commands(object):
    def setupUi(self, Generic_commands):
        if not Generic_commands.objectName():
            Generic_commands.setObjectName(u"Generic_commands")
        Generic_commands.setWindowModality(Qt.ApplicationModal)
        Generic_commands.resize(542, 383)
        self.actionExecute = QAction(Generic_commands)
        self.actionExecute.setObjectName(u"actionExecute")
        self.actionEdit = QAction(Generic_commands)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionTemplate = QAction(Generic_commands)
        self.actionTemplate.setObjectName(u"actionTemplate")
        self.actionDelete = QAction(Generic_commands)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionConcatenate = QAction(Generic_commands)
        self.actionConcatenate.setObjectName(u"actionConcatenate")
        self.actionExecute_n = QAction(Generic_commands)
        self.actionExecute_n.setObjectName(u"actionExecute_n")
        self.centralwidget = QWidget(Generic_commands)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.lbl_search = QLabel(self.centralwidget)
        self.lbl_search.setObjectName(u"lbl_search")

        self.hl.addWidget(self.lbl_search)

        self.lie_search = QLineEdit(self.centralwidget)
        self.lie_search.setObjectName(u"lie_search")
        self.lie_search.setMaxLength(10)

        self.hl.addWidget(self.lie_search)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.lbl_current_chip = QLabel(self.centralwidget)
        self.lbl_current_chip.setObjectName(u"lbl_current_chip")

        self.hl.addWidget(self.lbl_current_chip)

        self.lbl_chip = QLabel(self.centralwidget)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl.addWidget(self.lbl_chip)


        self.vl.addLayout(self.hl)

        self.vl2 = QVBoxLayout()
        self.vl2.setObjectName(u"vl2")
        self.tbl_cmd = QTableWidget(self.centralwidget)
        if (self.tbl_cmd.columnCount() < 2):
            self.tbl_cmd.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_cmd.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_cmd.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_cmd.setObjectName(u"tbl_cmd")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.tbl_cmd.setFont(font)
        self.tbl_cmd.setSortingEnabled(True)
        self.tbl_cmd.horizontalHeader().setVisible(True)
        self.tbl_cmd.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_cmd.horizontalHeader().setMinimumSectionSize(36)
        self.tbl_cmd.horizontalHeader().setDefaultSectionSize(110)
        self.tbl_cmd.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_cmd.horizontalHeader().setStretchLastSection(True)
        self.tbl_cmd.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_cmd.verticalHeader().setDefaultSectionSize(30)
        self.tbl_cmd.verticalHeader().setStretchLastSection(True)

        self.vl2.addWidget(self.tbl_cmd)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.vl2.addWidget(self.label)

        self.hl3 = QHBoxLayout()
        self.hl3.setObjectName(u"hl3")
        self.check_result = QCheckBox(self.centralwidget)
        self.check_result.setObjectName(u"check_result")
        self.check_result.setChecked(True)

        self.hl3.addWidget(self.check_result)

        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl3.addItem(self.hs2)

        self.btn_new_cmd = QPushButton(self.centralwidget)
        self.btn_new_cmd.setObjectName(u"btn_new_cmd")

        self.hl3.addWidget(self.btn_new_cmd)


        self.vl2.addLayout(self.hl3)


        self.vl.addLayout(self.vl2)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)

        Generic_commands.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Generic_commands)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 542, 22))
        self.menuCommandes = QMenu(self.menubar)
        self.menuCommandes.setObjectName(u"menuCommandes")
        Generic_commands.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Generic_commands)
        self.statusbar.setObjectName(u"statusbar")
        Generic_commands.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCommandes.menuAction())
        self.menuCommandes.addAction(self.actionExecute)
        self.menuCommandes.addAction(self.actionEdit)
        self.menuCommandes.addAction(self.actionTemplate)
        self.menuCommandes.addAction(self.actionDelete)
        self.menuCommandes.addAction(self.actionConcatenate)

        self.retranslateUi(Generic_commands)
        self.lie_search.textChanged.connect(Generic_commands.feed_cmd_array)
        self.btn_new_cmd.clicked.connect(Generic_commands.create)
        self.actionExecute.triggered.connect(Generic_commands.execute)
        self.actionEdit.triggered.connect(Generic_commands.edit)
        self.actionDelete.triggered.connect(Generic_commands.delete)
        self.actionTemplate.triggered.connect(Generic_commands.template)
        self.actionConcatenate.triggered.connect(Generic_commands.concatenate)
        self.actionExecute_n.triggered.connect(Generic_commands.execute_n)

        QMetaObject.connectSlotsByName(Generic_commands)
    # setupUi

    def retranslateUi(self, Generic_commands):
        Generic_commands.setWindowTitle(QCoreApplication.translate("Generic_commands", u"Hardsploit - Commands", None))
        self.actionExecute.setText(QCoreApplication.translate("Generic_commands", u"Execute", None))
        self.actionEdit.setText(QCoreApplication.translate("Generic_commands", u"Edit", None))
        self.actionTemplate.setText(QCoreApplication.translate("Generic_commands", u"Template", None))
        self.actionDelete.setText(QCoreApplication.translate("Generic_commands", u"Delete", None))
        self.actionConcatenate.setText(QCoreApplication.translate("Generic_commands", u"Concatenate", None))
        self.actionExecute_n.setText(QCoreApplication.translate("Generic_commands", u"Execute n times", None))
#if QT_CONFIG(tooltip)
        self.actionExecute_n.setToolTip(QCoreApplication.translate("Generic_commands", u"Execute a command multiple times in a raw", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_search.setText(QCoreApplication.translate("Generic_commands", u"Search", None))
        self.lie_search.setInputMask("")
        self.lbl_current_chip.setText(QCoreApplication.translate("Generic_commands", u"Current chip:", None))
        self.lbl_chip.setText(QCoreApplication.translate("Generic_commands", u"[CHIP]", None))
        ___qtablewidgetitem = self.tbl_cmd.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Generic_commands", u"Name", None));
        ___qtablewidgetitem1 = self.tbl_cmd.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Generic_commands", u"Description", None));
        self.label.setText(QCoreApplication.translate("Generic_commands", u"Right click on a command to open the menu", None))
        self.check_result.setText(QCoreApplication.translate("Generic_commands", u"Show command result", None))
        self.btn_new_cmd.setText(QCoreApplication.translate("Generic_commands", u"New Command", None))
        self.menuCommandes.setTitle(QCoreApplication.translate("Generic_commands", u"Commandes...", None))
    # retranslateUi

