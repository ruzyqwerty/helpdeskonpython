from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQTForms.registrationform import RegistrationForm
from dbconnector import get_data


class LoginForm(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.parentform = args[0]
        self.GoodExit = False
        uic.loadUi('PyQTForms/LoginForm.ui', self)

        self.btnCancel.clicked.connect(self.Close)
        self.btnLogin.clicked.connect(self.Login)
        self.btnSignUp.clicked.connect(self.SignUp)

    def SignUp(self):
        registration_form = RegistrationForm(self)
        registration_form.exec_()

    def SingUpEnd(self, login, password):
        self.leLogin.setText(login)
        self.lePassword.setText(password)

    def Login(self):
        login = self.leLogin.text()
        login = "".join(c for c in login if c not in ("'"))
        self.leLogin.setText(login)
        password = self.lePassword.text()
        password = "".join(c for c in password if c not in ("'"))
        self.lePassword.setText(password)
        if login == '' or password == '':
            self.lblErrors.setText("Не все поля заполнены.")
        else:
            users = get_data("""
            SELECT * from users
            WHERE login = '{}'
            AND
            password = '{}'
            """.format(login, password))
            if len(users) == 0:
                self.lblErrors.setText("Не верный логин или пароль.")
            else:
                self.parentform.Login(users[0])
                self.GoodExit = True
                self.close()

    def closeEvent(self, event):
        if not self.GoodExit:
            self.parentform.Login(None)
        self.close()

    def Close(self):
        self.parentform.Login(None)
        self.close()


