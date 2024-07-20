# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CRUD.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 636)
        MainWindow.setMaximumSize(QSize(16777215, 16777214))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.331731 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QRect(50, 0, 926, 625))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.CRUDMenu = QFrame(self.widget_4)
        self.CRUDMenu.setObjectName(u"CRUDMenu")
        self.CRUDMenu.setStyleSheet(u"")
        self.CRUDMenu.setFrameShape(QFrame.StyledPanel)
        self.CRUDMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.CRUDMenu)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.searchBtn = QPushButton(self.CRUDMenu)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setMinimumSize(QSize(100, 0))
        self.searchBtn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.searchBtn)

        self.searchEdit = QLineEdit(self.CRUDMenu)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color:rgb(65, 65, 65)")

        self.horizontalLayout_6.addWidget(self.searchEdit)

        self.addBtn = QPushButton(self.CRUDMenu)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(100, 0))
        self.addBtn.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_6.addWidget(self.addBtn)

        self.userBtn = QPushButton(self.CRUDMenu)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setMinimumSize(QSize(0, 40))
        self.userBtn.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px")
        icon = QIcon()
        icon.addFile(u"../img/user-regular.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon)
        self.userBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.userBtn)


        self.verticalLayout_5.addWidget(self.CRUDMenu)

        self.PersonalList = QScrollArea(self.widget_4)
        self.PersonalList.setObjectName(u"PersonalList")
        self.PersonalList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 924, 557))
        self.PersonalList.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_5.addWidget(self.PersonalList)

        self.CRUDFrame = QFrame(self.widget_4)
        self.CRUDFrame.setObjectName(u"CRUDFrame")
        self.CRUDFrame.setFrameShape(QFrame.StyledPanel)
        self.CRUDFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.CRUDFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.CRUDFrame)

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
        icon1 = QIcon()
        icon1.addFile(u"../img/bars-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.OptBtn.setIcon(icon1)
        self.OptBtn.setIconSize(QSize(25, 25))
        self.OptBtn.setCheckable(True)
        self.OptBtn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.OptBtn)


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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.searchEdit.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search movie...", None))
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.userBtn.setText("")
        self.logo.setText("")
        self.OptBtn.setText("")
        self.CRUDButton.setText(QCoreApplication.translate("MainWindow", u"       MANAGE", None))
    # retranslateUi

