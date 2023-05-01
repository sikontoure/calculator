from PyQt5.QtWidgets import *
from calculatorGUI import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.numberDisplay.setText('')

        self.equalButton.clicked.connect(lambda: self.equal())
        self.clearButton.clicked.connect(lambda: self.clear())

        self.addButton.clicked.connect(lambda: self.addition())
        self.subtractButton.clicked.connect(lambda: self.subtraction())
        self.multiplyButton.clicked.connect(lambda: self.multiplication())
        self.divisionButton.clicked.connect(lambda: self.division())

        self.zeroButton.clicked.connect(lambda: self.zero())
        self.oneButton.clicked.connect(lambda: self.one())
        self.twoButton.clicked.connect(lambda: self.two())
        self.threeButton.clicked.connect(lambda: self.three())
        self.fourButton.clicked.connect(lambda: self.four())
        self.fiveButton.clicked.connect(lambda: self.five())
        self.sixButton.clicked.connect(lambda: self.six())
        self.sevenButton.clicked.connect(lambda: self.seven())
        self.eightButton.clicked.connect(lambda: self.eight())
        self.nineButton.clicked.connect(lambda: self.nine())

    def clear(self):
        self.numberDisplay.setText('')

    def equal(self):
        equation = self.numberDisplay.toPlainText().split()
        print(equation)
        equation_funt = []
        equation_num = []

        num = 0
        while num < len(equation):
            x = equation[num]

            if x.isdigit():
                equation_num.append(float(x))
            elif x == '+':
                equation_funt.append(0)
            elif x == '-':
                equation_funt.append(1)
            elif x == 'x':
                equation_funt.append(2)
            elif x == '/':
                equation_funt.append(3)

            num += 1
        print(equation_num)
        print(equation_funt)


        if len(equation_funt) >= len(equation_num):
            self.numberDisplay.setText('INVALID')

        else:
            n = 0
            total = 0
            n1 = equation_num[n]
            while n < (len(equation_num) - 1):
                n2 = equation_num[n + 1]
                if equation_funt[n] == 0:
                    total = n1 + n2
                elif equation_funt[n] == 1:
                    total = n1 - n2
                elif equation_funt[n] == 2:
                    total = n1 * n2
                elif equation_funt[n] == 3:
                    total = n1 / n2

                n1 = total
                n += 1


            total = round(total)
            self.numberDisplay.setText(f'{total}')

    def division(self):
        display = self.numberDisplay.toPlainText()
        display += ' / '
        self.numberDisplay.setText(display)

    def multiplication(self):
        display = self.numberDisplay.toPlainText()
        display += ' x '
        self.numberDisplay.setText(display)

    def subtraction(self):
        display = self.numberDisplay.toPlainText()
        display += ' - '
        self.numberDisplay.setText(display)

    def addition(self):
        display = self.numberDisplay.toPlainText()
        display += ' + '
        self.numberDisplay.setText(display)

    def zero(self):
        display = self.numberDisplay.toPlainText()
        display += '0'
        self.numberDisplay.setText(display)


    def one(self):
        display = self.numberDisplay.toPlainText()
        display += '1'
        self.numberDisplay.setText(display)


    def two(self):
        display = self.numberDisplay.toPlainText()
        display += '2'
        self.numberDisplay.setText(display)


    def three(self):
        display = self.numberDisplay.toPlainText()
        display += '3'
        self.numberDisplay.setText(display)


    def four(self):
        display = self.numberDisplay.toPlainText()
        display += '4'
        self.numberDisplay.setText(display)


    def five(self):
        display = self.numberDisplay.toPlainText()
        display += '5'
        self.numberDisplay.setText(display)


    def six(self):
        display = self.numberDisplay.toPlainText()
        display += '6'
        self.numberDisplay.setText(display)


    def seven(self):
        display = self.numberDisplay.toPlainText()
        display += '7'
        self.numberDisplay.setText(display)


    def eight(self):
        display = self.numberDisplay.toPlainText()
        display += '8'
        self.numberDisplay.setText(display)


    def nine(self):
        display = self.numberDisplay.toPlainText()
        display += '9'
        self.numberDisplay.setText(display)


    def negative(self, display):
        pass

    def decimal(self, display):
        pass
