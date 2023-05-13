from calculatorController import *

def main():
    app = QApplication([])
    window = Controller()
    window.geometry()
    window.setWindowTitle('Calculator')
    window.resize(False, False)
    window.show()
    app.exec_()





if __name__ == '__main__':
    main()