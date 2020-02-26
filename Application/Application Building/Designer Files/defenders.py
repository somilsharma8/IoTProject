import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QLineEdit, QGridLayout
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QLabel, QComboBox, QStyleFactory

class Defend(QMainWindow) :

	def __init__(self):
		super(Defend,self).__init__()
		self.setGeometry(50,50,5000,1000)
		self.setWindowTitle("Defend System")
		'''
		self.centralwidget = QWidget(Form)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		'''
		self.home()
		
	def home(self):
		#btn=QPushButton('Exit', self.centralwidget)
		#btn.clicked.connect(self.close_win)
		
		#btn.resize(btn.sizeHint())
		#btn.move(50, 50)
		
		self.progress=QProgressBar(self)
		self.progress.setGeometry(400, 400, 250, 20)
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
		
		self.field=QLabel(self)
		self.field.resize(250, 40)
		self.field.move(450, 100)	#(200,250)
		self.field.setText('--Select an option--')
		
		self.field2=QLabel(self)
		self.field2.resize(250, 40)
		self.field2.move(540,300)	#(500, 500)
		self.field2.setText('Downloaded!')
		self.field2.hide()
		
		comboBox=QComboBox(self)
		comboBox.addItem('--Select an option--')
		comboBox.addItem('Shut Down Server')
		comboBox.addItem('Notify All Users')
		
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
		
		elif text=='Shut Down Server':
			self.progress.show()
			self.loading()
			self.field2.show()
			
			import os
			os.system('systemctl poweroff -i')
		
		else:
			self.progress.show()
			self.loading()
			self.field2.setText('All users notified!')
			self.field2.show()
			import smtplib
 
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login("somilsharma8@gmail.com", "somil528491")
			 
			msg = "Server Compromised!"
			sender_id="somilsharma8@gmail.com"
			receiver_id="somil_rajesh@srmuniv.edu.in"
			server.sendmail(sender_id, receiver_id, msg)
			server.quit()	
			
			
		
if __name__ == "__main__":
	'''
	app = QApplication(sys.argv)
	Gui = Sense()
	sys.exit(app.exec_())
	'''
	#import sys
	app = QApplication(sys.argv)
	Form = QMainWindow()
	ui = Defend()
	#ui.__init__()
	#Form.show()
	#self.mainwin.setVisible(False)
	sys.exit(app.exec_())

