# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_generic_read.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Generic_read(object):
    def setupUi(self, Generic_read):
        if not Generic_read.objectName():
            Generic_read.setObjectName(u"Generic_read")
        Generic_read.setWindowModality(Qt.ApplicationModal)
        Generic_read.resize(280, 221)
        Generic_read.setMinimumSize(QSize(5, 0))
        Generic_read.setMaximumSize(QSize(16777211, 16777215))
        self.gridLayout = QGridLayout(Generic_read)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_read = QLabel(Generic_read)
        self.lbl_read.setObjectName(u"lbl_read")

        self.hl2.addWidget(self.lbl_read)

        self.lbl_chip = QLabel(Generic_read)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs)


        self.vl.addLayout(self.hl2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_file = QLabel(Generic_read)
        self.lbl_file.setObjectName(u"lbl_file")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_file)

        self.btn_file = QPushButton(Generic_read)
        self.btn_file.setObjectName(u"btn_file")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btn_file)

        self.lbl_selected = QLabel(Generic_read)
        self.lbl_selected.setObjectName(u"lbl_selected")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_selected)

        self.lbl_selected_file = QLabel(Generic_read)
        self.lbl_selected_file.setObjectName(u"lbl_selected_file")
        self.lbl_selected_file.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_selected_file)

        self.lbl_type = QLabel(Generic_read)
        self.lbl_type.setObjectName(u"lbl_type")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_type)

        self.rbn_full = QRadioButton(Generic_read)
        self.rbn_full.setObjectName(u"rbn_full")
        self.rbn_full.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rbn_full)

        self.rbn_range = QRadioButton(Generic_read)
        self.rbn_range.setObjectName(u"rbn_range")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.rbn_range)

        self.lbl_start = QLabel(Generic_read)
        self.lbl_start.setObjectName(u"lbl_start")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_start)

        self.lie_start = QLineEdit(Generic_read)
        self.lie_start.setObjectName(u"lie_start")
        self.lie_start.setEnabled(False)
        self.lie_start.setMaxLength(20)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lie_start)

        self.lbl_stop = QLabel(Generic_read)
        self.lbl_stop.setObjectName(u"lbl_stop")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lbl_stop)

        self.lie_stop = QLineEdit(Generic_read)
        self.lie_stop.setObjectName(u"lie_stop")
        self.lie_stop.setEnabled(False)
        self.lie_stop.setMaxLength(20)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lie_stop)


        self.vl.addLayout(self.formLayout)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.btn_read = QPushButton(Generic_read)
        self.btn_read.setObjectName(u"btn_read")
        self.btn_read.setEnabled(False)

        self.hl.addWidget(self.btn_read)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Generic_read)
        self.btn_read.clicked.connect(Generic_read.read)
        self.btn_file.clicked.connect(Generic_read.select_read_file)
        self.rbn_range.toggled.connect(self.lie_start.setEnabled)
        self.rbn_range.toggled.connect(self.lie_stop.setEnabled)
        self.rbn_full.toggled.connect(self.lie_start.setDisabled)
        self.rbn_full.toggled.connect(self.lie_stop.setDisabled)

        QMetaObject.connectSlotsByName(Generic_read)
    # setupUi

    def retranslateUi(self, Generic_read):
        Generic_read.setWindowTitle(QCoreApplication.translate("Generic_read", u"Hardsploit - Read", None))
        self.lbl_read.setText(QCoreApplication.translate("Generic_read", u"Read from", None))
        self.lbl_chip.setText(QCoreApplication.translate("Generic_read", u"[CHIP]", None))
        self.lbl_file.setText(QCoreApplication.translate("Generic_read", u"Result file:", None))
        self.btn_file.setText(QCoreApplication.translate("Generic_read", u"File...", None))
        self.lbl_selected.setText(QCoreApplication.translate("Generic_read", u"Selected file:", None))
        self.lbl_selected_file.setText(QCoreApplication.translate("Generic_read", u"None", None))
        self.lbl_type.setText(QCoreApplication.translate("Generic_read", u"Type:", None))
        self.rbn_full.setText(QCoreApplication.translate("Generic_read", u"Full read", None))
        self.rbn_range.setText(QCoreApplication.translate("Generic_read", u"Range", None))
        self.lbl_start.setText(QCoreApplication.translate("Generic_read", u"Start address:", None))
        self.lbl_stop.setText(QCoreApplication.translate("Generic_read", u"Stop address:", None))
        self.btn_read.setText(QCoreApplication.translate("Generic_read", u"Read", None))
    # retranslateUi

