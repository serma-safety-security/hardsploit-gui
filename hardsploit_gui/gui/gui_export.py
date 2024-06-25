# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_export.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Export(object):
    def setupUi(self, Export):
        if not Export.objectName():
            Export.setObjectName(u"Export")
        Export.resize(298, 138)
        self.gridLayout = QGridLayout(Export)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vl = QVBoxLayout()
        self.vl.setObjectName(u"vl")
        self.lbl_export = QLabel(Export)
        self.lbl_export.setObjectName(u"lbl_export")

        self.vl.addWidget(self.lbl_export)

        self.hl2 = QHBoxLayout()
        self.hl2.setObjectName(u"hl2")
        self.rbn_comp = QRadioButton(Export)
        self.rbn_comp.setObjectName(u"rbn_comp")
        self.rbn_comp.setChecked(True)

        self.hl2.addWidget(self.rbn_comp)

        self.rbn_cmds = QRadioButton(Export)
        self.rbn_cmds.setObjectName(u"rbn_cmds")
        self.rbn_cmds.setChecked(False)

        self.hl2.addWidget(self.rbn_cmds)

        self.rbn_both = QRadioButton(Export)
        self.rbn_both.setObjectName(u"rbn_both")
        self.rbn_both.setChecked(False)

        self.hl2.addWidget(self.rbn_both)


        self.vl.addLayout(self.hl2)

        self.hl3 = QHBoxLayout()
        self.hl3.setObjectName(u"hl3")
        self.btn_file = QPushButton(Export)
        self.btn_file.setObjectName(u"btn_file")

        self.hl3.addWidget(self.btn_file)

        self.hs2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl3.addItem(self.hs2)


        self.vl.addLayout(self.hl3)

        self.hl = QHBoxLayout()
        self.hl.setObjectName(u"hl")
        self.hs = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hl.addItem(self.hs)

        self.btn_cancel = QPushButton(Export)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.hl.addWidget(self.btn_cancel)

        self.btn_export = QPushButton(Export)
        self.btn_export.setObjectName(u"btn_export")

        self.hl.addWidget(self.btn_export)


        self.vl.addLayout(self.hl)


        self.gridLayout.addLayout(self.vl, 0, 0, 1, 1)


        self.retranslateUi(Export)
        self.btn_cancel.clicked.connect(Export.close)
        self.btn_export.clicked.connect(Export.export_data)
        self.btn_file.clicked.connect(Export.select_file)

        QMetaObject.connectSlotsByName(Export)
    # setupUi

    def retranslateUi(self, Export):
        Export.setWindowTitle(QCoreApplication.translate("Export", u"Export", None))
        self.lbl_export.setText(QCoreApplication.translate("Export", u"Export:", None))
        self.rbn_comp.setText(QCoreApplication.translate("Export", u"Component", None))
        self.rbn_cmds.setText(QCoreApplication.translate("Export", u"Commands", None))
        self.rbn_both.setText(QCoreApplication.translate("Export", u"Both", None))
        self.btn_file.setText(QCoreApplication.translate("Export", u"File...", None))
        self.btn_cancel.setText(QCoreApplication.translate("Export", u"Cancel", None))
        self.btn_export.setText(QCoreApplication.translate("Export", u"Export", None))
    # retranslateUi

