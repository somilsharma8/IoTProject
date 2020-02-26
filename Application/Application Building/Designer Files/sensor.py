import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QLineEdit, QGridLayout
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QLabel, QComboBox, QStyleFactory

class Monitor(QMainWindow) :

	def __init__(self):
		super(Monitor,self).__init__()
		self.setGeometry(50,50,5000,1000)
		self.setWindowTitle("Monitor System")
		'''
		self.centralwidget = QWidget(Form)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		'''
		self.home()
		
	def home(self):
		btn=QPushButton('Exit')
		btn.clicked.connect(self.close_win)
		btn.resize(btn.sizeHint())
		btn.move(100, 250)
		btn.show()
		
		self.palette = QPalette()
		
		
		self.progress=QProgressBar(self)
		self.progress.setGeometry(380, 200, 250, 20)
		self.progress.hide()
				
		'''
		btn1=QPushButton('Download', self)
		btn1.move(200,120)
		btn1.clicked.connect(self.btn1)
		'''
		
		font = QFont()
		font.setPointSize(26)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		
		self.field3=QLabel(self)
		self.field3.resize(600, 600)
		self.field3.move(800, 300)	#(800, 300)
		self.field3.setText('WARNING:')
		self.field3.setFont(font)
		
		font.setPointSize(19)
		font.setBold(False)
		font.setItalic(True)
		font.setWeight(10)
		
		self.field4=QLabel(self)
		self.field4.resize(1000, 600)
		self.field4.move(250, 450)	#(250, 450)
		self.field4.setText("Please ensure that the machine you're currently using is bilaterally connected \nto the server and is permitted to access it as root.")
		self.field4.setFont(font)
		
		font = QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		
		self.field=QLabel(self)
		self.field.resize(250, 40)
		self.field.move(450, 100)	#(200,250)
		self.field.setText('--Select an sensor--')
		self.field.setFont(font)
		
		self.field2=QLabel(self)
		self.field2.resize(250, 40)
		self.field2.move(540,250)	#(500, 500)
		self.field2.setText('Downloaded!')
		self.field2.hide()
		
		font.setPointSize(14)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(50)
		
		self.field5=QLabel(self)
		self.field5.resize(600, 300)
		self.field5.move(650,300)	#(500, 500)
		self.field5.setFont(font)
		self.field5.hide()
		
		comboBox=QComboBox(self)
		comboBox.addItem('--Select an option--')
		#comboBox.addItem('Shut Down Server')
		#comboBox.addItem('Notify All Users')
		comboBox.addItem('Motion Sensor')
		
		comboBox.move(740,100)	#(300,300)
		comboBox.resize(200,50)
		comboBox.activated[str].connect(self.field_set)
		
		self.show()
		
	def close_win(self):
		self.close()
		
	def loading(self):
		self.complete=0
		
		while self.complete<100:
			self.complete+=0.00001
			self.progress.setValue(self.complete)
			
						
	def field_set(self, text):
		self.field.setText(text)
		if text=='--Select an option--':
			self.progress.hide()
		
		elif text=='Motion Sensor':
			self.progress.show()
			self.loading()
			self.field2.show()
			
			from fetch import main
			val=main()
			if(val==1):
				self.palette.setColor(QPalette.Foreground,Qt.red)
				self.field5.setText('Intruder has been detected! Please notify all users and defend the server!')
				self.field5.setPalette(self.palette)
				self.field5.show()
			else:
				self.palette.setColor(QPalette.Foreground,Qt.green)
				self.field5.setText('Server is completely secure.')
				self.field5.setPalette(self.palette)
				self.field5.show()
		
if __name__ == "__main__":
	'''
	app = QApplication(sys.argv)
	Gui = Sense()
	sys.exit(app.exec_())
	'''
	#import sys
	app = QApplication(sys.argv)
	Form = QMainWindow()
	ui = Monitor()
	#ui.__init__()
	#Form.show()
	#self.mainwin.setVisible(False)
	sys.exit(app.exec_())

