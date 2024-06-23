import sys
import os
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QListWidget, QListWidgetItem, QDialog, QPushButton, QTextEdit, QVBoxLayout, QApplication, QLabel, QSlider, QWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6 import uic
import cloudinary.uploader

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.helpButton = self.findChild(QPushButton, 'helpBtn')
        self.OptBtn = self.findChild(QPushButton, 'OptBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')

class Watch(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("ui/watch.ui", self)

        self.playBtn = self.findChild(QPushButton, 'playBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.fullscreenBtn = self.findChild(QPushButton, 'fullscreenBtn')
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.volumeBtn = self.findChild(QPushButton, 'volumeBtn')
        self.timeLabel = self.findChild(QLabel, 'timeLabel')
        self.durationBar = self.findChild(QSlider, 'durationbar')
        self.volumeBar = self.findChild(QSlider, 'volumeBar')
        self.videoWidget = self.findChild(QWidget, 'videoWidget')

class movieList(QMainWindow):
    def __init__(self):
        super().__init__()

        
class CRUD(QMainWindow):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Home()
    widget.show()
    sys.exit(app.exec())