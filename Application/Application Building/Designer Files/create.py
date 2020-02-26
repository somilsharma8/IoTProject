# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(896, 785)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(170, 130, 551, 521))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.uname.setFont(font)
        self.uname.setObjectName("uname")
        self.horizontalLayout.addWidget(self.uname)
        self.utext = QtWidgets.QLineEdit(self.widget)
        self.utext.setObjectName("utext")
        self.horizontalLayout.addWidget(self.utext)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pname.setFont(font)
        self.pname.setObjectName("pname")
        self.horizontalLayout_2.addWidget(self.pname)
        self.ptext = QtWidgets.QLineEdit(self.widget)
        self.ptext.setObjectName("ptext")
        self.horizontalLayout_2.addWidget(self.ptext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cname = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cname.setFont(font)
        self.cname.setObjectName("cname")
        self.horizontalLayout_3.addWidget(self.cname)
        self.ctext = QtWidgets.QLineEdit(self.widget)
        self.ctext.setObjectName("ctext")
        self.horizontalLayout_3.addWidget(self.ctext)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(200)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addbtn = QtWidgets.QPushButton(self.widget)
        self.addbtn.setObjectName("addbtn")
        self.horizontalLayout_4.addWidget(self.addbtn)
        self.exbtn = QtWidgets.QPushButton(self.widget)
        self.exbtn.setObjectName("exbtn")
        self.horizontalLayout_4.addWidget(self.exbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.uname.setText(_translate("Form", "User Name"))
        self.pname.setText(_translate("Form", "Password"))
        self.cname.setText(_translate("Form", "Confirm Password"))
        self.addbtn.setText(_translate("Form", "Add User"))
        self.exbtn.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

