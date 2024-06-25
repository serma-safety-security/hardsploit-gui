# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_chip_clone.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Chip_clone(object):
    def setupUi(self, Chip_clone):
        if not Chip_clone.objectName():
            Chip_clone.setObjectName(u"Chip_clone")
        Chip_clone.resize(178, 90)
        self.gridLayout = QGridLayout(Chip_clone)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_clone = QLabel(Chip_clone)
        self.lbl_clone.setObjectName(u"lbl_clone")

        self.verticalLayout.addWidget(self.lbl_clone)

        self.lie_reference = QLineEdit(Chip_clone)
        self.lie_reference.setObjectName(u"lie_reference")
        self.lie_reference.setMaxLength(30)

        self.verticalLayout.addWidget(self.lie_reference)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel = QPushButton(Chip_clone)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_clone = QPushButton(Chip_clone)
        self.btn_clone.setObjectName(u"btn_clone")

        self.horizontalLayout.addWidget(self.btn_clone)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Chip_clone)
        self.btn_cancel.clicked.connect(Chip_clone.close)
        self.btn_clone.clicked.connect(Chip_clone.clone)

        self.btn_clone.setDefault(True)


        QMetaObject.connectSlotsByName(Chip_clone)
    # setupUi

    def retranslateUi(self, Chip_clone):
        Chip_clone.setWindowTitle(QCoreApplication.translate("Chip_clone", u"Chip clone", None))
        self.lbl_clone.setText(QCoreApplication.translate("Chip_clone", u"Clone name", None))
        self.btn_cancel.setText(QCoreApplication.translate("Chip_clone", u"Cancel", None))
        self.btn_clone.setText(QCoreApplication.translate("Chip_clone", u"Clone", None))
    # retranslateUi

