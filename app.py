import sys
from PyQt6 import QtCore
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import  QMainWindow, QFileDialog, QDialog
from PyQt6.QtWidgets import  QLabel, QSlider, QWidget, QPushButton, QToolButton, QLineEdit, QScrollArea, QGridLayout, QSizePolicy, QDateEdit, QDialogButtonBox, QMessageBox
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QIcon, QPixmap, QImage
from PyQt6 import uic
import database
import requests
from cloudinary_config import upload_image, upload_video

# The Widgets:
class Register(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ui/sign_up.ui", self)
        self.name = ""
        self.check = 0
        self.btnSignUp = self.findChild(QPushButton, "btnSignUp")
        self.btnLogin = self.findChild(QPushButton, "btnLogin")
        self.txtname = self.findChild(QLineEdit, "txtname")
        self.txtEmail = self.findChild(QLineEdit, "txtEmail")
        self.txtPass = self.findChild(QLineEdit, "txtPass")
        self.txtConfirmPass = self.findChild(QLineEdit, "txtConfirmPass")
        self.eyeBtn = self.findChild(QPushButton, "eyeBtn")
        
        self.btnSignUp.clicked.connect(self.register)
        self.btnLogin.clicked.connect(self.showLoginPage)
        self.eyeBtn.clicked.connect(self.changeMode)
        self.init_ui()

    def init_ui(self):
        self.eyeIcon = QIcon("img\eye-solid.svg")
        self.eyeSlashIcon = QIcon("img\eye-slash-solid.svg")

        self.eyeBtn.setIcon(self.eyeIcon)

    def changeMode(self):
        if self.check == 0:
            self.eyeBtn.setIcon(self.eyeSlashIcon)
            self.txtPass.setEchoMode(QLineEdit.EchoMode.Normal)
            self.txtConfirmPass.setEchoMode(QLineEdit.EchoMode.Normal)
            self.check = 1
        elif self.check == 1:
            self.eyeBtn.setIcon(self.eyeIcon)
            self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.txtConfirmPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.check = 0

    def register(self):
        self.name = self.txtname.text()
        email = self.txtEmail.text()
        password = self.txtPass.text()
        confirm_pass = self.txtConfirmPass.text()

        if not self.name:
            err_box.setText("Please enter your name!")
            err_box.exec()
            return 

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec() 
            return 

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return 
        
        if not confirm_pass:
            err_box.setText("Please enter your confirmed password!")
            err_box.exec() 
            return 

        if password != confirm_pass:
            err_box.setText("Password and Confirm Password not match!")
            err_box.exec()
            return 
        
        query = f"SELECT * FROM USER WHERE email = ('{email}')"
        result = database.query_db(query)

        if len(result) > 0:
            err_box.setText("This email had been used for an another account!")
            err_box.exec()
            return
        
        query = f"INSERT INTO USER (username, password, email) VALUES ('{self.name}', '{password}', '{email}')"
        database.execute_db(query)
        success_box.setText("Register Successfully!")
        
        self.login = Login()
        self.login.show()
        self.close()

    def showLoginPage(self):
        self.login = Login()
        self.login.show()
        self.close()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() #call out the characters of ParentClass
        uic.loadUi("ui/sign_in.ui", self) #Create and load the file ui
        self.name = ""
        self.check = 0
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.txtEmail = self.findChild(QLineEdit, "txtEmail")
        self.txtPass = self.findChild(QLineEdit, "txtPass")
        self.eyeBtn = self.findChild(QPushButton, "eyeBtn")

        self.btn_login.clicked.connect(self.checkLogin)
        self.btn_register.clicked.connect(self.showRegisterPage)
        self.eyeBtn.clicked.connect(self.changeMode)
        self.init_ui()

    def init_ui(self):
        self.eyeIcon = QIcon("img\eye-solid.svg")
        self.eyeSlashIcon = QIcon("img\eye-slash-solid.svg")

        self.eyeBtn.setIcon(self.eyeIcon)

    def changeMode(self):
        if self.check == 0:
            self.eyeBtn.setIcon(self.eyeSlashIcon)
            self.txtPass.setEchoMode(QLineEdit.EchoMode.Normal)
            self.check = 1
        elif self.check == 1:
            self.eyeBtn.setIcon(self.eyeIcon)
            self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
            self.check = 0

    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPass.text()

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec()
            return

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return

        query = f"SELECT * FROM USER WHERE email ='{email}' and password='{password}'" #query select
        result = database.query_db(query)

        if len(result) == 0:
            err_box.setText("Invalid Username or Password!")
            err_box.exec()
            return
        
        success_box.setText("Succesfully Login!")
        success_box.exec()
        self.close()
        self.showMainPage(result[0][0])

    def showRegisterPage(self):
        self.register = Register()
        self.register.show()
        self.close()
        
    def showMainPage(self, id):
        self.main = Home(id)
        self.main.show()


class UserInfo(QtWidgets.QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/user_info.ui", self)
        self.id = id
        self.saveBtn = self.findChild(QPushButton, 'saveBtn')
        self.avatarBtn = self.findChild(QPushButton, 'avatarBtn')
        self.txtEmail = self.findChild(QLineEdit, 'txtEmail')
        self.txtName = self.findChild(QLineEdit, 'txtName')
        self.txtPhone = self.findChild(QLineEdit, 'txtPhone')
        self.txtAddress = self.findChild(QLineEdit, 'txtAddress')
        self.txtCountry = self.findChild(QLineEdit, 'txtCountry')
        self.movieListBtn = self.findChild(QPushButton, 'movieListBtn')
        self.txtPass = self.findChild(QLineEdit, 'txtPass')
        self.saveBtn.clicked.connect(self.updateInfo)
        self.loadData()
        self.avatar = ""
        self.avatarBtn.clicked.connect(self.loadAvatarImage)
        self.movieListBtn.clicked.connect(self.showMainPage)
    
    def loadData(self):
        result = database.get_user_by_id(self.id)
        self.txtName.setText(result[1])
        self.txtEmail.setText(result[2])
        self.txtPass.setText(result[3])
        self.txtPhone.setText(result[4])
        self.txtAddress.setText(result[5])
        self.txtCountry.setText(result[6])
        if result[7]:
            self.avatar = result[7]
            self.avatarBtn.setIcon(QIcon(result[7]))
        
    def loadAvatarImage(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if file:
            self.avatar = file
            self.avatarBtn.setIcon(QIcon(file))
        
    def updateInfo(self):
        email = self.txtEmail.text()
        username = self.txtName.text()
        phone = self.txtPhone.text()
        address = self.txtAddress.text()
        nationality = self.txtCountry.text()
        avatar = self.avatar
        database.update_user(self.id, email, username, phone, address, nationality, avatar)
        success_box.setText("Successfully updated your personal information!")
        success_box.exec()
        self.loadData()
        self.showMainPage()
        
    def showMainPage(self):
        self.main = Home(self.id)
        self.main.show()
        self.close()

class MovieItemWidget(QWidget):
    # Define a signal to handle navigation
    navigate_to_watch = QtCore.pyqtSignal(int)

    def __init__(self, id, name, release_date, genre, img, parent=None):
        super().__init__(parent)
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

        self.watchBtn.clicked.connect(self.emitNavigateSignal)
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

    def emitNavigateSignal(self):
        self.navigate_to_watch.emit(self.id)

class CRUDItemWidget(QWidget):
    def __init__(self, id, name, release_date, genre, img,  crud_page=None, movie_list_page=None):
        super().__init__()
        uic.loadUi("ui/crudItem.ui", self)
        self.id = id
        self.name = name
        self.release_date = release_date
        self.genre = genre
        self.img = img

        self.movieGenre = self.findChild(QLabel, 'movieGenre')
        self.movieDate = self.findChild(QLabel, 'movieDate')
        self.movieTitle = self.findChild(QLabel, 'movieTitle')
        self.movieView = self.findChild(QLabel, 'movieView')
        self.editBtn = self.findChild(QPushButton, 'editBtn')
        self.removeBtn = self.findChild(QPushButton, 'removeBtn')

        self.crud_page = crud_page
        self.movie_list_page = movie_list_page

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
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(650)
        self.setMinimumWidth(300)

    def editMovie(self):
        dialog = EditMovieDialog(self.id)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.init()

    def removeMovie(self):
        query = f"DELETE FROM movie WHERE id = {self.id} "
        database.execute_db(query)
        self.setParent(None)
        success_box.setText("Movie successfully deleted.")
        success_box.exec()
        if self.crud_page:
            self.crud_page.renderMovie()
        if self.movie_list_page:
            self.movie_list_page.renderMovie()

# The Dialogs:
class AddMovieDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/add_dialog.ui", self)
        
        self.titleEdit = self.findChild(QLineEdit, 'titleEdit')
        self.releaseDateEdit = self.findChild(QDateEdit, 'releaseDateEdit')
        self.genreEdit = self.findChild(QLineEdit, 'genreEdit')
        self.imageBtn = self.findChild(QToolButton, 'imageBtn')
        self.videoBtn = self.findChild(QToolButton, 'videoBtn')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.imageText = self.findChild(QLabel, 'imageText')
        self.videoText = self.findChild(QLabel, 'videoText')
        self.imageFile = ""
        self.videoFile = ""
        
        self.imageBtn.clicked.connect(self.uploadImage)
        self.videoBtn.clicked.connect(self.uploadVideo)
        self.buttonBox.accepted.connect(self.accept_add)
        self.buttonBox.rejected.connect(self.reject)

    def uploadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            response = upload_image(fileName)
            self.imageFile = response
            self.imageText.setText(response)
            
    def uploadVideo(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        if fileName:
            response = upload_video(fileName)
            self.videoFile = response
            self.videoText.setText(response)

    def accept_add(self):
        name = self.titleEdit.text()
        release_date = self.releaseDateEdit.date().toString('dd/MM/yyyy')
        genre = self.genreEdit.text()
        
        if name and release_date and genre and self.imageFile and self.videoFile:
            # Add to the database
            query = f"INSERT INTO movie (name, release_date, genre, img, link) VALUES ('{name}', '{release_date}', '{genre}', '{self.imageFile}', '{self.videoFile}')"
            database.execute_db(query)
            success_box.setText("Movie added.")
            success_box.exec()
            self.close()
        else:
            # Show an error message
            err_box.setText("Please fill all fields and upload the thumbnail image!")
            err_box.exec()

class EditMovieDialog(QDialog):
    def __init__(self, movie_id):
        super().__init__()
        uic.loadUi("ui/add_dialog.ui", self)
        
        self.movie_id = movie_id
        self.titleEdit = self.findChild(QLineEdit, 'titleEdit')
        self.releaseDateEdit = self.findChild(QDateEdit, 'releaseDateEdit')
        self.genreEdit = self.findChild(QLineEdit, 'genreEdit')
        self.imageBtn = self.findChild(QToolButton, 'imageBtn')
        self.videoBtn = self.findChild(QToolButton, 'videoBtn')
        self.buttonBox = self.findChild(QDialogButtonBox, 'buttonBox')
        self.imageText = self.findChild(QLabel, 'imageText')
        self.videoText = self.findChild(QLabel, 'videoText')
        self.imageFile = ""
        self.videoFile = ""
        
        self.imageBtn.clicked.connect(self.uploadImage)
        self.videoBtn.clicked.connect(self.uploadVideo)
        self.buttonBox.accepted.connect(self.accept_edit)
        self.buttonBox.rejected.connect(self.reject)
        
        self.loadMovieData()

    def loadMovieData(self):
        movie = database.getMovieByID(self.movie_id)
        if movie:
            self.titleEdit.setText(movie[1])
            self.videoText.setText(movie[2])
            self.release_date = QtCore.QDate.fromString(movie[3], 'dd/MM/yyyy')
            self.genreEdit.setText(movie[4])
            self.imageText.setText(movie[5])
            self.imageFile = movie[5]
            self.videoFile = movie[2]

    def uploadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            response = upload_image(fileName)
            self.imageFile = response
            self.imageText.setText(response)
            
    def uploadVideo(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        if fileName:
            response = upload_video(fileName)
            self.videoFile = response
            self.videoText.setText(response)

    def accept_edit(self):
        name = self.titleEdit.text()
        release_date = self.releaseDateEdit.date().toString('dd/MM/yyyy')
        genre = self.genreEdit.text()
        
        if name and release_date and genre and self.imageFile and self.videoFile:
            # Add to the database
            query = f"UPDATE movie SET name = '{name}', release_date = '{release_date}', genre = '{genre}', img = '{self.imageFile}', link = '{self.videoFile}' WHERE id = {self.movie_id}"
            database.execute_db(query)
            success_box.setText("Movie updated.")
            success_box.exec()
            self.close()

        if self.crud_page:
            self.crud_page.renderMovie()
        if self.movie_list_page:
            self.movie_list_page.renderMovie()
        else:
            error_box = QMessageBox()
            error_box.setText("Please fill all fields and upload the thumbnail image!")
            error_box.exec()

class MovieList(QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/movieList.ui", self)
        
        self.id = id
        self.user = database.get_user_by_id(self.id)
        
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.listBtn = self.findChild(QPushButton, 'listBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QToolButton, 'CRUDButton')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')
        self.movieList = self.findChild(QScrollArea, 'movieList')

        self.CRUDButton.clicked.connect(self.CRUDShow)
        self.userBtn.clicked.connect(self.UserShow)
        self.homeBtn.clicked.connect(self.HomeShow)
        self.searchEdit.textChanged.connect(self.searchMovie)

        self.movieItem = QWidget()
        self.gridLayout = QGridLayout(self.movieItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)

        self.movieItem.setLayout(self.gridLayout)

        self.movieList.setWidget(self.movieItem)
        self.movieList.setWidgetResizable(True)

        self.renderMovie()

    def searchMovie(self):
        search_term = self.searchEdit.text()
        if search_term:
            movieList = database.search_movies(search_term)
        else:
            movieList = database.query_db("SELECT * FROM movie")
        self.renderMovie(movieList)

    def renderMovie(self, movieList=None):
        # Clear previous search results
        for i in reversed(range(self.gridLayout.count())):
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            self.gridLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        if movieList is None:
            movieList = database.query_db("SELECT * FROM movie")
        row = 0
        column = 0
        for movie in movieList:
            itemWidget = MovieItemWidget(movie[0], movie[1], movie[3], movie[4], movie[5], self)
            itemWidget.navigate_to_watch.connect(self.navigateToWatch)
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0

    @QtCore.pyqtSlot(int)
    def navigateToWatch(self, movie_id):
        self.watchScreen = Watch(movie_id, self)
        self.watchScreen.show()
        self.close()

    def CRUDShow(self):
        self.CRUD = CRUD(self.id)
        self.CRUD.show()
        self.close()
    def HomeShow(self):
        self.home = Home(self.id)
        self.home.show()
        self.close()
    def UserShow(self):
        self.user = UserInfo(self.id)
        self.user.show()
        self.close()

class CRUD(QMainWindow):
    def __init__(self, id):
        super().__init__()
        uic.loadUi("ui/CRUD.ui", self)
        
        self.id = id
        self.user = database.get_user_by_id(self.id)
        
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.exitBtn = self.findChild(QPushButton, 'exitBtn')
        self.listBtn = self.findChild(QPushButton, 'listBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QPushButton, 'CRUDButton')
        self.addBtn = self.findChild(QPushButton, 'addBtn')
        self.searchEdit = self.findChild(QLineEdit, 'searchEdit')
        self.CRUDList = self.findChild(QScrollArea, 'CRUDList')

        self.addBtn.clicked.connect(self.addMovie)
        self.searchEdit.textChanged.connect(self.searchMovie)
        self.homeBtn.clicked.connect(self.HomeShow)
        self.listBtn.clicked.connect(self.ListShow)
        self.userBtn.clicked.connect(self.UserShow)

        self.movieItem = QWidget()
        self.gridLayout = QGridLayout(self.movieItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.movieItem.setLayout(self.gridLayout)

        self.CRUDList.setWidget(self.movieItem)
        self.CRUDList.setWidgetResizable(True)

        self.renderMovie()

    def addMovie(self):
        dialog = AddMovieDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.renderMovie()

    def searchMovie(self):
        search_term = self.searchEdit.text()
        if search_term:
            movieList = database.search_movies(search_term)
        else:
            movieList = database.query_db("SELECT * FROM movie")
        self.renderMovie(movieList)

    def refreshMovieList(self):
        self.renderMovie()
        success_box.setText("Movie deleted successfully.")
        success_box.exec()

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
            itemWidget = CRUDItemWidget(movie[0], movie[1], movie[3], movie[4], movie[5])
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0

    def ListShow(self):
        self.movieList = MovieList(self.id)
        self.movieList.show()
        self.close()
    def HomeShow(self):
        self.home = Home(self.id)
        self.home.show()
        self.close()
    def UserShow(self):
        self.user = UserInfo(self.id)
        self.user.show()
        self.close()

class Home(QMainWindow):
    def __init__(self,id):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.id = id
        self.listBtn = self.findChild(QPushButton, 'listBtn')
        self.userBtn = self.findChild(QPushButton, 'userBtn')
        self.CRUDButton = self.findChild(QToolButton, 'CRUDButton')

        self.listBtn.clicked.connect(self.showListPage)
        self.userBtn.clicked.connect(self.User)
        self.CRUDButton.clicked.connect(self.CRUDShow)

    def showListPage (self):
        self.list = MovieList(self.id)
        self.list.show()
        self.close()

    def User (self):
        self.user = UserInfo(self.id)
        self.user.show()
        self.close()
    
    def CRUDShow (self):
        self.crud = CRUD(self.id)
        self.crud.show()
        self.close()

class Watch(QMainWindow):
    def __init__(self, movie_id, list_page):
        super().__init__()
        
        uic.loadUi("ui/watch.ui", self)
        self.movie_id = movie_id
        self.list_page = list_page

        self.videoUrl = ""
        self.playBtn = self.findChild(QPushButton, 'playBtn')
        self.exitBtn = self.findChild(QToolButton, 'exitBtn')
        self.fullscreenBtn = self.findChild(QPushButton, 'fullscreenBtn')
        self.homeBtn = self.findChild(QPushButton, 'homeBtn')
        self.listBtn = self.findChild(QPushButton, 'listBtn')
        self.volumeBtn = self.findChild(QPushButton, 'volumeBtn')
        self.timeLabel = self.findChild(QLabel, 'timeLabel')
        self.durationBar = self.findChild(QSlider, 'durationBar')
        self.volumeBar = self.findChild(QSlider, 'volumeBar')
        self.videoName = self.findChild(QLabel, 'videoName')

        self.listBtn.clicked.connect(self.showListPage)
        self.homeBtn.clicked.connect(self.HomeShow)

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
        self.videoName.setText(movie[1])
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

    def mediaStateChanged(self):
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

    def showListPage(self):
        self.list_page.show()
        self.close()

    def HomeShow(self):
        self.home = Home(self)
        self.home.show()
        self.close()
    
    def closeEvent(self, event):
        self.mediaPlayer.stop()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    login = Login()
    login.show()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)

    sys.exit(app.exec())
