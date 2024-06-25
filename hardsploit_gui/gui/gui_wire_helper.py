# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_wire_helper.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Wire_helper(object):
    def setupUi(self, Wire_helper):
        if not Wire_helper.objectName():
            Wire_helper.setObjectName(u"Wire_helper")
        Wire_helper.resize(581, 560)
        Wire_helper.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Wire_helper)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.lbl_advice = QLabel(Wire_helper)
        self.lbl_advice.setObjectName(u"lbl_advice")

        self.vl.addWidget(self.lbl_advice)

        self.lbl_chip = QLabel(Wire_helper)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.vl.addWidget(self.lbl_chip)

        self.gView = QGraphicsView(Wire_helper)
        self.gView.setObjectName(u"gView")
        self.gView.setStyleSheet(u"Qt::GraphicsTextItem{outline: 0;}")

        self.vl.addWidget(self.gView)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(Wire_helper)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_rotate = QPushButton(Wire_helper)
        self.btn_rotate.setObjectName(u"btn_rotate")

        self.hl.addWidget(self.btn_rotate)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 1, 0, 1, 1)


        self.retranslateUi(Wire_helper)
        self.btn_cancel.clicked.connect(Wire_helper.close)
        self.btn_rotate.clicked.connect(Wire_helper.rotate_scene)

        QMetaObject.connectSlotsByName(Wire_helper)
    # setupUi

    def retranslateUi(self, Wire_helper):
        Wire_helper.setWindowTitle(QCoreApplication.translate("Wire_helper", u"Harsploit - Wiring helper", None))
        self.lbl_advice.setText(QCoreApplication.translate("Wire_helper", u"Click on a pin number or signal name to turn ON the corresponding LED", None))
        self.lbl_chip.setText(QCoreApplication.translate("Wire_helper", u"Your chip:", None))
        self.btn_cancel.setText(QCoreApplication.translate("Wire_helper", u"Close", None))
        self.btn_rotate.setText(QCoreApplication.translate("Wire_helper", u"Rotate", None))
    # retranslateUi

