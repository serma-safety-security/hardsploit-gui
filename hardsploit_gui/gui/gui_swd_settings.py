# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_swd_settings.ui'
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

class Ui_Swd_settings(object):
    def setupUi(self, Swd_settings):
        if not Swd_settings.objectName():
            Swd_settings.setObjectName(u"Swd_settings")
        Swd_settings.setWindowModality(Qt.ApplicationModal)
        Swd_settings.resize(400, 179)
        self.gridLayout = QGridLayout(Swd_settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(Swd_settings)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.lbl_parameters = QLabel(Swd_settings)
        self.lbl_parameters.setObjectName(u"lbl_parameters")

        self.horizontalLayout_2.addWidget(self.lbl_parameters)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Swd_settings)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lie_start_address = QLineEdit(Swd_settings)
        self.lie_start_address.setObjectName(u"lie_start_address")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lie_start_address)

        self.label_3 = QLabel(Swd_settings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lie_size_address = QLineEdit(Swd_settings)
        self.lie_size_address.setObjectName(u"lie_size_address")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_size_address)

        self.label_4 = QLabel(Swd_settings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(Swd_settings)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lie_cpu_id_address = QLineEdit(Swd_settings)
        self.lie_cpu_id_address.setObjectName(u"lie_cpu_id_address")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lie_cpu_id_address)

        self.lie_device_id_address = QLineEdit(Swd_settings)
        self.lie_device_id_address.setObjectName(u"lie_device_id_address")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lie_device_id_address)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(Swd_settings)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(Swd_settings)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Swd_settings)
        self.btn_save.clicked.connect(Swd_settings.save_settings)
        self.btn_cancel.clicked.connect(Swd_settings.close)

        QMetaObject.connectSlotsByName(Swd_settings)
    # setupUi

    def retranslateUi(self, Swd_settings):
        Swd_settings.setWindowTitle(QCoreApplication.translate("Swd_settings", u"Hardsploit - SWD settings", None))
        self.lbl_chip.setText(QCoreApplication.translate("Swd_settings", u"[CHIP]", None))
        self.lbl_parameters.setText(QCoreApplication.translate("Swd_settings", u"PARAMETERS", None))
        self.label_2.setText(QCoreApplication.translate("Swd_settings", u"Memory start address:", None))
        self.lie_start_address.setText("")
        self.lie_start_address.setPlaceholderText(QCoreApplication.translate("Swd_settings", u"eg 1ffff7e0", None))
        self.label_3.setText(QCoreApplication.translate("Swd_settings", u"Memory size address:", None))
        self.lie_size_address.setPlaceholderText(QCoreApplication.translate("Swd_settings", u"eg 08000000", None))
        self.label_4.setText(QCoreApplication.translate("Swd_settings", u"CPU ID address:", None))
        self.label_5.setText(QCoreApplication.translate("Swd_settings", u"Device ID address:", None))
        self.lie_cpu_id_address.setPlaceholderText(QCoreApplication.translate("Swd_settings", u"eg E000ED00", None))
        self.lie_device_id_address.setPlaceholderText(QCoreApplication.translate("Swd_settings", u"eg 1FFFF7E8", None))
        self.btn_cancel.setText(QCoreApplication.translate("Swd_settings", u"Cancel", None))
        self.btn_save.setText(QCoreApplication.translate("Swd_settings", u"Save", None))
    # retranslateUi

