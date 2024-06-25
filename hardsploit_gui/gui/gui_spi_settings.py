# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_spi_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Spi_settings(object):
    def setupUi(self, Spi_settings):
        if not Spi_settings.objectName():
            Spi_settings.setObjectName(u"Spi_settings")
        Spi_settings.resize(528, 237)
        self.gridLayout = QGridLayout(Spi_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.lbl_chip = QLabel(Spi_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl.addWidget(self.lbl_chip)

        self.lbl_param = QLabel(Spi_settings)
        self.lbl_param.setObjectName(u"lbl_param")

        self.hl.addWidget(self.lbl_param)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)


        self.gridLayout.addLayout(self.hl, 1, 0, 1, 1)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.fl = QFormLayout()
        self.fl.setObjectName(u"fl")
        self.lbl_frequency = QLabel(Spi_settings)
        self.lbl_frequency.setObjectName(u"lbl_frequency")

        self.fl.setWidget(2, QFormLayout.LabelRole, self.lbl_frequency)

        self.cbx_frequency = QComboBox(Spi_settings)
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.addItem("")
        self.cbx_frequency.setObjectName(u"cbx_frequency")
        self.cbx_frequency.setMaximumSize(QSize(100, 16777215))

        self.fl.setWidget(2, QFormLayout.FieldRole, self.cbx_frequency)

        self.lbl_cmd_read = QLabel(Spi_settings)
        self.lbl_cmd_read.setObjectName(u"lbl_cmd_read")

        self.fl.setWidget(3, QFormLayout.LabelRole, self.lbl_cmd_read)

        self.lie_cmd_read = QLineEdit(Spi_settings)
        self.lie_cmd_read.setObjectName(u"lie_cmd_read")
        self.lie_cmd_read.setMaximumSize(QSize(100, 16777215))
        self.lie_cmd_read.setMaxLength(5)

        self.fl.setWidget(3, QFormLayout.FieldRole, self.lie_cmd_read)

        self.lbl_cmd_erase = QLabel(Spi_settings)
        self.lbl_cmd_erase.setObjectName(u"lbl_cmd_erase")

        self.fl.setWidget(5, QFormLayout.LabelRole, self.lbl_cmd_erase)

        self.lie_cmd_erase = QLineEdit(Spi_settings)
        self.lie_cmd_erase.setObjectName(u"lie_cmd_erase")
        self.lie_cmd_erase.setMaxLength(5)

        self.fl.setWidget(5, QFormLayout.FieldRole, self.lie_cmd_erase)

        self.lbl_cmd_write = QLabel(Spi_settings)
        self.lbl_cmd_write.setObjectName(u"lbl_cmd_write")

        self.fl.setWidget(6, QFormLayout.LabelRole, self.lbl_cmd_write)

        self.lie_cmd_write_enable = QLineEdit(Spi_settings)
        self.lie_cmd_write_enable.setObjectName(u"lie_cmd_write_enable")
        self.lie_cmd_write_enable.setMaxLength(5)

        self.fl.setWidget(6, QFormLayout.FieldRole, self.lie_cmd_write_enable)

        self.lbl_mode = QLabel(Spi_settings)
        self.lbl_mode.setObjectName(u"lbl_mode")

        self.fl.setWidget(1, QFormLayout.LabelRole, self.lbl_mode)

        self.cbx_mode = QComboBox(Spi_settings)
        self.cbx_mode.addItem("")
        self.cbx_mode.addItem("")
        self.cbx_mode.addItem("")
        self.cbx_mode.addItem("")
        self.cbx_mode.setObjectName(u"cbx_mode")
        self.cbx_mode.setMaximumSize(QSize(100, 16777215))

        self.fl.setWidget(1, QFormLayout.FieldRole, self.cbx_mode)

        self.label = QLabel(Spi_settings)
        self.label.setObjectName(u"label")

        self.fl.setWidget(4, QFormLayout.LabelRole, self.label)

        self.lie_cmd_write = QLineEdit(Spi_settings)
        self.lie_cmd_write.setObjectName(u"lie_cmd_write")

        self.fl.setWidget(4, QFormLayout.FieldRole, self.lie_cmd_write)


        self.hl2.addLayout(self.fl)

        self.fl2 = QFormLayout()
        self.fl2.setObjectName(u"fl2")
        self.lbl_total_size = QLabel(Spi_settings)
        self.lbl_total_size.setObjectName(u"lbl_total_size")

        self.fl2.setWidget(0, QFormLayout.LabelRole, self.lbl_total_size)

        self.lie_total_size = QLineEdit(Spi_settings)
        self.lie_total_size.setObjectName(u"lie_total_size")
        self.lie_total_size.setMaximumSize(QSize(100, 16777215))
        self.lie_total_size.setMaxLength(20)

        self.fl2.setWidget(0, QFormLayout.FieldRole, self.lie_total_size)

        self.lbl_page_size = QLabel(Spi_settings)
        self.lbl_page_size.setObjectName(u"lbl_page_size")

        self.fl2.setWidget(1, QFormLayout.LabelRole, self.lbl_page_size)

        self.lie_page_size = QLineEdit(Spi_settings)
        self.lie_page_size.setObjectName(u"lie_page_size")
        self.lie_page_size.setMaximumSize(QSize(100, 16777215))
        self.lie_page_size.setMaxLength(10)

        self.fl2.setWidget(1, QFormLayout.FieldRole, self.lie_page_size)

        self.label_2 = QLabel(Spi_settings)
        self.label_2.setObjectName(u"label_2")

        self.fl2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lie_write_page_latency = QLineEdit(Spi_settings)
        self.lie_write_page_latency.setObjectName(u"lie_write_page_latency")
        self.lie_write_page_latency.setMaxLength(10)

        self.fl2.setWidget(2, QFormLayout.FieldRole, self.lie_write_page_latency)

        self.label_3 = QLabel(Spi_settings)
        self.label_3.setObjectName(u"label_3")

        self.fl2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lie_erase_time = QLineEdit(Spi_settings)
        self.lie_erase_time.setObjectName(u"lie_erase_time")
        self.lie_erase_time.setMaxLength(10)

        self.fl2.setWidget(3, QFormLayout.FieldRole, self.lie_erase_time)

        self.label_4 = QLabel(Spi_settings)
        self.label_4.setObjectName(u"label_4")

        self.fl2.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.rbn_yes = QRadioButton(Spi_settings)
        self.rbn_yes.setObjectName(u"rbn_yes")
        self.rbn_yes.setChecked(True)

        self.fl2.setWidget(4, QFormLayout.FieldRole, self.rbn_yes)

        self.label_5 = QLabel(Spi_settings)
        self.label_5.setObjectName(u"label_5")

        self.fl2.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.rbn_no = QRadioButton(Spi_settings)
        self.rbn_no.setObjectName(u"rbn_no")

        self.fl2.setWidget(5, QFormLayout.FieldRole, self.rbn_no)


        self.hl2.addLayout(self.fl2)


        self.gridLayout.addLayout(self.hl2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(Spi_settings)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(Spi_settings)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.btn_save)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Spi_settings)
        self.btn_save.clicked.connect(Spi_settings.save_settings)
        self.btn_cancel.clicked.connect(Spi_settings.close)

        QMetaObject.connectSlotsByName(Spi_settings)
    # setupUi

    def retranslateUi(self, Spi_settings):
        Spi_settings.setWindowTitle(QCoreApplication.translate("Spi_settings", u"Hardsploit - Bus settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("Spi_settings", u"[CHIP]", None))
        self.lbl_param.setText(QCoreApplication.translate("Spi_settings", u"PARAMETERS", None))
        self.lbl_frequency.setText(QCoreApplication.translate("Spi_settings", u"Frequency (Mhz):", None))
        self.cbx_frequency.setItemText(0, QCoreApplication.translate("Spi_settings", u"25.00", None))
        self.cbx_frequency.setItemText(1, QCoreApplication.translate("Spi_settings", u"18.75", None))
        self.cbx_frequency.setItemText(2, QCoreApplication.translate("Spi_settings", u"15.00", None))
        self.cbx_frequency.setItemText(3, QCoreApplication.translate("Spi_settings", u"12.50", None))
        self.cbx_frequency.setItemText(4, QCoreApplication.translate("Spi_settings", u"10.71", None))
        self.cbx_frequency.setItemText(5, QCoreApplication.translate("Spi_settings", u"9.38", None))
        self.cbx_frequency.setItemText(6, QCoreApplication.translate("Spi_settings", u"7.50", None))
        self.cbx_frequency.setItemText(7, QCoreApplication.translate("Spi_settings", u"5.00", None))
        self.cbx_frequency.setItemText(8, QCoreApplication.translate("Spi_settings", u"3.95", None))
        self.cbx_frequency.setItemText(9, QCoreApplication.translate("Spi_settings", u"3.00", None))
        self.cbx_frequency.setItemText(10, QCoreApplication.translate("Spi_settings", u"2.03", None))
        self.cbx_frequency.setItemText(11, QCoreApplication.translate("Spi_settings", u"1.00", None))
        self.cbx_frequency.setItemText(12, QCoreApplication.translate("Spi_settings", u"0.50", None))
        self.cbx_frequency.setItemText(13, QCoreApplication.translate("Spi_settings", u"0.29", None))

        self.lbl_cmd_read.setText(QCoreApplication.translate("Spi_settings", u"Read command:", None))
        self.lie_cmd_read.setText("")
        self.lie_cmd_read.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in decimal", None))
        self.lbl_cmd_erase.setText(QCoreApplication.translate("Spi_settings", u"Erase command:", None))
        self.lie_cmd_erase.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in decimal", None))
        self.lbl_cmd_write.setText(QCoreApplication.translate("Spi_settings", u"Enable write command:", None))
        self.lie_cmd_write_enable.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in decimal", None))
        self.lbl_mode.setText(QCoreApplication.translate("Spi_settings", u"Mode:", None))
        self.cbx_mode.setItemText(0, QCoreApplication.translate("Spi_settings", u"0", None))
        self.cbx_mode.setItemText(1, QCoreApplication.translate("Spi_settings", u"1", None))
        self.cbx_mode.setItemText(2, QCoreApplication.translate("Spi_settings", u"2", None))
        self.cbx_mode.setItemText(3, QCoreApplication.translate("Spi_settings", u"3", None))

        self.label.setText(QCoreApplication.translate("Spi_settings", u"Write command:", None))
        self.lie_cmd_write.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in decimal", None))
        self.lbl_total_size.setText(QCoreApplication.translate("Spi_settings", u"Total size:", None))
        self.lie_total_size.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"8 bits word", None))
        self.lbl_page_size.setText(QCoreApplication.translate("Spi_settings", u"Page size:", None))
        self.lie_page_size.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in byte", None))
        self.label_2.setText(QCoreApplication.translate("Spi_settings", u"Write page latency:", None))
        self.lie_write_page_latency.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in miliseconds", None))
        self.label_3.setText(QCoreApplication.translate("Spi_settings", u"Clear chip time:", None))
        self.lie_erase_time.setPlaceholderText(QCoreApplication.translate("Spi_settings", u"in seconds", None))
        self.label_4.setText(QCoreApplication.translate("Spi_settings", u"Flash memory:", None))
        self.rbn_yes.setText(QCoreApplication.translate("Spi_settings", u"Yes", None))
        self.label_5.setText("")
        self.rbn_no.setText(QCoreApplication.translate("Spi_settings", u"No", None))
        self.btn_cancel.setText(QCoreApplication.translate("Spi_settings", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("Spi_settings", u"Save", None))
    # retranslateUi

