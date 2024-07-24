# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_up.ui'
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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(0, 0, 0)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 371, 500))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 90, 171, 31))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 291, 16))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.txtEmail = QLineEdit(self.widget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(50, 170, 261, 41))
        self.txtEmail.setFont(font2)
        self.txtEmail.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.txtPass = QLineEdit(self.widget)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(50, 270, 261, 41))
        self.txtPass.setFont(font2)
        self.txtPass.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.btnSignUp = QPushButton(self.widget)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setGeometry(QRect(50, 370, 261, 41))
        self.btnSignUp.setFont(font2)
        self.btnSignUp.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(50, 410, 271, 31))
        self.btnLogin.setFont(font2)
        self.btnLogin.setStyleSheet(u"color:rgb(0, 0, 0);")
        self.txtConfirmPass = QLineEdit(self.widget)
        self.txtConfirmPass.setObjectName(u"txtConfirmPass")
        self.txtConfirmPass.setGeometry(QRect(50, 320, 261, 41))
        self.txtConfirmPass.setFont(font2)
        self.txtConfirmPass.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.txtname = QLineEdit(self.widget)
        self.txtname.setObjectName(u"txtname")
        self.txtname.setGeometry(QRect(50, 220, 261, 41))
        self.txtname.setFont(font2)
        self.txtname.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"color: rgb(0, 0, 0);\n"
"border radius: 10px;\n"
"padding-left: 10px")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 450, 131, 181))
        self.label_3.setStyleSheet(u"border-radius: 10px;")
        self.label_3.setPixmap(QPixmap(u"../img/leaves diagonal1.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, -20, 121, 91))
        self.label_4.setStyleSheet(u"border-radius: 10px;")
        self.label_4.setPixmap(QPixmap(u"../img/leaves-horizontal.png"))
        self.label_4.setScaledContents(True)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(110, 20, 141, 81))
        self.label_14.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_14.setScaledContents(True)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-30, 410, 131, 181))
        self.label_6.setStyleSheet(u"border-radius: 10px;")
        self.label_6.setPixmap(QPixmap(u"../img/leaves diagonal1.png"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-10, -20, 131, 111))
        self.label_7.setStyleSheet(u"border-radius: 10px;")
        self.label_7.setPixmap(QPixmap(u"../img/leaves diagonal2.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 100, 131, 181))
        self.label_8.setStyleSheet(u"border-radius: 10px;")
        self.label_8.setPixmap(QPixmap(u"../img/leaves diagonal1.png"))
        self.label_8.setScaledContents(True)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(300, 280, 151, 81))
        self.label_15.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(-80, 220, 151, 81))
        self.label_16.setPixmap(QPixmap(u"../img/leavecenter.png"))
        self.label_16.setScaledContents(True)
        self.label_16.raise_()
        self.label_15.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.label_14.raise_()
        self.label_2.raise_()
        self.txtEmail.raise_()
        self.label.raise_()
        self.txtPass.raise_()
        self.btnSignUp.raise_()
        self.btnLogin.raise_()
        self.txtConfirmPass.raise_()
        self.txtname.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"            Please enter your details", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txtPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnSignUp.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Already have account?Sign in", None))
        self.txtConfirmPass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.txtname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_14.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
    # retranslateUi

