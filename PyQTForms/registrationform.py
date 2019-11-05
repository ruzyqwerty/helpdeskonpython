from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQTForms.adminagreementform import AdminAgreementForm
from dbconnector import set_data, get_data
from PyQTForms._registrationform import Ui_Dialog


class RegistrationForm(QDialog, Ui_Dialog):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

        self.parentform = args[0]
        self.adminpermission = False
        self.btnCancel.clicked.connect(self.close)
        self.btnAdd.clicked.connect(self.AddUser)

    def AddUser(self):
        login = self.leLogin.text()
        login = "".join(c for c in login if c not in ("'"))
        self.leLogin.setText(login)
        password = self.lePassword.text()
        password = "".join(c for c in password if c not in ("'"))
        self.lePassword.setText(password)
        name = self.leName.text()
        name = "".join(c for c in name if c not in ("'"))
        self.leName.setText(name)
        phonenumber = self.lePhonenumber.text()
        phonenumber = "".join(c for c in phonenumber if c not in ("'"))
        self.lePhonenumber.setText(phonenumber)
        if login == "" or password == "" or name == "" or phonenumber == "":
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Некоторые поля пустые!")
            msg.setWindowTitle("Внимание!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            result = get_data("""
            SELECT * from users
            WHERE phonenumber == '{}'
            """.format(phonenumber))
            another = get_data("""
            SELECT * from users
            WHERE login == '{}'
            """.format(login))
            if len(result) + len(another) > 0:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Пользователь с таким номером телефона или логином существует!")
                msg.setWindowTitle("Ошибка!")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            else:
                if self.cbRole.currentText() == "admin":
                    if not self.adminpermission:
                        adminagreementform = AdminAgreementForm(self)
                        adminagreementform.exec_()
                        if self.adminpermission:
                            msg = QMessageBox(self)
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("Регистрация разрешена!")
                            msg.setWindowTitle("Внимание!")
                            msg.setStandardButtons(QMessageBox.Ok)
                            retval = msg.exec_()
                    else:
                        set_data("""
                                        INSERT INTO users(login, password, name, role, phonenumber)
                                        VALUES('{}', '{}', '{}', 'admin', '{}')    
                                        """.format(login, password, name, phonenumber))
                        self.parentform.SingUpEnd(login, password)
                        self.close()
                else:
                    set_data("""
                    INSERT INTO users(login, password, name, role, phonenumber)
                    VALUES('{}', '{}', '{}', 'user', '{}')    
                    """.format(login, password, name, phonenumber))
                    self.parentform.SingUpEnd(login, password)
                    self.close()

