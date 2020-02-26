# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create2.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import QMargins

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 30, 551, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.uname.setFont(font)
        self.uname.setObjectName("uname")
        self.horizontalLayout.addWidget(self.uname)
        self.utext = QtWidgets.QLineEdit(self.layoutWidget)
        self.utext.setObjectName("utext")
        self.horizontalLayout.addWidget(self.utext)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        #You can remove the following loc
        #Adding pin Lable
        self.ename = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ename.setFont(font)
        self.ename.setObjectName("ename")
        self.horizontalLayout_2.addWidget(self.ename)
        self.etext = QtWidgets.QLineEdit(self.layoutWidget)
        self.etext.setObjectName("etext")
        self.horizontalLayout_2.addWidget(self.etext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_8")
        
        self.pname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pname.setFont(font)
        self.pname.setObjectName("pname")
        self.horizontalLayout_2.addWidget(self.pname)
        self.ptext = QtWidgets.QLineEdit(self.layoutWidget)
        self.ptext.setObjectName("ptext")
        self.horizontalLayout_2.addWidget(self.ptext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cname.setFont(font)
        self.cname.setObjectName("cname")
        self.horizontalLayout_3.addWidget(self.cname)
        self.ctext = QtWidgets.QLineEdit(self.layoutWidget)
        self.ctext.setObjectName("ctext")
        self.horizontalLayout_3.addWidget(self.ctext)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(200)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addbtn = QtWidgets.QPushButton(self.layoutWidget)
        self.addbtn.setObjectName("addbtn")
        ##when add new user button is clicked
        self.addbtn.clicked.connect(self.addbtn_clkd)
        self.horizontalLayout_4.addWidget(self.addbtn)
        self.exbtn = QtWidgets.QPushButton(self.layoutWidget)
        self.exbtn.setObjectName("exbtn")
        ##When exit buton is clicked
        self.exbtn.clicked.connect(self.exbtn_clk)
        self.horizontalLayout_4.addWidget(self.exbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uname.setText(_translate("MainWindow", "User Name"))
        self.ename.setText(_translate("MainWindow", "PIN"))
        self.pname.setText(_translate("MainWindow", "EMail"))
        self.cname.setText(_translate("MainWindow", "Password"))
        self.addbtn.setText(_translate("MainWindow", "Add User"))
        self.exbtn.setText(_translate("MainWindow", "Exit"))
        
    def addbtn_clkd(self):
        username = self.utext.text()
        pin = self.etext.text()
        email = self.ptext.text()
        password = self.ctext.text()
        
        if(pin=='1234'):
        
            connection = sqlite3.connect("login.db")
            connection.execute("INSERT INTO USERS VALUES (?,?,?)", (username, email, password))
            connection.commit()
            connection.close()
            
            choice=QtWidgets.QMessageBox.question(self,'User Successfully Added','Do you want to add more?',QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if(choice==QtWidgets.QMessageBox.Yes):
                pass
            else:
                '''
                app = QtWidgets.QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                ui1 = Ui_MainWindow()
                ui1.setupUi(MainWindow)
                from login2 import Ui_Form
                MainWindow.setVisible(False)
                self.mainwin=QtWidgets.QMainWindow()
                ui=Ui_Form()
                #mainwin=Ui_Form()
                ui.setupUi(self.mainwin)
                self.mainwin.show()'''
                exit()
        
        else:
            choice1=QtWidgets.QMessageBox.warning(self, 'Incorrect Pin!', 'Try Again',QtWidgets.QMessageBox.Retry)
            pass 

    def exbtn_clk(self):
        '''
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui1 = Ui_MainWindow()
        ui1.setupUi(MainWindow)
        MainWindow.setVisible(False)
        from login2 import Ui_Form
        self.mainwin=QtWidgets.QMainWindow()
        self.ui=Ui_Form()
        #mainwin=Ui_Form()
        self.ui.setupUi(self.mainwin)
        self.mainwin.show()
        '''
        exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui1 = Ui_MainWindow()
    ui1.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

