# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistrationForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(382, 169)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.lblPassword = QtWidgets.QLabel(Dialog)
        self.lblPassword.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.lblPassword.setObjectName("lblPassword")
        self.lePassword = QtWidgets.QLineEdit(Dialog)
        self.lePassword.setGeometry(QtCore.QRect(210, 30, 161, 20))
        self.lePassword.setObjectName("lePassword")
        self.lblLogin = QtWidgets.QLabel(Dialog)
        self.lblLogin.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.lblLogin.setObjectName("lblLogin")
        self.leLogin = QtWidgets.QLineEdit(Dialog)
        self.leLogin.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.leLogin.setObjectName("leLogin")
        self.lblName = QtWidgets.QLabel(Dialog)
        self.lblName.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.lblName.setObjectName("lblName")
        self.lblPhonenumber = QtWidgets.QLabel(Dialog)
        self.lblPhonenumber.setGeometry(QtCore.QRect(210, 60, 191, 16))
        self.lblPhonenumber.setObjectName("lblPhonenumber")
        self.lePhonenumber = QtWidgets.QLineEdit(Dialog)
        self.lePhonenumber.setGeometry(QtCore.QRect(210, 80, 161, 20))
        self.lePhonenumber.setObjectName("lePhonenumber")
        self.leName = QtWidgets.QLineEdit(Dialog)
        self.leName.setGeometry(QtCore.QRect(10, 80, 191, 20))
        self.leName.setObjectName("leName")
        self.lblRole = QtWidgets.QLabel(Dialog)
        self.lblRole.setGeometry(QtCore.QRect(250, 110, 47, 13))
        self.lblRole.setObjectName("lblRole")
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setGeometry(QtCore.QRect(10, 110, 111, 51))
        self.btnAdd.setObjectName("btnAdd")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(130, 110, 111, 51))
        self.btnCancel.setObjectName("btnCancel")
        self.cbRole = QtWidgets.QComboBox(Dialog)
        self.cbRole.setGeometry(QtCore.QRect(250, 130, 121, 22))
        self.cbRole.setObjectName("cbRole")
        self.cbRole.addItem("")
        self.cbRole.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Окно регистрации"))
        self.lblPassword.setText(_translate("Dialog", "Пароль"))
        self.lblLogin.setText(_translate("Dialog", "Логин"))
        self.lblName.setText(_translate("Dialog", "Имя"))
        self.lblPhonenumber.setText(_translate("Dialog", "Номер телефона"))
        self.lblRole.setText(_translate("Dialog", "Роль"))
        self.btnAdd.setText(_translate("Dialog", "Добавить"))
        self.btnCancel.setText(_translate("Dialog", "Отмена"))
        self.cbRole.setItemText(0, _translate("Dialog", "admin"))
        self.cbRole.setItemText(1, _translate("Dialog", "user"))
