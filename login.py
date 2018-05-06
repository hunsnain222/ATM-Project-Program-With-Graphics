# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from Data.welcome import *
from Data.deposite import Ui_Deposite


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMouseTracking(True)
        Dialog.setStyleSheet("")
        self.lb_cardNo = QtWidgets.QLabel(Dialog)
        self.lb_cardNo.setGeometry(QtCore.QRect(90, 70, 66, 17))
        self.lb_cardNo.setTextFormat(QtCore.Qt.PlainText)
        self.lb_cardNo.setObjectName("lb_cardNo")
        self.lb_pin = QtWidgets.QLabel(Dialog)
        self.lb_pin.setGeometry(QtCore.QRect(80, 110, 81, 16))
        self.lb_pin.setObjectName("lb_pin")
        self.line_cardNo = QtWidgets.QLineEdit(Dialog)
        self.line_cardNo.setGeometry(QtCore.QRect(180, 70, 113, 27))
        self.line_cardNo.setObjectName("line_cardNo")
        self.line_pin = QtWidgets.QLineEdit(Dialog)
        self.line_pin.setGeometry(QtCore.QRect(180, 110, 113, 27))
        self.line_pin.setObjectName("line_pin")
        self.b_new = QtWidgets.QPushButton(Dialog)
        self.b_new.setGeometry(QtCore.QRect(240, 160, 111, 27))
        self.b_new.setObjectName("b_new")
        self.b_login = QtWidgets.QPushButton(Dialog)
        self.b_login.setGeometry(QtCore.QRect(110, 160, 111, 27))
        self.b_login.setCheckable(False)
        self.b_login.setFlat(False)
        self.b_login.setObjectName("b_login")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 200, 211, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 240, 301, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 331, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ATM Official Project"))
        Dialog.setWhatsThis(_translate("Dialog", "ATM Project"))
        self.lb_cardNo.setText(_translate("Dialog", "Card NO"))
        self.lb_pin.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">PIN Code</p></body></html>"))
        self.line_cardNo.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter Card No, given by the bank</span></p></body></html>"))
        self.line_pin.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Enter 4-Digin PIN</p></body></html>"))
        self.b_new.setToolTip(_translate("Dialog", "<html><head/><body><p>Contact the Bank in order to be part of State Bank of Pakistan</p></body></html>"))
        self.b_new.setText(_translate("Dialog", "Create Account"))
        self.b_new.clicked.connect(self.message_createAccount)
        self.b_login.setText(_translate("Dialog", "Login"))
        self.b_login.clicked.connect(self.loginCheck)
        self.pushButton_3.setText(_translate("Dialog", "Exit"))
        self.pushButton_3.clicked.connect(self.exit)
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to State Bank of Pakistan</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">A Project prepared by the team --&gt; DareDevils Please be patience as we\'re updating our ATM regularly.</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Hasnain Kazmi , Saood , Ahmed</span></p></body></html>"))
        self.label_3.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Please report any issue to the email. Don\'t call at peak times</p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#2e3436;\">Manager: P17-6133@nu.edu.pk , +923464646629</span></p></body></html>"))

    def userWelcome(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def messageFailure(self,title,message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Warning)
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()

    ### authenticate use and pin
    def loginCheck(self):
        username = self.line_cardNo.text()
        pin  = self.line_pin.text()
        d =self.data()
        # print(d)
        if username in d.keys() and pin in d[username]:
            print("Access Granted:")
            self.userWelcome()
        else:
            self.messageFailure("Access Not Granted","Contact bank in case of forgot PIN")

    def message_createAccount(self):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Warning)
        messageBox.setWindowTitle("Contact Bank")
        messageBox.setText("Please contact bank for activating new account or visit bank website\nwww.easylife-coding.com")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()
    def exit(self):
        print("GoodBye")
        sys.exit()
    def stop(self):
        self.terminate()
#### file handling, for getting user data ###
    def join(self):
        directory = "Data"
        name = "usersdata.csv"
        filename = os.path.join(directory, name)
        return filename

#when 1 is entered from main(login_user)
    def data(self):
        filename = self.join()
        d = {}
        with open(filename, "a") as ap:
            with open(filename, "r") as rd:
                    r = csv.reader(rd)
                    for us in r:
                            us[1] = us[1]
                            us[2] = float(us[2])
                            d[us[0]] = us[1],us[2]
                            # print(d)
                    return d










if __name__ == '__main__':
    import sys
    app= QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
