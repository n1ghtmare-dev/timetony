# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import ui.images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QSize(400, 200))
        MainWindow.setMaximumSize(QSize(400, 200))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-image: url(:/images/jpg.jpg);\n"
"background-position: center; \n"
"background-repeat: no-repeat;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setStyleSheet(u"background: none;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 16777215))
        font = QFont()
        font.setFamilies([u"Beverley"])
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 200);\n"
"background: none;\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pin_button = QPushButton(self.frame)
        self.pin_button.setObjectName(u"pin_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pin_button.sizePolicy().hasHeightForWidth())
        self.pin_button.setSizePolicy(sizePolicy1)
        self.pin_button.setMinimumSize(QSize(30, 30))
        self.pin_button.setMaximumSize(QSize(30, 30))
        self.pin_button.setSizeIncrement(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.pin_button.setFont(font1)
        self.pin_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pin_button.setAcceptDrops(False)
        self.pin_button.setAutoFillBackground(False)
        self.pin_button.setStyleSheet(u"background: none;\n"
"background-color: #8D5CEF;\n"
"border: none;\n"
"border-radius: 5px;")
        icon = QIcon()
        icon.addFile(u":/images/pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pin_button.setIcon(icon)
        self.pin_button.setIconSize(QSize(20, 20))
        self.pin_button.setCheckable(False)
        self.pin_button.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pin_button)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: none;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.time_label = QLabel(self.frame_2)
        self.time_label.setObjectName(u"time_label")
        font2 = QFont()
        font2.setFamilies([u"Days Sans"])
        font2.setPointSize(29)
        self.time_label.setFont(font2)
        self.time_label.setStyleSheet(u"color: rgba(255, 255, 255, 200);")

        self.horizontalLayout_2.addWidget(self.time_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setStyleSheet(u"background: none;")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.set_bg_button = QPushButton(self.frame_3)
        self.set_bg_button.setObjectName(u"set_bg_button")
        self.set_bg_button.setMinimumSize(QSize(60, 25))
        self.set_bg_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.set_bg_button.setStyleSheet(u"background: none;\n"
"background-color: #8D5CEF;\n"
"border: none;\n"
"border-radius: 5px;")

        self.horizontalLayout_3.addWidget(self.set_bg_button)

        self.horizontalSpacer_5 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Indigo", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.set_bg_button.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u043d", None))
    # retranslateUi

