# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_parallel_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Parallel_settings(object):
    def setupUi(self, Parallel_settings):
        if not Parallel_settings.objectName():
            Parallel_settings.setObjectName(u"Parallel_settings")
        Parallel_settings.resize(384, 216)
        self.gridLayout = QGridLayout(Parallel_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_chip = QLabel(Parallel_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.lbl_parameters = QLabel(Parallel_settings)
        self.lbl_parameters.setObjectName(u"lbl_parameters")

        self.hl2.addWidget(self.lbl_parameters)

        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs2)


        self.vl.addLayout(self.hl2)

        self.fl = QFormLayout()
        self.fl.setObjectName(u"fl")
        self.lbl_total_size = QLabel(Parallel_settings)
        self.lbl_total_size.setObjectName(u"lbl_total_size")

        self.fl.setWidget(1, QFormLayout.LabelRole, self.lbl_total_size)

        self.lie_total_size = QLineEdit(Parallel_settings)
        self.lie_total_size.setObjectName(u"lie_total_size")
        self.lie_total_size.setMaxLength(20)

        self.fl.setWidget(1, QFormLayout.FieldRole, self.lie_total_size)

        self.lbl_latency = QLabel(Parallel_settings)
        self.lbl_latency.setObjectName(u"lbl_latency")

        self.fl.setWidget(2, QFormLayout.LabelRole, self.lbl_latency)

        self.lie_read_latency = QLineEdit(Parallel_settings)
        self.lie_read_latency.setObjectName(u"lie_read_latency")
        self.lie_read_latency.setMaxLength(20)

        self.fl.setWidget(2, QFormLayout.FieldRole, self.lie_read_latency)

        self.lbl_write_latency = QLabel(Parallel_settings)
        self.lbl_write_latency.setObjectName(u"lbl_write_latency")

        self.fl.setWidget(3, QFormLayout.LabelRole, self.lbl_write_latency)

        self.lie_write_latency = QLineEdit(Parallel_settings)
        self.lie_write_latency.setObjectName(u"lie_write_latency")

        self.fl.setWidget(3, QFormLayout.FieldRole, self.lie_write_latency)

        self.lbl_word_size = QLabel(Parallel_settings)
        self.lbl_word_size.setObjectName(u"lbl_word_size")

        self.fl.setWidget(4, QFormLayout.LabelRole, self.lbl_word_size)

        self.groupBox = QGroupBox(Parallel_settings)
        self.groupBox.setObjectName(u"groupBox")
        self.rbn_8b = QRadioButton(self.groupBox)
        self.rbn_8b.setObjectName(u"rbn_8b")
        self.rbn_8b.setGeometry(QRect(0, 0, 71, 20))
        self.rbn_8b.setChecked(True)
        self.rbn_16b = QRadioButton(self.groupBox)
        self.rbn_16b.setObjectName(u"rbn_16b")
        self.rbn_16b.setGeometry(QRect(80, 0, 81, 21))

        self.fl.setWidget(4, QFormLayout.FieldRole, self.groupBox)

        self.lbl_page_size = QLabel(Parallel_settings)
        self.lbl_page_size.setObjectName(u"lbl_page_size")

        self.fl.setWidget(5, QFormLayout.LabelRole, self.lbl_page_size)

        self.lie_page_size = QLineEdit(Parallel_settings)
        self.lie_page_size.setObjectName(u"lie_page_size")

        self.fl.setWidget(5, QFormLayout.FieldRole, self.lie_page_size)


        self.vl.addLayout(self.fl)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(Parallel_settings)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(Parallel_settings)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))

        self.hl.addWidget(self.btn_save)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 1, 0, 1, 1)


        self.retranslateUi(Parallel_settings)
        self.btn_cancel.clicked.connect(Parallel_settings.close)
        self.btn_save.clicked.connect(Parallel_settings.save_settings)

        QMetaObject.connectSlotsByName(Parallel_settings)
    # setupUi

    def retranslateUi(self, Parallel_settings):
        Parallel_settings.setWindowTitle(QCoreApplication.translate("Parallel_settings", u"Hardsploit - Parallel settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("Parallel_settings", u"[CHIP]", None))
        self.lbl_parameters.setText(QCoreApplication.translate("Parallel_settings", u"PARAMETERS", None))
        self.lbl_total_size.setText(QCoreApplication.translate("Parallel_settings", u"Total size:", None))
        self.lie_total_size.setText("")
        self.lie_total_size.setPlaceholderText(QCoreApplication.translate("Parallel_settings", u"in bytes", None))
        self.lbl_latency.setText(QCoreApplication.translate("Parallel_settings", u"Read latency:", None))
        self.lie_read_latency.setPlaceholderText(QCoreApplication.translate("Parallel_settings", u" 0 to 1600 nanosecondes", None))
        self.lbl_write_latency.setText(QCoreApplication.translate("Parallel_settings", u"Write latency", None))
        self.lie_write_latency.setText("")
        self.lie_write_latency.setPlaceholderText(QCoreApplication.translate("Parallel_settings", u"in nanosecondes (7 to 1965)", None))
        self.lbl_word_size.setText(QCoreApplication.translate("Parallel_settings", u"Word size:", None))
        self.groupBox.setTitle("")
        self.rbn_8b.setText(QCoreApplication.translate("Parallel_settings", u"8 bits", None))
        self.rbn_16b.setText(QCoreApplication.translate("Parallel_settings", u"16 bits", None))
        self.lbl_page_size.setText(QCoreApplication.translate("Parallel_settings", u"Page size:", None))
        self.lie_page_size.setText("")
        self.lie_page_size.setPlaceholderText(QCoreApplication.translate("Parallel_settings", u"in bytes", None))
        self.btn_cancel.setText(QCoreApplication.translate("Parallel_settings", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("Parallel_settings", u"Save", None))
    # retranslateUi

