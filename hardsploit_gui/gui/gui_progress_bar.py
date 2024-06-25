# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_progress_bar.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Progress_bar(object):
    def setupUi(self, Progress_bar):
        if not Progress_bar.objectName():
            Progress_bar.setObjectName(u"Progress_bar")
        Progress_bar.setWindowModality(Qt.ApplicationModal)
        Progress_bar.resize(358, 90)
        self.gridLayout = QGridLayout(Progress_bar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_status = QLabel(Progress_bar)
        self.lbl_status.setObjectName(u"lbl_status")

        self.gridLayout.addWidget(self.lbl_status, 0, 0, 1, 1)

        self.pgb = QProgressBar(Progress_bar)
        self.pgb.setObjectName(u"pgb")
        self.pgb.setValue(0)

        self.gridLayout.addWidget(self.pgb, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_time = QLabel(Progress_bar)
        self.lbl_time.setObjectName(u"lbl_time")

        self.horizontalLayout.addWidget(self.lbl_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbl_close = QPushButton(Progress_bar)
        self.lbl_close.setObjectName(u"lbl_close")

        self.horizontalLayout.addWidget(self.lbl_close)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Progress_bar)
        self.lbl_close.clicked.connect(Progress_bar.close)

        QMetaObject.connectSlotsByName(Progress_bar)
    # setupUi

    def retranslateUi(self, Progress_bar):
        Progress_bar.setWindowTitle(QCoreApplication.translate("Progress_bar", u"Processing...", None))
        self.lbl_status.setText(QCoreApplication.translate("Progress_bar", u"[STATUS]", None))
        self.lbl_time.setText(QCoreApplication.translate("Progress_bar", u"[TIME]", None))
        self.lbl_close.setText(QCoreApplication.translate("Progress_bar", u"Close", None))
    # retranslateUi

