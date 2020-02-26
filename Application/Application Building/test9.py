import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QProgressBar


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 1000, 1000)
        self.setWindowTitle('pyqt5 Tut')
        # self.setWindowIcon(QIcon('pic.png'))

        extractAction = QAction('&Get to the choppah', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
	
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        checkBox = QCheckBox('Enlarge Window', self)
        # checkBox.toggle()  # if you want to be checked in in the begin
        checkBox.move(100, 200)
        #To have initial state toggled on, use the following command
        #checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress=QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)
	
        btn1=QPushButton('Download', self)
        btn1.move(200,120)
        btn1.clicked.connect(self.download)

        self.show()
        
    def download(self):
        self.complete=0
    	
        while self.complete<100 :
                self.complete += 0.0001
                self.progress.setValue(self.complete)    

    def enlarge_window(self, state):
       	if state == Qt.Checked:
    	        self.setGeometry(50, 50, 1000, 600)
       	else:
	        self.setGeometry(50, 50 , 500, 300)

    def close_application(self):
        choice=QMessageBox.question(self,'Exiting','Are you sure?',QMessageBox.Yes|QMessageBox.No)
        if(choice==QMessageBox.Yes):
        	print('Quitting')
        	sys.exit()
        else:
        	pass
        
def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()

