import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('pyqt5 Tut')
        self.home()
        
    def home(self):
        btn=QPushButton("Quit", self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)	
        self.show()

def run():
        app = QApplication(sys.argv)
        #app.setWindowIcon(QIcon('logo.png'))
        gui=window()
        sys.exit(app.exec_())

run()

