from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class AboutProgramForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('PyQTForms/AboutProgramForm.ui', self)

    def Secret(self):
        pass #  TODO: Сделать пасхалку