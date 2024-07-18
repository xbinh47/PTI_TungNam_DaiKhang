import sys
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from PyQt6.QtWidgets import  QLabel, QSlider, QWidget, QPushButton, QToolButton, QLineEdit, QScrollArea, QGridLayout, QSizePolicy, QDateEdit, QDialogButtonBox, QMessageBox
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon, QPixmap, QImage
from PyQt6 import uic
import cloudinary.uploader
from cloudinary_config import cloudinary
import database
from database import execute_db
import requests

#The Widgets:
class MovieItemWidget(QWidget):
    def __init__(self, id, name, release_date, genre, img):
        super().__init__()
        uic.loadUi("ui/item.ui", self)
        self.id = id
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.img = img

        self.movieGenre = self.findChild(QLabel, 'movieGenre')
        self.movieDate = self.findChild(QLabel, 'movieDate')
        self.movieTitle = self.findChild(QLabel, 'movieTitle')
        self.movieView = self.findChild(QLabel, 'movieView')
        self.watchBtn = self.findChild(QPushButton, 'watchBtn')

        self.watchBtn.clicked.connect(self.navigateToWatch)
        self.init()

    def init(self):
        image = QImage()
        image.loadFromData(requests.get(self.img).content)
        self.movieView.setPixmap(QPixmap(image))
        self.movieView.setScaledContents(True)
        self.movieTitle.setText(self.name)
        self.movieDate.setText(f"Release date: {self.release_date}")
        self.movieGenre.setText(f"Genre: {self.genre}")

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(650)
        self.setMinimumWidth(300)

    def navigateToWatch(self):
        watchScreen = Watch(self.id)
        watchScreen.show()

class CRUDItemWidget(QWidget):
    def __init__(self, id, name, release_date, genre, img):
        super().__init__()
        uic.loadUi("ui/item.ui", self)
        self.id = id
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.img = img

        self.movieGenre = self.findChild(QLabel, 'movieGenre')
        self.movieDate = self.findChild(QLabel, 'movieDate')
        self.movieTitle = self.findChild(QLabel, 'movieTitle')
        self.movieView = self.findChild(QLabel, 'movieView')
        self.editBtn = self.findChild(QPushButton, 'watchBtn')
        self.removeBtn = self.findChild(QPushButton, 'removeBtn')

        self.editBtn.clicked.connect(self.editMovie)
        self.removeBtn.clicked.connect(self.removeMovie)
        self.init()

    def init(self):
        image = QImage()
        image.loadFromData(requests.get(self.img).content)
        self.movieView.setPixmap(QPixmap(image))
        self.movieView.setScaledContents(True)
        self.movieTitle.setText(self.name)
        self.movieDate.setText(f"Release date: {self.release_date}")
        self.movieGenre.setText(f"Genre: {self.genre}")

    def editMovie(self):
        dialog = EditMovieDialog(self.id)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.init()

    def removeMovie(self):
        query = f"DELETE FROM movie WHERE id = {self.id} "
        execute_db(query)
        self.setParent(None)

#The Dialogs:
class AddMovieDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/add_dialog.ui", self)
        
        self.titleEdit = self.findChild(QLineEdit, 'titleEdit')
        self.releaseDateEdit = self.findChild(QDateEdit, 'releaseDateEdit')
        self.genreEdit = self.findChild(QLineEdit, 'genreEdit')
        self.imageBtn = self.findChild(QPushButton, 'imageBtn')
        self.urlEdit = self.findChild(QLineEdit, 'urlEdit')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        
        self.imageBtn.clicked.connect(self.uploadImage)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        
        self.uploadedImageUrl = ""

    def uploadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            response = cloudinary.uploader.upload(fileName)
            self.uploadedImageUrl = response['url']
            self.urlEdit.setText(self.uploadedImageUrl)

    def accept(self):
        name = self.titleEdit.text()
        release_date = self.releaseDateEdit.date().toString('yyyy-MM-dd')
        genre = self.genreEdit.text()
        img = self.uploadedImageUrl
        
        if name and release_date and genre and img:
            # Add to the database
            query = f"INSERT INTO movie (name, release_date, genre, img) VALUES ('{name}', '{release_date}', '{genre}', '{img}')"
            execute_db(query)
            success_box.setText("Movie edited.")
            success_box.exec()
        else:
            # Show an error message
            err_box.setText("Please fill all fields and upload the thumbnail image!")
            err_box.exec()

class EditMovieDialog(QDialog):
    def __init__(self, movie_id):
        super().__init__()
        uic.loadUi("ui/edit_dialog.ui", self)
        
        self.movie_id = movie_id
        self.titleEdit = self.findChild(QLineEdit, 'titleEdit')
        self.releaseDateEdit = self.findChild(QDateEdit, 'releaseDateEdit')
        self.genreEdit = self.findChild(QLineEdit, 'genreEdit')
        self.imageBtn = self.findChild(QPushButton, 'imageBtn')
        self.urlEdit = self.findChild(QLineEdit, 'urlEdit')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        
        self.imageBtn.clicked.connect(self.uploadImage)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.uploadedImageUrl = ""
        self.loadMovieData()

    def loadMovieData(self):
        movie = database.getMovieByID(self.movie_id)
        if movie:
            self.titleEdit.setText(movie[1])
            self.releaseDateEdit.setDate(QtCore.QDate.fromString(movie[2], 'yyyy-MM-dd'))
            self.genreEdit.setText(movie[3])
            self.urlEdit.setText(movie[4])
            self.uploadedImageUrl = movie[4]

    def uploadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            response = cloudinary.uploader.upload(fileName)
            self.uploadedImageUrl = response['url']
            self.urlEdit.setText(self.uploadedImageUrl)

    def accept(self):
        name = self.titleEdit.text()
        release_date = self.releaseDateEdit.date().toString('yyyy-MM-dd')
        genre = self.genreEdit.text()
        img = self.uploadedImageUrl

        if name and release_date and genre and img:
            # Add to the database
            query = f"INSERT INTO movie (name, release_date, genre, img) VALUES ('{name}', '{release_date}', '{genre}', '{img}')"
            execute_db(query)
            success_box.setText("Movie edited.")
            success_box.exec()
        else:
            # Show an error message
            err_box.setText("Please fill all fields and upload the thumbnail image!")
            err_box.exec()



class MovieList(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/movieList.ui", self)
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.listBtn = self.findChild(QPushButton, 'listBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')
        self.movieList = self.findChild(QScrollArea, 'movieList')

        self.CRUDButton.clicked.connect(self.CRUDShow)
        # self.homeBtn.clicked.connect(self.HomeShow)
        # self.userBtn.clicked.connect(self.UserShow)


        self.movieItem = QWidget()
        self.gridLayout = QGridLayout(self.movieItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)

        self.movieItem.setLayout(self.gridLayout)

        self.movieList.setWidget(self.movieItem)
        self.movieList.setWidgetResizable(True)

        self.renderMovie()

    def renderMovie(self):
        # Clear previous search results
        for i in reversed(range(self.gridLayout.count())): 
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
        
        movieList = database.query_db("SELECT * FROM movie")
        row = 0
        column = 0
        for movie in movieList:
            itemWidget = MovieItemWidget(movie[0], movie[1], movie[3], movie[4], movie[5])
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0

    def CRUDShow(self):
        CRUDPage.show()
        self.close()
    # def HomeShow(self):
    #     HomePage.show()
    #     self.close()
    # def UserShow(self):
    #     UserPage.show()
        # self.close()


class CRUD(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/CRUD.ui", self)
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.listBtn = self.findChild(QPushButton, 'ListBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')
        self.addBtn = self.findChild(QPushButton, 'addBtn')
        self.searchBtn = self.findChild(QPushButton, 'searchBtn')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')
        self.movieList = self.findChild(QScrollArea, 'movieList')

        self.addBtn.clicked.connect(self.addMovie)
        self.searchBtn.clicked.connect(self.searchMovie)
        # self.homeBtn.clicked.connect(self.HomeShow)
        self.listBtn.clicked.connect(self, ListPage.show())
        # self.userBtn.clicked.connect(self.UserShow)

        self.movieItem = QWidget()
        self.gridLayout = QGridLayout(self.movieItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.movieItem.setLayout(self.gridLayout)

        self.movieList.setWidget(self.movieItem)
        self.movieList.setWidgetResizable(True)

        self.renderMovie()

    def addMovie(self):
        dialog = AddMovieDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.renderMovie()

    def searchMovie(self):
        search_term = self.searchEdit.text()
        movieList = database.search_movies(search_term)
        self.displayMovies(movieList)

    def renderMovie(self):
        movieList = database.query_db("SELECT * FROM movie")
        self.displayMovies(movieList)

    def displayMovies(self, movieList):
        for i in reversed(range(self.gridLayout.count())):
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        row = 0
        column = 0
        for movie in movieList:
            itemWidget = MovieItemWidget(movie[0], movie[1], movie[3], movie[4], movie[5])
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0

    def ListShow(self):
        ListPage.show()
        self.close()
    # def HomeShow(self):
    #     HomePage.show()
    #     self.close()
    # def UserShow(self):
    #     UserPage.show()
    #     self.close()

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
    def __init__(self, movie_id):
        super().__init__()
        
        uic.loadUi("ui/watch.ui", self)

        self.movie_id = movie_id

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

        movie = database.getMovieByID(self.movie_id)
        self.init_ui()
        self.initVideoUrl(movie[2])

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
        try:
            print(self.videoUrl)
            self.mediaPlayer.setSource(QUrl.fromLocalFile(self.videoUrl))
            self.mediaPlayer.pause()
            
            self.durationBar.sliderMoved.connect(self.setPosition)
            self.volumeBar.sliderMoved.connect(self.setVolume)
            self.mediaPlayer.playbackStateChanged.connect(self.mediaStateChanged)
            self.mediaPlayer.positionChanged.connect(self.positionChanged)
            self.mediaPlayer.durationChanged.connect(self.durationChanged)
            self.mediaPlayer.errorOccurred.connect(self.handleError)
        except Exception as e:
            print(f"Error loading video: {e}")

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
        error_message = self.mediaPlayer.errorString()
        self.playBtn.setText(f"Error: {error_message}")
        print(f"Media Player Error: {error_message}")
        
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
    app = QtWidgets.QApplication(sys.argv)
    widget = Watch(2)
    widget.show()
    ListPage = MovieList()
    ListPage.show()
    CRUDPage = CRUD()
    # HomePage = Home()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)

    sys.exit(app.exec())

