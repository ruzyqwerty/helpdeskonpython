from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQTForms._aboutprogramform import Ui_Form


class AboutProgramForm(QWidget, Ui_Form):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)

    def Secret(self):
        pass #  TODO: Сделать пасхалку