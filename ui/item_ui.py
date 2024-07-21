# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 650)
        self.movieView = QLabel(Form)
        self.movieView.setObjectName(u"movieView")
        self.movieView.setGeometry(QRect(10, 10, 300, 480))
        self.movieTitle = QLabel(Form)
        self.movieTitle.setObjectName(u"movieTitle")
        self.movieTitle.setGeometry(QRect(10, 470, 321, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.movieTitle.setFont(font)
        self.movieTitle.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.movieDate = QLabel(Form)
        self.movieDate.setObjectName(u"movieDate")
        self.movieDate.setGeometry(QRect(10, 520, 151, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.movieDate.setFont(font1)
        self.movieDate.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.movieGenre = QLabel(Form)
        self.movieGenre.setObjectName(u"movieGenre")
        self.movieGenre.setGeometry(QRect(10, 560, 321, 31))
        self.movieGenre.setFont(font1)
        self.movieGenre.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.watchBtn = QPushButton(Form)
        self.watchBtn.setObjectName(u"watchBtn")
        self.watchBtn.setGeometry(QRect(10, 598, 281, 41))
        self.watchBtn.setStyleSheet(u"border-radius:10px;\n"
"background-color:rgb(255, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.movieView.setText("")
        self.movieTitle.setText(QCoreApplication.translate("Form", u"Title", None))
        self.movieDate.setText(QCoreApplication.translate("Form", u"Release date", None))
        self.movieGenre.setText(QCoreApplication.translate("Form", u"Genre", None))
        self.watchBtn.setText(QCoreApplication.translate("Form", u"Watch now", None))
    # retranslateUi

