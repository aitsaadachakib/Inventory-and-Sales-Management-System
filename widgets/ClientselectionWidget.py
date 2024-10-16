from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem,QMainWindow,QMenuBar
from PySide6.QtGui import QIcon
from SuperMarket import Cart
from ui.Purchase import Ui_purchase
from widgets.UIFunctions import showMessage, askQuestion
from ui.Clientselection import Ui_Clientselection
from widgets.UIFunctions import Theme, showMessage
from PySide6.QtCore import QRect, Signal, QObject
from SuperMarket.database import Customer,CustomerType



class ClientselectionMainwigget(QMainWindow):
    def __init__(self,session,purchsewigget,mainwiget,*args,**kwargs):
        self.session=session
        self.mainwiget=mainwiget
        super().__init__(*args, **kwargs)
        self.setWindowTitle('SAADA Phone')
        self.setWindowIcon(QIcon('res/images/icon-128px.png'))
        self.centralWidget=Clientselection(session,purchsewigget,mainwiget)
        self.setCentralWidget(self.centralWidget)
        self.setContentsMargins(0, 23, 0, 0)
        self.theme = {'dark': 'stylesheets/dark.qss',
                      'light': 'stylesheets/light.qss'}
        thm = Theme(self)
        json_theme = thm.getTheme()
        thm.applyTheme(json_theme)
        self.setupMenuBar()

        


    

    def setupMenuBar(self):
        """method to setup the menubar"""
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 23))

        Ajouterclient = menubar.addAction('Ajouter client')
        Ajouterclient.triggered.connect(lambda: self.Addclient())


        settings = menubar.addMenu('Settings')
        theme = settings.addMenu('Theme')
        light = theme.addAction('light')
        dark = theme.addAction('dark')
        thm = Theme(self)
        light.triggered.connect(lambda: thm.applyTheme('light'))
        dark.triggered.connect(lambda: thm.applyTheme('dark'))
    def Addclient(self):
        return












class Clientselection(QWidget,Ui_Clientselection):
    def __init__(self,session,purchsewigget,mainwiget,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.session=session
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.typecombo.addItem('-')
        self.typecombo.addItem('seller')
        self.typecombo.addItem('buyer')


        self.typecombo.currentIndexChanged.connect(self.on_typecombo_changed)

        self.nameinput.textChanged.connect(self.on_nameinput_changed)




        header = self.clienttable.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)


        self.setupTable()
    

    def on_typecombo_changed(self,index):
        return
    def on_nameinput_changed(self,text):
        return
    def setupTable(self):
        self.session.query(Customer).all()



class Addclient(QWidget):
    def __init__(self, parent = ..., f = ...):
        super().__init__(parent, f)