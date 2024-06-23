from PySide6 import QtWidgets
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QLabel, QPushButton, QSlider, QVBoxLayout, QListWidget, QWidget
from PySide6.QtMultimedia import QMediaContent

import cloudinary.uploader

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PySide6.QtGui import QPixmap, QIcon

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        

class Watch(QMainWindow):
    def __init__(self):
        super().__init__()

        self.playBtn = self.findChild(QPushButton, 'playBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.fullscreenBtn = self.findChild(QPushButton, 'fullscreenBtn')
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.volumeBtn = self.findChild(QPushButton, 'volumeBtn')
        self.timeLabel = self.findChild(QLabel, 'timeLabel')
        self.durationBar = self.findChild(QSlider, 'durationbar')
        self.volumeBar = self.findChild(QSlider, 'volumeBar')
        self.videoWidget = self.findChild(QWidget, 'videoWidget')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Home()
    widget.show()
    sys.exit(app.exec())