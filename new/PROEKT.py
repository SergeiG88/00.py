import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_Ui()

    def init_Ui(self):
        self.setWindowTitle('Ковертер валют')
        self.setWindowIcon(QIcon)

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
    
sys.exit(app.exec())