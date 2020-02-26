# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from create2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import QMargins

class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(813, 655)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(190, 50, 501, 591))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fname.setFont(font)
        self.fname.setAlignment(QtCore.Qt.AlignCenter)
        self.fname.setObjectName("fname")
        self.verticalLayout.addWidget(self.fname)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.uname.setFont(font)
        self.uname.setObjectName("uname")
        self.horizontalLayout.addWidget(self.uname)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pname.setFont(font)
        self.pname.setObjectName("pname")
        self.horizontalLayout_2.addWidget(self.pname)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        #User Password Masking
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setObjectName("login_btn")
        #Login button clicked
        self.login_btn.clicked.connect(self.login_check)
        self.horizontalLayout_3.addWidget(self.login_btn)
        self.newusr_btn = QtWidgets.QPushButton(self.widget)
        self.newusr_btn.setObjectName("newusr_btn")
        #new user action trigerred
        self.newusr_btn.clicked.connect(self.newusr_clk)
        self.horizontalLayout_3.addWidget(self.newusr_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fname.setText(_translate("Form", "Login Form"))
        self.uname.setText(_translate("Form", "User :"))
        self.pname.setText(_translate("Form", "Password:"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.newusr_btn.setText(_translate("Form", "Create New User"))

    def login_check(self):
    	username = self.lineEdit.text()
    	password = self.lineEdit_2.text()
    	
    	connection = sqlite3.connect("login.db")
    	result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
    	
    	if( len(result.fetchall()) > 0):
    		print("Welcome To The App")
    		from homepage1 import Ui_MainWindow
    		Form.setVisible(False)
    		self.mainwin=QMainWindow()
    		self.ui=Ui_MainWindow()
    		self.ui.setupUi(self.mainwin)
    		self.mainwin.show() 
    		
    	else:
    		print("Log In Incorrect!")
    		self.msgbox_fail('Warning', 'Log In Incorrect')
    
    def newusr_clk(self):
        Form.setVisible(False)
        self.mainwin=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.mainwin)
        self.mainwin.show() 
        
    def msgbox_fail(self, title, text):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #self.mainwin.setVisible(False)
    sys.exit(app.exec_())

