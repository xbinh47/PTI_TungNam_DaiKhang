# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_in.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 600)
        MainWindow.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 0, 0)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 50, 371, 500))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 110, 261, 31))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(0, 0, 0);ssssss")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 150, 291, 16))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.txtEmail = QLineEdit(self.widget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(60, 180, 261, 41))
        self.txtEmail.setFont(font2)
        self.txtEmail.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.txtPass = QLineEdit(self.widget)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(60, 230, 261, 41))
        self.txtPass.setFont(font2)
        self.txtPass.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(60, 280, 261, 41))
        self.btn_login.setFont(font2)
        self.btn_login.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.btn_register = QPushButton(self.widget)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(70, 340, 251, 24))
        self.btn_register.setFont(font2)
        self.btn_register.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-10, -40, 161, 91))
        self.label_3.setPixmap(QPixmap(u"../img/leaves-horizontal.png"))
        self.label_3.setScaledContents(True)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(310, -20, 81, 71))
        self.label_6.setPixmap(QPixmap(u"../img/leaves diagonal2.png"))
        self.label_6.setScaledContents(True)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(109, 40, 151, 81))
        self.label_14.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_14.setScaledContents(True)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-30, 380, 131, 181))
        self.label_7.setStyleSheet(u"border-radius: 10px;")
        self.label_7.setPixmap(QPixmap(u"../img/leaves diagonal1.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(260, 380, 131, 151))
        self.label_8.setStyleSheet(u"border-radius: 10px;")
        self.label_8.setPixmap(QPixmap(u"../img/leaves diagonal2.png"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(-40, 180, 101, 91))
        self.label_9.setStyleSheet(u"border-radius: 10px;")
        self.label_9.setPixmap(QPixmap(u"../img/leaves diagonal2.png"))
        self.label_9.setScaledContents(True)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(310, 180, 81, 71))
        self.label_10.setPixmap(QPixmap(u"../img/leaves diagonal2.png"))
        self.label_10.setScaledContents(True)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(-90, 290, 151, 81))
        self.label_15.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(300, 70, 151, 81))
        self.label_16.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_16.setScaledContents(True)
        self.label_16.raise_()
        self.label_10.raise_()
        self.label_14.raise_()
        self.label_2.raise_()
        self.txtEmail.raise_()
        self.label.raise_()
        self.txtPass.raise_()
        self.btn_login.raise_()
        self.btn_register.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_15.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome back", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"            Please enter your details", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Don't have account?Sign up", None))
        self.label_3.setText("")
        self.label_6.setText("")
        self.label_14.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
    # retranslateUi

