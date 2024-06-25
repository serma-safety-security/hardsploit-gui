# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_import.ui'
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

class Ui_Import(object):
    def setupUi(self, Import):
        if not Import.objectName():
            Import.setObjectName(u"Import")
        Import.resize(298, 138)
        self.gridLayout = QGridLayout(Import)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_import = QLabel(Import)
        self.lbl_import.setObjectName(u"lbl_import")

        self.verticalLayout.addWidget(self.lbl_import)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rbn_comp = QRadioButton(Import)
        self.rbn_comp.setObjectName(u"rbn_comp")
        self.rbn_comp.setChecked(True)

        self.horizontalLayout_3.addWidget(self.rbn_comp)

        self.rbn_cmds = QRadioButton(Import)
        self.rbn_cmds.setObjectName(u"rbn_cmds")

        self.horizontalLayout_3.addWidget(self.rbn_cmds)

        self.rbn_both = QRadioButton(Import)
        self.rbn_both.setObjectName(u"rbn_both")

        self.horizontalLayout_3.addWidget(self.rbn_both)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_file = QPushButton(Import)
        self.btn_file.setObjectName(u"btn_file")

        self.horizontalLayout_2.addWidget(self.btn_file)

        self.label_file = QLabel(Import)
        self.label_file.setObjectName(u"label_file")

        self.horizontalLayout_2.addWidget(self.label_file)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(Import)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_import = QPushButton(Import)
        self.btn_import.setObjectName(u"btn_import")

        self.horizontalLayout.addWidget(self.btn_import)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Import)
        self.btn_cancel.clicked.connect(Import.close)
        self.btn_import.clicked.connect(Import.import_data)
        self.btn_file.clicked.connect(Import.select_file)

        QMetaObject.connectSlotsByName(Import)
    # setupUi

    def retranslateUi(self, Import):
        Import.setWindowTitle(QCoreApplication.translate("Import", u"Import", None))
        self.lbl_import.setText(QCoreApplication.translate("Import", u"Importing:", None))
        self.rbn_comp.setText(QCoreApplication.translate("Import", u"Component", None))
        self.rbn_cmds.setText(QCoreApplication.translate("Import", u"Commands", None))
        self.rbn_both.setText(QCoreApplication.translate("Import", u"Both", None))
        self.btn_file.setText(QCoreApplication.translate("Import", u"File...", None))
        self.label_file.setText("")
        self.btn_cancel.setText(QCoreApplication.translate("Import", u"Cancel", None))
        self.btn_import.setText(QCoreApplication.translate("Import", u"Import", None))
    # retranslateUi

