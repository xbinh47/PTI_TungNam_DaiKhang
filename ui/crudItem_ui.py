# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crudItem.ui'
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
        Form.setStyleSheet(u"")
        self.movieGenre = QLabel(Form)
        self.movieGenre.setObjectName(u"movieGenre")
        self.movieGenre.setGeometry(QRect(0, 550, 321, 31))
        font = QFont()
        font.setPointSize(10)
        self.movieGenre.setFont(font)
        self.movieGenre.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.movieTitle = QLabel(Form)
        self.movieTitle.setObjectName(u"movieTitle")
        self.movieTitle.setGeometry(QRect(0, 460, 321, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.movieTitle.setFont(font1)
        self.movieTitle.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.editBtn = QPushButton(Form)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setGeometry(QRect(30, 590, 121, 29))
        self.movieDate = QLabel(Form)
        self.movieDate.setObjectName(u"movieDate")
        self.movieDate.setGeometry(QRect(0, 510, 151, 31))
        self.movieDate.setFont(font)
        self.movieDate.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"")
        self.movieView = QLabel(Form)
        self.movieView.setObjectName(u"movieView")
        self.movieView.setGeometry(QRect(0, 0, 300, 480))
        self.movieView.setStyleSheet(u"")
        self.removeBtn = QPushButton(Form)
        self.removeBtn.setObjectName(u"removeBtn")
        self.removeBtn.setGeometry(QRect(160, 590, 121, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.movieGenre.setText(QCoreApplication.translate("Form", u"Genre", None))
        self.movieTitle.setText(QCoreApplication.translate("Form", u"Title", None))
        self.editBtn.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.movieDate.setText(QCoreApplication.translate("Form", u"Release date", None))
        self.movieView.setText("")
        self.removeBtn.setText(QCoreApplication.translate("Form", u"Remove", None))
    # retranslateUi

