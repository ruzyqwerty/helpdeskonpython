from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QDateTime


class NewRequestForm(QDialog):
    def __init__(self, *args):
        super().__init__()
        self.parentform = args[0]
        uic.loadUi('PyQTForms/NewRequestForm.ui', self)

        self.dteDeadline.setMinimumDateTime(QDateTime.currentDateTime())
        self.btnCancel.clicked.connect(self.close)
        self.btnAdd.clicked.connect(self.AddRequest)

    def AddRequest(self):
        name = self.leRequestName.text()
        name = "".join(c for c in name if c not in ("'"))
        self.leRequestName.setText(name)
        time = self.dteDeadline.text()
        if name == "":
            self.lblErrors.setText("Поле пустое, введите название запроса.")
        else:
            self.parentform.AddRequest(name, time)
            self.close()



