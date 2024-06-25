# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_command_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Command_editor(object):
    def setupUi(self, Command_editor):
        if not Command_editor.objectName():
            Command_editor.setObjectName(u"Command_editor")
        Command_editor.setWindowModality(Qt.ApplicationModal)
        Command_editor.resize(540, 440)
        self.gridLayout = QGridLayout(Command_editor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.vl2 = QVBoxLayout()
        self.vl2.setObjectName(u"vl2")
        self.fl = QFormLayout()
        self.fl.setObjectName(u"fl")
        self.lbl_chip = QLabel(Command_editor)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.fl.setWidget(2, QFormLayout.LabelRole, self.lbl_chip)

        self.lbl_chip_val = QLabel(Command_editor)
        self.lbl_chip_val.setObjectName(u"lbl_chip_val")

        self.fl.setWidget(2, QFormLayout.FieldRole, self.lbl_chip_val)

        self.lbl_cmd = QLabel(Command_editor)
        self.lbl_cmd.setObjectName(u"lbl_cmd")

        self.fl.setWidget(3, QFormLayout.LabelRole, self.lbl_cmd)

        self.lbl_cmd_val = QLabel(Command_editor)
        self.lbl_cmd_val.setObjectName(u"lbl_cmd_val")

        self.fl.setWidget(3, QFormLayout.FieldRole, self.lbl_cmd_val)

        self.lbl_name = QLabel(Command_editor)
        self.lbl_name.setObjectName(u"lbl_name")

        self.fl.setWidget(6, QFormLayout.LabelRole, self.lbl_name)

        self.lie_name = QLineEdit(Command_editor)
        self.lie_name.setObjectName(u"lie_name")
        self.lie_name.setMaximumSize(QSize(300, 16777215))
        self.lie_name.setMaxLength(25)

        self.fl.setWidget(6, QFormLayout.FieldRole, self.lie_name)

        self.lbl_description = QLabel(Command_editor)
        self.lbl_description.setObjectName(u"lbl_description")

        self.fl.setWidget(7, QFormLayout.LabelRole, self.lbl_description)

        self.lie_description = QLineEdit(Command_editor)
        self.lie_description.setObjectName(u"lie_description")
        self.lie_description.setMaximumSize(QSize(300, 16777215))
        self.lie_description.setMaxLength(200)

        self.fl.setWidget(7, QFormLayout.FieldRole, self.lie_description)


        self.vl2.addLayout(self.fl)

        self.vl3 = QVBoxLayout()
        self.vl3.setObjectName(u"vl3")
        self.label = QLabel(Command_editor)
        self.label.setObjectName(u"label")

        self.vl3.addWidget(self.label)

        self.tbl_bytes = QTableWidget(Command_editor)
        self.tbl_bytes.setObjectName(u"tbl_bytes")
        font = QFont()
        font.setFamilies([u"Arial"])
        self.tbl_bytes.setFont(font)
        self.tbl_bytes.setSortingEnabled(True)
        self.tbl_bytes.horizontalHeader().setVisible(True)
        self.tbl_bytes.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_bytes.horizontalHeader().setMinimumSectionSize(36)
        self.tbl_bytes.horizontalHeader().setDefaultSectionSize(110)
        self.tbl_bytes.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_bytes.horizontalHeader().setStretchLastSection(True)
        self.tbl_bytes.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_bytes.verticalHeader().setDefaultSectionSize(30)
        self.tbl_bytes.verticalHeader().setStretchLastSection(True)

        self.vl3.addWidget(self.tbl_bytes)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.btn_clone = QPushButton(Command_editor)
        self.btn_clone.setObjectName(u"btn_clone")
        self.btn_clone.setMinimumSize(QSize(0, 0))
        self.btn_clone.setMaximumSize(QSize(16777215, 16777215))

        self.hl2.addWidget(self.btn_clone)

        self.btn_remove = QPushButton(Command_editor)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setMaximumSize(QSize(30, 16777215))

        self.hl2.addWidget(self.btn_remove)

        self.btn_add_row = QPushButton(Command_editor)
        self.btn_add_row.setObjectName(u"btn_add_row")
        self.btn_add_row.setMaximumSize(QSize(30, 16777215))

        self.hl2.addWidget(self.btn_add_row)

        self.lie_text_2_bytes = QLineEdit(Command_editor)
        self.lie_text_2_bytes.setObjectName(u"lie_text_2_bytes")
        self.lie_text_2_bytes.setMaxLength(200)

        self.hl2.addWidget(self.lie_text_2_bytes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.horizontalSpacer)


        self.vl3.addLayout(self.hl2)


        self.vl2.addLayout(self.vl3)


        self.vl.addLayout(self.vl2)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(Command_editor)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_validate = QPushButton(Command_editor)
        self.btn_validate.setObjectName(u"btn_validate")

        self.hl.addWidget(self.btn_validate)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Command_editor)
        self.btn_cancel.clicked.connect(Command_editor.close)
        self.btn_clone.clicked.connect(Command_editor.clone_row)
        self.btn_remove.clicked.connect(Command_editor.remove_row)
        self.btn_add_row.clicked.connect(Command_editor.add_row)
        self.tbl_bytes.itemChanged.connect(Command_editor.check_cell_content)

        QMetaObject.connectSlotsByName(Command_editor)
    # setupUi

    def retranslateUi(self, Command_editor):
        Command_editor.setWindowTitle(QCoreApplication.translate("Command_editor", u"Hardsploit - Command editor", None))
        self.lbl_chip.setText(QCoreApplication.translate("Command_editor", u"Current chip:", None))
        self.lbl_chip_val.setText(QCoreApplication.translate("Command_editor", u"[CHIP]", None))
        self.lbl_cmd.setText(QCoreApplication.translate("Command_editor", u"Current command:", None))
        self.lbl_cmd_val.setText(QCoreApplication.translate("Command_editor", u"[CMD]", None))
        self.lbl_name.setText(QCoreApplication.translate("Command_editor", u"Name:", None))
        self.lie_name.setInputMask("")
        self.lbl_description.setText(QCoreApplication.translate("Command_editor", u"Description:", None))
        self.label.setText(QCoreApplication.translate("Command_editor", u"Command bytes array:", None))
        self.btn_clone.setText(QCoreApplication.translate("Command_editor", u"Clone", None))
        self.btn_remove.setText(QCoreApplication.translate("Command_editor", u"-", None))
        self.btn_add_row.setText(QCoreApplication.translate("Command_editor", u"+", None))
        self.lie_text_2_bytes.setPlaceholderText(QCoreApplication.translate("Command_editor", u"Text to command bytes", None))
        self.btn_cancel.setText(QCoreApplication.translate("Command_editor", u"Cancel", None))
        self.btn_validate.setText(QCoreApplication.translate("Command_editor", u"Add", None))
    # retranslateUi

