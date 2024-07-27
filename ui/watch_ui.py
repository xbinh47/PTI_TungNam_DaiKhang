# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watch.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 636)
        MainWindow.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.505, y2:1, stop:0.725962 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setEnabled(True)
        self.leftMenu.setGeometry(QRect(10, 10, 50, 625))
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

        self.logo = QLabel(self.leftMenu)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"border-radius:10px\n"
"")
        self.logo.setPixmap(QPixmap(u"../img/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setMargin(8)

        self.verticalLayout_3.addWidget(self.logo)

        self.homeBtn = QPushButton(self.leftMenu)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        self.homeBtn.setMinimumSize(QSize(0, 50))
        self.homeBtn.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)")
        icon = QIcon()
        icon.addFile(u"../img/house-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(25, 25))
        self.homeBtn.setCheckable(True)
        self.homeBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.listBtn = QPushButton(self.leftMenu)
        self.listBtn.setObjectName(u"listBtn")
        sizePolicy.setHeightForWidth(self.listBtn.sizePolicy().hasHeightForWidth())
        self.listBtn.setSizePolicy(sizePolicy)
        self.listBtn.setMinimumSize(QSize(0, 50))
        self.listBtn.setStyleSheet(u"border-radius:10px")
        icon1 = QIcon()
        icon1.addFile(u"../img/bars-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.listBtn.setIcon(icon1)
        self.listBtn.setIconSize(QSize(25, 25))
        self.listBtn.setCheckable(True)
        self.listBtn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.listBtn)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitBtn = QToolButton(self.leftMenu)
        self.exitBtn.setObjectName(u"exitBtn")
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setMinimumSize(QSize(0, 50))
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitBtn.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.928, y1:1, x2:0.932692, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        icon2 = QIcon()
        icon2.addFile(u"../img/right-from-bracket-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon2)
        self.exitBtn.setIconSize(QSize(25, 25))
        self.exitBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.exitBtn)

        self.watchFrame = QFrame(self.centralwidget)
        self.watchFrame.setObjectName(u"watchFrame")
        self.watchFrame.setGeometry(QRect(70, 10, 901, 621))
        self.watchFrame.setFrameShape(QFrame.StyledPanel)
        self.watchFrame.setFrameShadow(QFrame.Raised)
        self.menuBar = QFrame(self.watchFrame)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 881, 31))
        self.menuBar.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px")
        self.menuBar.setFrameShape(QFrame.StyledPanel)
        self.menuBar.setFrameShadow(QFrame.Raised)
        self.videoName = QLabel(self.menuBar)
        self.videoName.setObjectName(u"videoName")
        self.videoName.setGeometry(QRect(10, 10, 861, 20))
        self.controlFrame = QFrame(self.watchFrame)
        self.controlFrame.setObjectName(u"controlFrame")
        self.controlFrame.setGeometry(QRect(0, 550, 881, 71))
        self.controlFrame.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-radius:10px")
        self.controlFrame.setFrameShape(QFrame.StyledPanel)
        self.controlFrame.setFrameShadow(QFrame.Raised)
        self.durationBar = QSlider(self.controlFrame)
        self.durationBar.setObjectName(u"durationBar")
        self.durationBar.setGeometry(QRect(130, 10, 731, 22))
        self.durationBar.setOrientation(Qt.Horizontal)
        self.timeLabel = QLabel(self.controlFrame)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(10, 10, 121, 20))
        self.volumeBar = QSlider(self.controlFrame)
        self.volumeBar.setObjectName(u"volumeBar")
        self.volumeBar.setGeometry(QRect(700, 40, 160, 22))
        self.volumeBar.setMaximum(100)
        self.volumeBar.setValue(100)
        self.volumeBar.setOrientation(Qt.Horizontal)
        self.volumeBtn = QPushButton(self.controlFrame)
        self.volumeBtn.setObjectName(u"volumeBtn")
        self.volumeBtn.setGeometry(QRect(650, 30, 41, 41))
        self.volumeBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../img/volume-high-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.volumeBtn.setIcon(icon3)
        self.volumeBtn.setIconSize(QSize(30, 20))
        self.playBtn = QPushButton(self.controlFrame)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setGeometry(QRect(430, 34, 41, 31))
        self.playBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../img/pause-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon4)
        self.fullscreenBtn = QPushButton(self.controlFrame)
        self.fullscreenBtn.setObjectName(u"fullscreenBtn")
        self.fullscreenBtn.setGeometry(QRect(10, 40, 111, 29))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.fullscreenBtn.setFont(font)
        self.fullscreenBtn.setStyleSheet(u"border-radius:10px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0)")
        self.videoWidget = QWidget(self.watchFrame)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(0, 40, 881, 501))
        self.videoWidget.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.homeBtn.setText("")
        self.listBtn.setText("")
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"       EXIT", None))
        self.videoName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00/00:00:00", None))
        self.volumeBtn.setText("")
        self.playBtn.setText("")
        self.fullscreenBtn.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
    # retranslateUi

