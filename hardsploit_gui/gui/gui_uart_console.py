# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_uart_console.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Uart_console(object):
    def setupUi(self, Uart_console):
        if not Uart_console.objectName():
            Uart_console.setObjectName(u"Uart_console")
        Uart_console.setWindowModality(Qt.WindowModal)
        Uart_console.resize(710, 587)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Uart_console.sizePolicy().hasHeightForWidth())
        Uart_console.setSizePolicy(sizePolicy)
        self.actionSend = QAction(Uart_console)
        self.actionSend.setObjectName(u"actionSend")
        self.gridLayout = QGridLayout(Uart_console)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_chip = QLabel(Uart_console)
        self.lbl_chip.setObjectName(u"lbl_chip")

        self.horizontalLayout_2.addWidget(self.lbl_chip)

        self.label = QLabel(Uart_console)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_connect = QPushButton(Uart_console)
        self.btn_connect.setObjectName(u"btn_connect")

        self.horizontalLayout_2.addWidget(self.btn_connect)

        self.btn_disconnect = QPushButton(Uart_console)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.btn_disconnect)

        self.pushButton = QPushButton(Uart_console)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.mode_select = QComboBox(Uart_console)
        self.mode_select.addItem("")
        self.mode_select.addItem("")
        self.mode_select.setObjectName(u"mode_select")
        sizePolicy.setHeightForWidth(self.mode_select.sizePolicy().hasHeightForWidth())
        self.mode_select.setSizePolicy(sizePolicy)
        self.mode_select.setMinimumSize(QSize(130, 0))
        self.mode_select.setEditable(False)

        self.horizontalLayout_2.addWidget(self.mode_select)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_clear = QPushButton(Uart_console)
        self.btn_clear.setObjectName(u"btn_clear")

        self.horizontalLayout_2.addWidget(self.btn_clear)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.console = QTextEdit(Uart_console)
        self.console.setObjectName(u"console")
        palette = QPalette()
        brush = QBrush(QColor(170, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush3 = QBrush(QColor(240, 240, 240, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        self.console.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setBold(False)
        self.console.setFont(font)
        self.console.setFrameShape(QFrame.StyledPanel)
        self.console.setFrameShadow(QFrame.Sunken)
        self.console.setReadOnly(True)

        self.verticalLayout.addWidget(self.console)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lie_cmd = QLineEdit(Uart_console)
        self.lie_cmd.setObjectName(u"lie_cmd")

        self.horizontalLayout.addWidget(self.lie_cmd)

        self.btn_send = QPushButton(Uart_console)
        self.btn_send.setObjectName(u"btn_send")

        self.horizontalLayout.addWidget(self.btn_send)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Uart_console)
        self.btn_send.clicked.connect(Uart_console.send)
        self.btn_connect.clicked.connect(Uart_console.connect)
        self.btn_disconnect.clicked.connect(Uart_console.disconnect)
        self.btn_clear.clicked.connect(Uart_console.clear_console)
        self.pushButton.clicked.connect(Uart_console.open_settings)
        self.mode_select.currentIndexChanged.connect(Uart_console.select_mode)

        QMetaObject.connectSlotsByName(Uart_console)
    # setupUi

    def retranslateUi(self, Uart_console):
        Uart_console.setWindowTitle(QCoreApplication.translate("Uart_console", u"Hardsploit - UART console", None))
        self.actionSend.setText(QCoreApplication.translate("Uart_console", u"Send", None))
#if QT_CONFIG(shortcut)
        self.actionSend.setShortcut(QCoreApplication.translate("Uart_console", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_chip.setText(QCoreApplication.translate("Uart_console", u"[CHIP]", None))
        self.label.setText(QCoreApplication.translate("Uart_console", u"UART console", None))
        self.btn_connect.setText(QCoreApplication.translate("Uart_console", u"Connect", None))
        self.btn_disconnect.setText(QCoreApplication.translate("Uart_console", u"Disconnect", None))
        self.pushButton.setText(QCoreApplication.translate("Uart_console", u"Settings", None))
        self.mode_select.setItemText(0, QCoreApplication.translate("Uart_console", u"Simple mode", None))
        self.mode_select.setItemText(1, QCoreApplication.translate("Uart_console", u"Advanced mode", None))

        self.btn_clear.setText(QCoreApplication.translate("Uart_console", u"Clear", None))
        self.btn_send.setText(QCoreApplication.translate("Uart_console", u"Send", None))
    # retranslateUi

