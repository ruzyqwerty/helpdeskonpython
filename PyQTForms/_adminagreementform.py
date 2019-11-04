# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAgreementForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(312, 113)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.lblKey = QtWidgets.QLabel(Dialog)
        self.lblKey.setGeometry(QtCore.QRect(10, 10, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lblKey.setFont(font)
        self.lblKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKey.setWordWrap(True)
        self.lblKey.setObjectName("lblKey")
        self.leKey = QtWidgets.QLineEdit(Dialog)
        self.leKey.setGeometry(QtCore.QRect(20, 40, 271, 20))
        self.leKey.setObjectName("leKey")
        self.btnAccept = QtWidgets.QPushButton(Dialog)
        self.btnAccept.setGeometry(QtCore.QRect(20, 70, 131, 31))
        self.btnAccept.setObjectName("btnAccept")
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setGeometry(QtCore.QRect(160, 70, 131, 31))
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Подтверждения админа"))
        self.lblKey.setText(_translate("Dialog", "Введите ключ регистрации нового админа:"))
        self.btnAccept.setText(_translate("Dialog", "Подтвердить"))
        self.btnCancel.setText(_translate("Dialog", "Отмена"))
