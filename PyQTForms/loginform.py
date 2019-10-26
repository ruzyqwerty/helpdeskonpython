from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from dbconnector import get_data


class LoginForm(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.parentform = args[0]
        uic.loadUi('PyQTForms/LoginForm.ui', self)

        self.btnCancel.clicked.connect(self.Close)
        self.btnLogin.clicked.connect(self.Login)

    def Login(self):
        login = self.leLogin.text()
        password = self.lePassword.text()
        if login == '' or password == '':
            pass #TODO: Вывести ошибку, что поля не заполнены
        else:
            users = get_data("""
            SELECT * from users
            WHERE login = '{}'
            AND
            password = '{}'
            """.format(login, password))
            if len(users) == 0:
                pass #TODO: Вывести ошибку, что нет такого пользователя
            else:
                self.parentform.Login(users[0])
                self.close()

    def Close(self):
        self.parentform.Login(None)
        self.close()


