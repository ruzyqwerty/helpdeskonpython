from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQTForms.adminagreementform import AdminAgreementForm
from dbconnector import set_data, get_data


class RegistrationForm(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.parentform = args[0]
        self.adminpermission = False
        uic.loadUi('PyQTForms/RegistrationForm.ui', self)

        self.btnCancel.clicked.connect(self.close)
        self.btnAdd.clicked.connect(self.AddUser)

    def AddUser(self):
        login = self.leLogin.text()
        password = self.lePassword.text()
        name = self.leName.text()
        phonenumber = self.lePhonenumber.text()
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
            if len(result) > 0:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Пользователь с таким номером телефона существует!")
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

