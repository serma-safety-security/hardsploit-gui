# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_generic_write.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Generic_write(object):
    def setupUi(self, Generic_write):
        if not Generic_write.objectName():
            Generic_write.setObjectName(u"Generic_write")
        Generic_write.setWindowModality(Qt.ApplicationModal)
        Generic_write.resize(241, 155)
        self.gridLayout = QGridLayout(Generic_write)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_write = QLabel(Generic_write)
        self.lbl_write.setObjectName(u"lbl_write")

        self.hl2.addWidget(self.lbl_write)

        self.lbl_chip = QLabel(Generic_write)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs)


        self.vl.addLayout(self.hl2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_file = QLabel(Generic_write)
        self.lbl_file.setObjectName(u"lbl_file")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_file)

        self.btn_file = QPushButton(Generic_write)
        self.btn_file.setObjectName(u"btn_file")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btn_file)

        self.lbl_selected = QLabel(Generic_write)
        self.lbl_selected.setObjectName(u"lbl_selected")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_selected)

        self.lbl_selected_file = QLabel(Generic_write)
        self.lbl_selected_file.setObjectName(u"lbl_selected_file")
        self.lbl_selected_file.setMaximumSize(QSize(250, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lbl_selected_file)

        self.lbl_start = QLabel(Generic_write)
        self.lbl_start.setObjectName(u"lbl_start")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_start)

        self.lie_start = QLineEdit(Generic_write)
        self.lie_start.setObjectName(u"lie_start")
        self.lie_start.setMaxLength(20)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lie_start)


        self.vl.addLayout(self.formLayout)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.btn_write = QPushButton(Generic_write)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setEnabled(False)

        self.hl.addWidget(self.btn_write)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Generic_write)
        self.btn_write.clicked.connect(Generic_write.write)
        self.btn_file.clicked.connect(Generic_write.select_write_file)

        QMetaObject.connectSlotsByName(Generic_write)
    # setupUi

    def retranslateUi(self, Generic_write):
        Generic_write.setWindowTitle(QCoreApplication.translate("Generic_write", u"Hardsploit - Write", None))
        self.lbl_write.setText(QCoreApplication.translate("Generic_write", u"Write in", None))
        self.lbl_chip.setText(QCoreApplication.translate("Generic_write", u"[CHIP]", None))
        self.lbl_file.setText(QCoreApplication.translate("Generic_write", u"Content to write:", None))
        self.btn_file.setText(QCoreApplication.translate("Generic_write", u"File...", None))
        self.lbl_selected.setText(QCoreApplication.translate("Generic_write", u"Selected file:", None))
        self.lbl_selected_file.setText(QCoreApplication.translate("Generic_write", u"None", None))
        self.lbl_start.setText(QCoreApplication.translate("Generic_write", u"Start address:", None))
        self.lie_start.setText(QCoreApplication.translate("Generic_write", u"0", None))
        self.btn_write.setText(QCoreApplication.translate("Generic_write", u"Write", None))
    # retranslateUi

