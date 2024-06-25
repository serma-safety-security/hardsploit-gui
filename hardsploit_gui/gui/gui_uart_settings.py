# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_uart_settings.ui'
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

class Ui_Uart_settings(object):
    def setupUi(self, Uart_settings):
        if not Uart_settings.objectName():
            Uart_settings.setObjectName(u"Uart_settings")
        Uart_settings.setWindowModality(Qt.WindowModal)
        Uart_settings.resize(254, 291)
        self.gridLayout = QGridLayout(Uart_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(Uart_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.lbl_uart = QLabel(Uart_settings)
        self.lbl_uart.setObjectName(u"lbl_uart")

        self.horizontalLayout_2.addWidget(self.lbl_uart)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Uart_settings)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lie_baud_rate = QLineEdit(Uart_settings)
        self.lie_baud_rate.setObjectName(u"lie_baud_rate")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_baud_rate)

        self.label_2 = QLabel(Uart_settings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.lie_word_size = QLineEdit(Uart_settings)
        self.lie_word_size.setObjectName(u"lie_word_size")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lie_word_size)

        self.label_3 = QLabel(Uart_settings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lie_parity_bit = QLineEdit(Uart_settings)
        self.lie_parity_bit.setObjectName(u"lie_parity_bit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lie_parity_bit)

        self.label_4 = QLabel(Uart_settings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lie_parity_type = QLineEdit(Uart_settings)
        self.lie_parity_type.setObjectName(u"lie_parity_type")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lie_parity_type)

        self.label_5 = QLabel(Uart_settings)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.lie_stop_bits_nbr = QLineEdit(Uart_settings)
        self.lie_stop_bits_nbr.setObjectName(u"lie_stop_bits_nbr")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lie_stop_bits_nbr)

        self.label_6 = QLabel(Uart_settings)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.lie_idle_line_lvl = QLineEdit(Uart_settings)
        self.lie_idle_line_lvl.setObjectName(u"lie_idle_line_lvl")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lie_idle_line_lvl)

        self.label_7 = QLabel(Uart_settings)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rbn_cr = QRadioButton(Uart_settings)
        self.rbn_cr.setObjectName(u"rbn_cr")
        self.rbn_cr.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rbn_cr)

        self.rbn_lf = QRadioButton(Uart_settings)
        self.rbn_lf.setObjectName(u"rbn_lf")

        self.horizontalLayout_3.addWidget(self.rbn_lf)

        self.rbn_both = QRadioButton(Uart_settings)
        self.rbn_both.setObjectName(u"rbn_both")

        self.horizontalLayout_3.addWidget(self.rbn_both)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_8 = QLabel(Uart_settings)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.pushButton_3 = QPushButton(Uart_settings)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_3)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(Uart_settings)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Uart_settings)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Uart_settings)
        self.pushButton.clicked.connect(Uart_settings.save_settings)
        self.pushButton_2.clicked.connect(Uart_settings.close)
        self.pushButton_3.clicked.connect(Uart_settings.autodetect)

        QMetaObject.connectSlotsByName(Uart_settings)
    # setupUi

    def retranslateUi(self, Uart_settings):
        Uart_settings.setWindowTitle(QCoreApplication.translate("Uart_settings", u"Hardsploit - UART settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("Uart_settings", u"[CHIP]", None))
        self.lbl_uart.setText(QCoreApplication.translate("Uart_settings", u"UART settings", None))
        self.label.setText(QCoreApplication.translate("Uart_settings", u"Baud rate (manual):", None))
        self.lie_baud_rate.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_2.setText(QCoreApplication.translate("Uart_settings", u"Word size:", None))
        self.lie_word_size.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_3.setText(QCoreApplication.translate("Uart_settings", u"Parity bit:", None))
        self.lie_parity_bit.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_4.setText(QCoreApplication.translate("Uart_settings", u"Parity type:", None))
        self.lie_parity_type.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_5.setText(QCoreApplication.translate("Uart_settings", u"Stop bits number:", None))
        self.lie_stop_bits_nbr.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_6.setText(QCoreApplication.translate("Uart_settings", u"Idle line level:", None))
        self.lie_idle_line_lvl.setPlaceholderText(QCoreApplication.translate("Uart_settings", u"decimal value", None))
        self.label_7.setText(QCoreApplication.translate("Uart_settings", u"CR / LF:", None))
        self.rbn_cr.setText(QCoreApplication.translate("Uart_settings", u"CR", None))
        self.rbn_lf.setText(QCoreApplication.translate("Uart_settings", u"LF", None))
        self.rbn_both.setText(QCoreApplication.translate("Uart_settings", u"Both", None))
        self.label_8.setText(QCoreApplication.translate("Uart_settings", u"Baud rate (auto):", None))
        self.pushButton_3.setText(QCoreApplication.translate("Uart_settings", u"Autodetection", None))
        self.pushButton_2.setText(QCoreApplication.translate("Uart_settings", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("Uart_settings", u"Save", None))
    # retranslateUi

