from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQTForms._adminagreementform import Ui_Dialog


class AdminAgreementForm(QDialog, Ui_Dialog):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.parentform = args[0]

        self.btnCancel.clicked.connect(self.close)
        self.btnAccept.clicked.connect(self.AcceptKey)

    def AcceptKey(self):
        key = self.leKey.text()
        if key == "In-My-Heart-Omsk":
            self.parentform.adminpermission = True
            self.close()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Неверный ключ регистрации!")
            msg.setWindowTitle("Внимание, Омск!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
