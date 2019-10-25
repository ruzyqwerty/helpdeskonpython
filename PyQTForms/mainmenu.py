from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQTForms.loginform import LoginForm
from os.path import exists
from dbconnector import get_data

PATH = "auto_login.txt"


class MainMenuForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = None
        uic.loadUi('PyQTForms/MainMenuForm.ui', self)
        if exists(PATH):
            with open(PATH, mode="r") as auto_login:
                data = auto_login.read()
                data = data.split(';')
                data.pop(-1)
                self.Login(data)
        else:
            login_form = LoginForm(self)
            login_form.exec_()

    def Login(self, user):
        if user is not None:
            self.lblName.setText("Привет, {} - {}!".format(user[4], user[3]))
            self.user = user
            with open(PATH, mode="w") as auto_login:
                for element in self.user:
                    auto_login.write(str(element) + ";")
            self.UpdateDataGridView()
        else:
            self.deleteLater()

    def UpdateDataGridView(self):
        if self.user[4] == "admin":
            data = get_data("""
            SELECT * from requests
            """)
        else:
            data = get_data("""
            SELECT * from requests
            WHERE request_creator == {}
            """.format(self.user[0]))
        self.dgvRequests.setRowCount(len(data))
        self.dgvRequests.setColumnCount(3)
        self.dgvRequests.setHorizontalHeaderLabels(["Название", "Кто сделал?", "Сделано?"])
        for row in data:
            inx = data.index(row)
            self.dgvRequests.setItem(inx, 0, QTableWidgetItem(row[1]))
            who_done = get_data("""
            SELECT * from users
            WHERE id = {}
            """.format(row[2]))[0][3]
            self.dgvRequests.setItem(inx, 1, QTableWidgetItem(who_done))
            self.dgvRequests.setItem(inx, 2, QTableWidgetItem(row[3]))




