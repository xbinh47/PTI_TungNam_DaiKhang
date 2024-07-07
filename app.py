import sys
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QSlider, QWidget, QPushButton, QToolButton, QLineEdit
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import cloudinary.uploader
from cloudinary_config import cloudinary
import sqlite3


class movieList(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/movieList.ui", self)
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.OptBtn = self.findChild(QPushButton, 'OptBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')
class CRUD(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/CRUD.ui", self)
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.OptBtn = self.findChild(QPushButton, 'OptBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')
        self.addBtn = self.findChild(QPushButton, 'addBtn')
        self.editBtn = self.findChild(QPushButton, 'editBtn')
        self.removeBtn = self.findChild(QPushButton, 'removeBtn')
        self.searchBtn = self.findChild(QPushButton, 'searchBtn')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')

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

        self.videoUrl = ""
        self.playBtn = self.findChild(QPushButton, 'playBtn')
        self.exitBtn = self.findChild(QToolButton, 'exitBtn')
        self.fullscreenBtn = self.findChild(QPushButton, 'fullscreenBtn')
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.volumeBtn = self.findChild(QPushButton, 'volumeBtn')
        self.timeLabel = self.findChild(QLabel, 'timeLabel')
        self.durationBar = self.findChild(QSlider, 'durationBar')
        self.volumeBar = self.findChild(QSlider, 'volumeBar')

        # Create a QVideoWidget object
        placeholder = self.findChild(QWidget, 'videoWidget')
        self.videoWidget = QVideoWidget()
        self.videoWidget.setGeometry(placeholder.geometry())
        self.videoWidget.setParent(placeholder.parentWidget())
        placeholder.hide()

        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.audioOutput = QAudioOutput(self)
        self.mediaPlayer.setAudioOutput(self.audioOutput)

        self.init_ui()

    def init_ui(self):
        self.playIcon = QIcon("img/play-solid.svg")
        self.pauseIcon = QIcon("img/pause-solid.svg")
        self.volumeHighIcon = QIcon("img/volume-high-solid.svg")
        self.volumeLowIcon = QIcon("img/volume-low-solid.svg")
        self.volumeOffIcon = QIcon("img/volume-off-solid.svg")
        self.muteIcon = QIcon("img/volume-off-solid.svg")
        self.exitIcon = QIcon("img/right-from-bracket-solid.svg")
        self.homeIcon = QIcon("img/house-solid.svg")
        
        self.playBtn.setIcon(self.playIcon)
        self.exitBtn.setIcon(self.exitIcon)
        self.homeBtn.setIcon(self.homeIcon)
        self.volumeBtn.setIcon(self.volumeHighIcon)

        # Ensure volume bar range is set from 0 to 100
        self.current_volume = 50
        self.volumeBar.setValue(self.current_volume)
        self.volumeBar.setRange(0, 100)
        self.volumeBar.setValue(50)  # Set initial volume to 50%

        # Connect QPushButton and QToolButton clicks to methods
        self.playBtn.clicked.connect(self.play)
        self.exitBtn.clicked.connect(self.close)
        self.fullscreenBtn.clicked.connect(self.toggleFullscreen)
        self.volumeBtn.clicked.connect(self.toggleMute)

    def initVideoUrl(self, url): 
        self.videoUrl = url
        self.loadVideo()        
        
    def loadVideo(self):
        self.mediaPlayer.setSource(QUrl.fromLocalFile(self.videoUrl))
        self.mediaPlayer.pause()
        
        self.durationBar.sliderMoved.connect(self.setPosition)
        self.volumeBar.sliderMoved.connect(self.setVolume)
        self.mediaPlayer.playbackStateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.errorOccurred.connect(self.handleError)
    
    def mediaStateChanged(self, state):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(self.pauseIcon)
        else:
            self.playBtn.setIcon(self.playIcon)

    def positionChanged(self, position):
        self.durationBar.setValue(position)
        # Convert position and duration from milliseconds to hh:mm:ss format
        current_time = self.formatTime(position)
        total_time = self.formatTime(self.mediaPlayer.duration())
        self.timeLabel.setText(f"{current_time}/{total_time}")
        
    def durationChanged(self, duration):
        self.durationBar.setRange(0, duration)
    
    def handleError(self):
        self.playBtn.setEnabled(False)
        self.playBtn.setText("Error: " + self.mediaPlayer.errorString())
        
    def play(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
        
    def setVolume(self, volume):
        # Convert the slider value to a float between 0.0 and 1.0
        volume = volume / 100.0
        self.audioOutput.setVolume(volume)
        if volume == 0.0:
            self.volumeBtn.setIcon(self.volumeOffIcon)
        elif volume < 0.5:
            self.volumeBtn.setIcon(self.volumeLowIcon)
        else:
            self.volumeBtn.setIcon(self.volumeHighIcon)
    
    def toggleMute(self):
        if self.audioOutput.isMuted():
            self.audioOutput.setMuted(False)
            if self.current_volume >= 50:
                self.volumeBtn.setIcon(self.volumeHighIcon)
            elif self.current_volume < 50:
                self.volumeBtn.setIcon(self.volumeLowIcon)
            else:
                self.volumeBtn.setIcon(self.volumeOffIcon)
            self.volumeBar.setValue(self.current_volume)
            
        else:
            self.audioOutput.setMuted(True)
            self.volumeBtn.setIcon(self.muteIcon)
            self.current_volume = self.volumeBar.value()
            self.volumeBar.setValue(0)
    
    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def formatTime(self, milliseconds):
        total_seconds = milliseconds // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    sqliteConnection = sqlite3.connect('data/db.db')
    def query_db(query):
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall() #check if the result was in db(in list)
        cursor.close()
        return result
    
    app = QtWidgets.QApplication(sys.argv)
    widget = Watch()
    widget.initVideoUrl("https://res.cloudinary.com/duwwvifxn/video/upload/v1720250930/Despicable_Me_4_Official_Trailer_gwoeip.mp4")
    widget.show()
    sys.exit(app.exec())
