from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from SuperMarket.users import Users
from ui.login import Ui_login
from widgets.MainWidget import MainWidget
from widgets.UIFunctions import Theme, showMessage
from SuperMarket.database import User


class LoginWidget(QWidget, Ui_login):
    def __init__(self,session, *args, **kwargs):
        self.session=session
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Saada phone')
        self.setWindowIcon(QIcon('res/images/icon-128px.png'))

        self.theme = {'dark': 'stylesheets/login-dark.qss',
                      'light': 'stylesheets/login-light.qss'}
        thm = Theme(self)
        json_theme = thm.getTheme()
        thm.applyTheme(json_theme)

        self.buttonLogo.clicked.connect(lambda: self.changeTheme())
        self.buttonSignIn.clicked.connect(lambda: self.tryLogin())

    def changeTheme(self):
        thm = Theme(self)
        if thm.getTheme() == 'dark':
            theme = 'light'
        else:
            theme = 'dark'
        thm.applyTheme(theme)

    def tryLogin(self):
        username = self.fieldUserName.text()
        password = self.fieldPwd.text()
        if username == '' or password == '':
            showMessage(self, 'Input Error', 'please fill the fields')
        else:
            user = self.session.query(User).filter_by(name=username).first()
            if not user :
                showMessage(self, 'Input Error', 'Invalid Username or password')
            elif user:
                self.login(user)

    def logout(self):
        self.fieldUserName.clear()
        self.fieldPwd.clear()
        self.mainWidget.close()
        self.show()

    def login(self, user_data):
        self.mainWidget = MainWidget(user_data,self.session)
        self.mainWidget.communicate.logout.connect(lambda: self.logout())
        self.hide()
        self.mainWidget.showMaximized()
