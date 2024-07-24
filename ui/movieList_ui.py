# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movieList.ui'
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
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 636)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.725962 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QRect(50, 0, 951, 625))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_4)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 9, 0)
        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.searchInput = QLineEdit(self.frame_5)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setMinimumSize(QSize(400, 30))
        self.searchInput.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-color:rgb(62, 62, 62);\n"
"font: 700 10pt \"Segoe UI\";\n"
"border-radius:10px")

        self.horizontalLayout_2.addWidget(self.searchInput)

        self.searchBtn = QPushButton(self.frame_5)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(0, 40))
        self.searchBtn.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)")
        icon = QIcon()
        icon.addFile(u"../img/magnifying-glass-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon)
        self.searchBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.searchBtn)

        self.userBtn = QPushButton(self.frame_5)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setMinimumSize(QSize(0, 40))
        self.userBtn.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px")
        icon1 = QIcon()
        icon1.addFile(u"../img/user-regular.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon1)
        self.userBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.userBtn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.widget)

        self.movieList = QScrollArea(self.widget_4)
        self.movieList.setObjectName(u"movieList")
        self.movieList.setStyleSheet(u"background-color:rgb(0, 0, 0);")
        self.movieList.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 949, 583))
        self.movieList.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.movieList)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 51, 621))
        self.homeBtn = QPushButton(self.widget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setGeometry(QRect(0, 70, 50, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(0, 50))
        self.homeBtn.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)")
        icon2 = QIcon()
        icon2.addFile(u"../img/house-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon2)
        self.homeBtn.setIconSize(QSize(25, 25))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)
        self.listBtn = QPushButton(self.widget_2)
        self.listBtn.setObjectName(u"listBtn")
        self.listBtn.setGeometry(QRect(0, 130, 50, 50))
        sizePolicy.setHeightForWidth(self.listBtn.sizePolicy().hasHeightForWidth())
        self.listBtn.setSizePolicy(sizePolicy)
        self.listBtn.setMinimumSize(QSize(0, 50))
        self.listBtn.setStyleSheet(u"border-radius:10px")
        icon3 = QIcon()
        icon3.addFile(u"../img/bars-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.listBtn.setIcon(icon3)
        self.listBtn.setIconSize(QSize(25, 25))
        self.listBtn.setCheckable(True)
        self.listBtn.setAutoExclusive(True)
        self.CRUDButton = QToolButton(self.widget_2)
        self.CRUDButton.setObjectName(u"CRUDButton")
        self.CRUDButton.setGeometry(QRect(0, 190, 50, 50))
        sizePolicy.setHeightForWidth(self.CRUDButton.sizePolicy().hasHeightForWidth())
        self.CRUDButton.setSizePolicy(sizePolicy)
        self.CRUDButton.setMinimumSize(QSize(0, 50))
        self.CRUDButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CRUDButton.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        icon4 = QIcon()
        icon4.addFile(u"../img/film-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CRUDButton.setIcon(icon4)
        self.CRUDButton.setIconSize(QSize(30, 30))
        self.CRUDButton.setCheckable(True)
        self.CRUDButton.setAutoExclusive(True)
        self.CRUDButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.logo = QLabel(self.widget_2)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 0, 50, 50))
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"border-radius:10px\n"
"")
        self.logo.setPixmap(QPixmap(u"../img/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setMargin(8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search movie...", None))
        self.searchBtn.setText("")
        self.userBtn.setText("")
        self.homeBtn.setText("")
        self.listBtn.setText("")
        self.CRUDButton.setText(QCoreApplication.translate("MainWindow", u"       MANAGE", None))
        self.logo.setText("")
    # retranslateUi

