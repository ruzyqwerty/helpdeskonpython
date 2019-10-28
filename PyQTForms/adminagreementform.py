from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox


class AdminAgreementForm(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.parentform = args[0]
        uic.loadUi('PyQTForms/AdminAgreementForm.ui', self)

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
