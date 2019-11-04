# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 117)
        Dialog.setMaximumSize(QtCore.QSize(343, 117))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.leLogin = QtWidgets.QLineEdit(Dialog)
        self.leLogin.setGeometry(QtCore.QRect(20, 30, 141, 20))
        self.leLogin.setObjectName("leLogin")
        self.lblLogin = QtWidgets.QLabel(Dialog)
        self.lblLogin.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.lblLogin.setObjectName("lblLogin")
        self.lblPassword = QtWidgets.QLabel(Dialog)
        self.lblPassword.setGeometry(QtCore.QRect(180, 10, 131, 16))
        self.lblPassword.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblPassword.setObjectName("lblPassword")
        self.lePassword = QtWidgets.QLineEdit(Dialog)
        self.lePassword.setGeometry(QtCore.QRect(180, 30, 141, 20))
        self.lePassword.setObjectName("lePassword")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(20, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnSignUp = QtWidgets.QPushButton(Dialog)
        self.btnSignUp.setGeometry(QtCore.QRect(110, 80, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setObjectName("btnSignUp")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(240, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.lblErrors = QtWidgets.QLabel(Dialog)
        self.lblErrors.setGeometry(QtCore.QRect(20, 60, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblErrors.setFont(font)
        self.lblErrors.setText("")
        self.lblErrors.setObjectName("lblErrors")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Окно входа"))
        self.lblLogin.setText(_translate("Dialog", "Логин"))
        self.lblPassword.setText(_translate("Dialog", "Пароль"))
        self.btnLogin.setText(_translate("Dialog", "Войти"))
        self.btnSignUp.setText(_translate("Dialog", "Зарегистрироваться"))
        self.btnCancel.setText(_translate("Dialog", "Отмена"))
