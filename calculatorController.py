from PyQt5.QtWidgets import *
from calculatorGUI import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


    def enter(self):
        pass

    def clear(self):
        pass

    def division(self):
        pass

    def multiplication(self):
        pass

    def subtraction(self):
        pass

    def addition(self):
        pass


