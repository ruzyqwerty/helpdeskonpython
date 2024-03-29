# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenuForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 369)
        MainWindow.setMaximumSize(QtCore.QSize(700, 369))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dgvRequests = QtWidgets.QTableWidget(self.centralwidget)
        self.dgvRequests.setGeometry(QtCore.QRect(10, 91, 621, 251))
        self.dgvRequests.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dgvRequests.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dgvRequests.setRowCount(1)
        self.dgvRequests.setColumnCount(5)
        self.dgvRequests.setObjectName("dgvRequests")
        self.dgvRequests.horizontalHeader().setCascadingSectionResizes(False)
        self.dgvRequests.horizontalHeader().setDefaultSectionSize(116)
        self.dgvRequests.horizontalHeader().setSortIndicatorShown(False)
        self.dgvRequests.horizontalHeader().setStretchLastSection(False)
        self.dgvRequests.verticalHeader().setVisible(True)
        self.dgvRequests.verticalHeader().setDefaultSectionSize(23)
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(10, 10, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.btnAddRequest = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddRequest.setGeometry(QtCore.QRect(10, 40, 121, 41))
        self.btnAddRequest.setObjectName("btnAddRequest")
        self.btnDeleteRequest = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteRequest.setGeometry(QtCore.QRect(140, 40, 121, 41))
        self.btnDeleteRequest.setObjectName("btnDeleteRequest")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(570, 50, 61, 31))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnDone = QtWidgets.QPushButton(self.centralwidget)
        self.btnDone.setEnabled(False)
        self.btnDone.setGeometry(QtCore.QRect(270, 40, 111, 41))
        self.btnDone.setObjectName("btnDone")
        self.leSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.leSearch.setGeometry(QtCore.QRect(390, 60, 171, 20))
        self.leSearch.setObjectName("leSearch")
        self.lblSearch = QtWidgets.QLabel(self.centralwidget)
        self.lblSearch.setGeometry(QtCore.QRect(390, 40, 171, 16))
        self.lblSearch.setObjectName("lblSearch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuRequests = QtWidgets.QMenu(self.menuBar)
        self.menuRequests.setObjectName("menuRequests")
        self.menuAbouta = QtWidgets.QMenu(self.menuBar)
        self.menuAbouta.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.menuAbouta.setFont(font)
        self.menuAbouta.setTearOffEnabled(False)
        self.menuAbouta.setObjectName("menuAbouta")
        self.menuSingOut = QtWidgets.QMenu(self.menuBar)
        self.menuSingOut.setObjectName("menuSingOut")
        MainWindow.setMenuBar(self.menuBar)
        self.menuAdd = QtWidgets.QAction(MainWindow)
        self.menuAdd.setObjectName("menuAdd")
        self.menuDelete = QtWidgets.QAction(MainWindow)
        self.menuDelete.setObjectName("menuDelete")
        self.menuDone = QtWidgets.QAction(MainWindow)
        self.menuDone.setObjectName("menuDone")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.menuAbout = QtWidgets.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuRequests.addAction(self.menuAdd)
        self.menuRequests.addAction(self.menuDelete)
        self.menuRequests.addAction(self.menuDone)
        self.menuAbouta.addAction(self.menuAbout)
        self.menuSingOut.addAction(self.menuExit)
        self.menuBar.addAction(self.menuRequests.menuAction())
        self.menuBar.addAction(self.menuSingOut.menuAction())
        self.menuBar.addAction(self.menuAbouta.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Helpdesk - Главное окно"))
        self.dgvRequests.setSortingEnabled(False)
        self.lblName.setText(_translate("MainWindow", "ТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТТЕСТ"))
        self.btnAddRequest.setText(_translate("MainWindow", "Добавить запрос"))
        self.btnDeleteRequest.setText(_translate("MainWindow", "Удалить запрос"))
        self.btnUpdate.setText(_translate("MainWindow", "Обновить"))
        self.btnDone.setText(_translate("MainWindow", "Сделано!"))
        self.lblSearch.setText(_translate("MainWindow", "Поиск по названию запроса."))
        self.menuRequests.setTitle(_translate("MainWindow", "Запросы"))
        self.menuAbouta.setTitle(_translate("MainWindow", "Об программе"))
        self.menuSingOut.setTitle(_translate("MainWindow", "Выход из учетной записи"))
        self.menuAdd.setText(_translate("MainWindow", "Добавить"))
        self.menuDelete.setText(_translate("MainWindow", "Удалить"))
        self.menuDone.setText(_translate("MainWindow", "Сделано"))
        self.action.setText(_translate("MainWindow", "Выйии"))
        self.menuExit.setText(_translate("MainWindow", "Выйти"))
        self.menuAbout.setText(_translate("MainWindow", "Почитать об программе"))
