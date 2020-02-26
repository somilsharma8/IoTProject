# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import QMargins

class Ui_MainWindow(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.monitor_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.monitor_btn.setFont(font)
        self.monitor_btn.setObjectName("monitor_btn")
        self.verticalLayout.addWidget(self.monitor_btn)
        
        #Monitor button clicked
        self.monitor_btn.clicked.connect(self.sensor)
        
        self.defend_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.defend_btn.setFont(font)
        self.defend_btn.setObjectName("defend_btn")
        self.verticalLayout.addWidget(self.defend_btn)
        
        #Defend button clicked
        self.defend_btn.clicked.connect(self.defend)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow1", "Choose from the following options"))
        self.monitor_btn.setText(_translate("MainWindow1", "MONITOR SERVER"))
        self.defend_btn.setText(_translate("MainWindow1", "DEFEND SERVER"))

    def sensor(self):
        from sensor import Monitor
        
        #MainWindow1.setVisible(False)
        self.mainwin=QMainWindow()
        self.ui=Monitor()
        #self.ui.__init__()
        
    def defend(self):
        from defenders import Defend
        
        #MainWindow1.setVisible(False)
        self.mainwin1=QMainWindow()
        self.ui=Defend()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())

