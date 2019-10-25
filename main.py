import sys
from PyQTForms.mainmenu import QApplication, MainMenuForm

app = QApplication(sys.argv)
mainmenuform = MainMenuForm()
mainmenuform.show()
sys.exit(app.exec_())
