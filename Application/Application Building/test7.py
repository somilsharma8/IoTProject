import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox


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
        self.show()

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

