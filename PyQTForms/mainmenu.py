from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQTForms.loginform import LoginForm
from PyQTForms.newrequestform import NewRequestForm
from os.path import exists
from dbconnector import get_data, set_data

PATH = "auto_login.lgl"

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

        self.btnAddRequest.clicked.connect(self.OpenNewRequestForm)
        self.btnDeleteRequest.clicked.connect(self.DeleteRequest)
        self.btnUpdate.clicked.connect(self.UpdateDataGridView)
        self.btnDone.clicked.connect(self.Done)

    def Login(self, user):
        if user is not None:
            self.lblName.setText("Привет, {} - {}!".format(user[4], user[3]))
            self.user = user
            with open(PATH, mode="w") as auto_login:
                for element in self.user:
                    auto_login.write(str(element) + ";")
            self.UpdateDataGridView()
            self.btnDone.setEnabled(True)
        else:
            self.deleteLater()

    def OpenNewRequestForm(self):
        new_request_form = NewRequestForm(self)
        new_request_form.exec_()

    def AddRequest(self, request, time):
        set_data("""
        INSERT INTO requests(name, request_creator, deadline, done)
        VALUES('{}', {}, '{}', 'False')
        """.format(request, self.user[0], time))
        self.UpdateDataGridView()

    def DeleteRequest(self):
        request = self.dgvRequests.selectedItems()
        if len(request) > 0:
            name = request[0].text()
            phonenumber = request[2].text()
            deadline = request[3].text()
            done = request[4].text()
            if done == "Нет":
                done = "False"
            else:
                done = "True"
            all_requests = get_data("""
            SELECT * from requests
            WHERE name = '{}'
            AND
            done = '{}'
            AND
            deadline = '{}'
            AND request_creator in (
            SELECT id from users
            WHERE phonenumber = '{}')
            """.format(name, done, deadline, phonenumber))
            if len(all_requests) > 1:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("В базе данных нашлось больше одного запроса с таким именнем, будет удалён первый из них.")
                msg.setWindowTitle("Внимание!")
                msg.setStandardButtons(QMessageBox.Ok)

                retval = msg.exec_()
            if len(all_requests) == 1:
                request = all_requests[0]
                set_data("""
                DELETE from requests
                WHERE id = {}
                """.format(request[0]))
            else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Не было найдено таких заявок.")
                msg.setWindowTitle("Ошибка!")
                msg.setStandardButtons(QMessageBox.Ok)

                retval = msg.exec_()
            self.UpdateDataGridView()

    def UpdateDataGridView(self):
        titles = []
        if self.user[4] == "admin":
            titles = ["Название", "Кто сделал?", "Номер телефона", "Дедлайн", "Сделано?"]
            data = get_data("""
            SELECT * from requests
            """)
        else:
            data = get_data("""
            SELECT * from requests
            WHERE request_creator == {}
            """.format(self.user[0]))
            titles = ["Название", "Дедлайн", "Сделано?"]
        self.dgvRequests.setRowCount(len(data))
        self.dgvRequests.setColumnCount(len(titles))
        self.dgvRequests.setHorizontalHeaderLabels(titles)
        for row in data:
            inx = data.index(row)
            self.dgvRequests.setItem(inx, 0, QTableWidgetItem(row[1]))
            who_done, his_phonenumber = get_data("""
            SELECT name, phonenumber from users
            WHERE id = {}
            """.format(row[2]))[0]
            if self.user[4] == "admin":
                self.dgvRequests.setItem(inx, 1, QTableWidgetItem(who_done))
                self.dgvRequests.setItem(inx, 2, QTableWidgetItem(str(his_phonenumber)))
            statement = "Да"
            if row[4] == "False":
                statement = "Нет"
            self.dgvRequests.setItem(inx, len(titles) - 2, QTableWidgetItem(row[3]))
            self.dgvRequests.setItem(inx, len(titles) - 1, QTableWidgetItem(statement))

    def Done(self):
        request = self.dgvRequests.selectedItems()
        if len(request) > 0:
            name = request[0].text()
            phonenumber = request[2].text()
            deadline = request[3].text()
            done = request[4].text()
            if done == "Нет":
                done = "False"
            else:
                done = "True"
            all_requests = get_data("""
            SELECT * from requests
            WHERE name = '{}'
            AND
            done = '{}'
            AND
            deadline = '{}'
            AND request_creator in (
            SELECT id from users
            WHERE phonenumber = '{}')
            """.format(name, done, deadline, phonenumber))
            if len(all_requests) > 1:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("В базе данных нашлось больше одного запроса с таким именнем, будет изменён первый из них.")
                msg.setWindowTitle("Внимание!")
                msg.setStandardButtons(QMessageBox.Ok)

                retval = msg.exec_()
            if len(all_requests) == 1:
                request = all_requests[0]
                set_data("""
                UPDATE requests
                SET done = 'True'
                WHERE id = {}
                """.format(request[0]))
            else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Не было найдено таких заявок.")
                msg.setWindowTitle("Ошибка!")
                msg.setStandardButtons(QMessageBox.Ok)

                retval = msg.exec_()
            self.UpdateDataGridView()

