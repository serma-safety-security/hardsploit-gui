# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_can_write.ui'
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

class Ui_Can_write(object):
    def setupUi(self, Can_write):
        if not Can_write.objectName():
            Can_write.setObjectName(u"Can_write")
        Can_write.setWindowModality(Qt.ApplicationModal)
        Can_write.resize(253, 420)
        self.gridLayout = QGridLayout(Can_write)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.lbl_write = QLabel(Can_write)
        self.lbl_write.setObjectName(u"lbl_write")

        self.hl2.addWidget(self.lbl_write)

        self.lbl_chip = QLabel(Can_write)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.hl2.addWidget(self.lbl_chip)

        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl2.addItem(self.hs)


        self.vl.addLayout(self.hl2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.lbl_data = QLabel(Can_write)
        self.lbl_data.setObjectName(u"lbl_data")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_data)

        self.lie_data_1 = QLineEdit(Can_write)
        self.lie_data_1.setObjectName(u"lie_data_1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lie_data_1)

        self.lie_data_2 = QLineEdit(Can_write)
        self.lie_data_2.setObjectName(u"lie_data_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lie_data_2)

        self.label = QLabel(Can_write)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Can_write)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Can_write)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(Can_write)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(Can_write)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(Can_write)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(Can_write)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_7)

        self.lie_data_3 = QLineEdit(Can_write)
        self.lie_data_3.setObjectName(u"lie_data_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lie_data_3)

        self.lie_data_4 = QLineEdit(Can_write)
        self.lie_data_4.setObjectName(u"lie_data_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lie_data_4)

        self.lie_data_5 = QLineEdit(Can_write)
        self.lie_data_5.setObjectName(u"lie_data_5")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lie_data_5)

        self.lie_data_6 = QLineEdit(Can_write)
        self.lie_data_6.setObjectName(u"lie_data_6")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lie_data_6)

        self.lie_data_7 = QLineEdit(Can_write)
        self.lie_data_7.setObjectName(u"lie_data_7")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lie_data_7)

        self.lie_data_8 = QLineEdit(Can_write)
        self.lie_data_8.setObjectName(u"lie_data_8")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lie_data_8)

        self.label_8 = QLabel(Can_write)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_8)


        self.vl.addLayout(self.formLayout)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.btn_write = QPushButton(Can_write)
        self.btn_write.setObjectName(u"btn_write")
        self.btn_write.setEnabled(True)

        self.hl.addWidget(self.btn_write)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Can_write)
        self.btn_write.clicked.connect(Can_write.write)

        QMetaObject.connectSlotsByName(Can_write)
    # setupUi

    def retranslateUi(self, Can_write):
        Can_write.setWindowTitle(QCoreApplication.translate("Can_write", u"Hardsploit - CAN write", None))
        self.lbl_write.setText(QCoreApplication.translate("Can_write", u"Write in", None))
        self.lbl_chip.setText(QCoreApplication.translate("Can_write", u"[CHIP]", None))
        self.lbl_data.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b01:", None))
        self.lie_data_1.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_2.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.label.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b02:", None))
        self.label_2.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b03:", None))
        self.label_3.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b04:", None))
        self.label_4.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b05:", None))
        self.label_5.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b06:", None))
        self.label_6.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b07:", None))
        self.label_7.setText(QCoreApplication.translate("Can_write", u"Byte n\u00b08:", None))
        self.lie_data_3.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_4.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_5.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_6.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_7.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.lie_data_8.setPlaceholderText(QCoreApplication.translate("Can_write", u"hexadecimal value", None))
        self.label_8.setText(QCoreApplication.translate("Can_write", u"Fill only the fields you want to write", None))
        self.btn_write.setText(QCoreApplication.translate("Can_write", u"Write", None))
    # retranslateUi

