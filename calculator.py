from calculatorController import *

def main():
    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Calculator')
    window.geometry()
    window.resize(False, False)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
