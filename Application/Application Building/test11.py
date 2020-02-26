import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

class Win(QMainWindow):
	
	def __init__(self):
		
		super().__init__()
		self.title='Python Stuff'
		self.home()
	
	def home(self):
		
		self.setWindowTitle(self.title)
		self.setGeometry(600,400,200,200)
		self.statusBar().showMessage('Running')
		self.show()
		
if __name__== '__main__':
		
	app=QApplication(sys.argv)
	ex=Win()
	sys.exit(app.exec())
