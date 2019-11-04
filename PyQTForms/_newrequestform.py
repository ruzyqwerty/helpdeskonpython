# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewRequestForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(264, 174)
        Dialog.setMaximumSize(QtCore.QSize(5555, 5555))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        Dialog.setFont(font)
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setGeometry(QtCore.QRect(20, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(140, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName("btnCancel")
        self.leRequestName = QtWidgets.QLineEdit(Dialog)
        self.leRequestName.setGeometry(QtCore.QRect(20, 30, 231, 20))
        self.leRequestName.setObjectName("leRequestName")
        self.lblReqName = QtWidgets.QLabel(Dialog)
        self.lblReqName.setGeometry(QtCore.QRect(20, 10, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblReqName.setFont(font)
        self.lblReqName.setObjectName("lblReqName")
        self.lblErrors = QtWidgets.QLabel(Dialog)
        self.lblErrors.setGeometry(QtCore.QRect(20, 110, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblErrors.setFont(font)
        self.lblErrors.setText("")
        self.lblErrors.setObjectName("lblErrors")
        self.dteDeadline = QtWidgets.QDateTimeEdit(Dialog)
        self.dteDeadline.setGeometry(QtCore.QRect(20, 80, 231, 22))
        self.dteDeadline.setObjectName("dteDeadline")
        self.lblDeadline = QtWidgets.QLabel(Dialog)
        self.lblDeadline.setGeometry(QtCore.QRect(20, 60, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDeadline.setFont(font)
        self.lblDeadline.setObjectName("lblDeadline")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление нового запроса"))
        self.btnAdd.setText(_translate("Dialog", "Добавить"))
        self.btnCancel.setText(_translate("Dialog", "Отмена"))
        self.lblReqName.setText(_translate("Dialog", "Название запроса"))
        self.lblDeadline.setText(_translate("Dialog", "Дедлайн"))
