# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 636)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.725962 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setEnabled(True)
        self.leftMenu.setGeometry(QRect(0, 0, 50, 625))
        self.leftMenu.setMinimumSize(QSize(50, 0))
        self.leftMenu.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"border-radius:10px\n"
"")
        self.logo.setPixmap(QPixmap(u"../img/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setMargin(8)

        self.verticalLayout.addWidget(self.logo)

        self.OptBtn = QPushButton(self.frame)
        self.OptBtn.setObjectName(u"OptBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptBtn.sizePolicy().hasHeightForWidth())
        self.OptBtn.setSizePolicy(sizePolicy)
        self.OptBtn.setMinimumSize(QSize(0, 50))
        self.OptBtn.setStyleSheet(u"border-radius:10px")
        icon = QIcon()
        icon.addFile(u"../img/bars-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.OptBtn.setIcon(icon)
        self.OptBtn.setIconSize(QSize(25, 25))
        self.OptBtn.setCheckable(True)
        self.OptBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.OptBtn)

        self.homeBtn = QPushButton(self.frame)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(0, 50))
        self.homeBtn.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)")
        icon1 = QIcon()
        icon1.addFile(u"../img/house-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(25, 25))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.homeBtn)


        self.verticalLayout_3.addWidget(self.frame)

        self.CRUDButton = QToolButton(self.leftMenu)
        self.CRUDButton.setObjectName(u"CRUDButton")
        sizePolicy.setHeightForWidth(self.CRUDButton.sizePolicy().hasHeightForWidth())
        self.CRUDButton.setSizePolicy(sizePolicy)
        self.CRUDButton.setMinimumSize(QSize(0, 50))
        self.CRUDButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CRUDButton.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        icon2 = QIcon()
        icon2.addFile(u"../img/film-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDButton.setIcon(icon2)
        self.CRUDButton.setIconSize(QSize(30, 30))
        self.CRUDButton.setCheckable(True)
        self.CRUDButton.setAutoExclusive(True)
        self.CRUDButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.CRUDButton)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitButton = QToolButton(self.leftMenu)
        self.exitButton.setObjectName(u"exitButton")
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QSize(0, 50))
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitButton.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        icon3 = QIcon()
        icon3.addFile(u"../img/right-from-bracket-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)
        self.exitButton.setIconSize(QSize(25, 25))
        self.exitButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.exitButton)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(60, 40, 981, 581))
        self.userBtn = QPushButton(self.centralwidget)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setGeometry(QRect(1000, 0, 41, 40))
        self.userBtn.setMinimumSize(QSize(0, 40))
        self.userBtn.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px")
        icon4 = QIcon()
        icon4.addFile(u"../img/user-regular.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon4)
        self.userBtn.setIconSize(QSize(20, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 0, 181, 31))
        self.label.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color:rgb(0, 0, 0)")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 0, 93, 29))
        self.pushButton.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(870, 0, 121, 31))
        self.label_2.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 700 10pt \"Segoe UI\";\n"
"color:rgb(0, 0, 0)")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.OptBtn.setText("")
        self.homeBtn.setText("")
        self.CRUDButton.setText(QCoreApplication.translate("MainWindow", u"       MANAGE", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"       EXIT", None))
        self.userBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome to Interten!", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Help?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your Account", None))
    # retranslateUi

