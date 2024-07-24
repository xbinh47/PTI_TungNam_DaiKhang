# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        if not EditDialog.objectName():
            EditDialog.setObjectName(u"EditDialog")
        EditDialog.resize(437, 364)
        icon = QIcon()
        icon.addFile(u"sidebar/Crunchyroll_Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        EditDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(EditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(EditDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.titleFrame = QFrame(self.frame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(10)
        self.titleLabel.setFont(font)

        self.horizontalLayout.addWidget(self.titleLabel)

        self.titleEdit = QLineEdit(self.titleFrame)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.titleEdit)


        self.verticalLayout_2.addWidget(self.titleFrame)

        self.releasedateFrame = QFrame(self.frame)
        self.releasedateFrame.setObjectName(u"releasedateFrame")
        self.releasedateFrame.setFrameShape(QFrame.StyledPanel)
        self.releasedateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.releasedateFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.releasedateLabel = QLabel(self.releasedateFrame)
        self.releasedateLabel.setObjectName(u"releasedateLabel")
        self.releasedateLabel.setMinimumSize(QSize(100, 0))
        self.releasedateLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.releasedateLabel)

        self.releaseDateEdit = QDateEdit(self.releasedateFrame)
        self.releaseDateEdit.setObjectName(u"releaseDateEdit")
        self.releaseDateEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.releaseDateEdit)


        self.verticalLayout_2.addWidget(self.releasedateFrame)

        self.imageFrame = QFrame(self.frame)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.imageFrame)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.imageLabel = QLabel(self.imageFrame)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setMinimumSize(QSize(100, 0))
        self.imageLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.imageLabel)

        self.imageBtn = QToolButton(self.imageFrame)
        self.imageBtn.setObjectName(u"imageBtn")
        self.imageBtn.setMinimumSize(QSize(100, 0))
        self.imageBtn.setMaximumSize(QSize(100, 16777215))
        self.imageBtn.setFont(font)
        self.imageBtn.setCheckable(True)
        self.imageBtn.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.imageBtn)


        self.verticalLayout_2.addWidget(self.imageFrame)

        self.urlFrame = QFrame(self.frame)
        self.urlFrame.setObjectName(u"urlFrame")
        self.urlFrame.setFrameShape(QFrame.StyledPanel)
        self.urlFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.urlFrame)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.urlLabel = QLabel(self.urlFrame)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setMinimumSize(QSize(100, 0))
        self.urlLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.urlLabel)

        self.urlEdit = QLineEdit(self.urlFrame)
        self.urlEdit.setObjectName(u"urlEdit")
        self.urlEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_5.addWidget(self.urlEdit)


        self.verticalLayout_2.addWidget(self.urlFrame)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(EditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EditDialog)
        self.buttonBox.accepted.connect(EditDialog.accept)
        self.buttonBox.rejected.connect(EditDialog.reject)

        QMetaObject.connectSlotsByName(EditDialog)
    # setupUi

    def retranslateUi(self, EditDialog):
        EditDialog.setWindowTitle(QCoreApplication.translate("EditDialog", u"Edit Anime", None))
        self.titleLabel.setText(QCoreApplication.translate("EditDialog", u"New Title", None))
        self.releasedateLabel.setText(QCoreApplication.translate("EditDialog", u"New Release Date", None))
        self.imageLabel.setText(QCoreApplication.translate("EditDialog", u"New Image", None))
        self.imageBtn.setText(QCoreApplication.translate("EditDialog", u"Browse", None))
        self.urlLabel.setText(QCoreApplication.translate("EditDialog", u"New URL", None))
    # retranslateUi

