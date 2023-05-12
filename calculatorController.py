from PyQt5.QtWidgets import *
from calculatorGUI import *


class Controller(QMainWindow, Ui_MainWindow):
    """
    Controller class that contains the functionality of a Calculator.
    """
    def __init__(self):
        super().__init__()
        """
        Constructor that sets the buttons and displays of a Calculator
        """

        self.setupUi(self)

        self.numberDisplay.setText('')

        self.equalButton.clicked.connect(lambda: self.equal())
        self.clearButton.clicked.connect(lambda: self.clear())

        self.addButton.clicked.connect(lambda: self.addition())
        self.subtractButton.clicked.connect(lambda: self.subtraction())
        self.multiplyButton.clicked.connect(lambda: self.multiplication())
        self.divisionButton.clicked.connect(lambda: self.division())
        self.negativeButton.clicked.connect(lambda: self.negative())
        self.decimalButton.clicked.connect(lambda: self.decimal())

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

    def clear(self) -> None:
        """
        Clears the number display.
        """
        self.numberDisplay.setText('')

    def equal(self) -> None:
        """
        Performs the calculations and displays the results.
        """
        try:
            equation = self.numberDisplay.toPlainText().split()
            print(equation)
            equation_funt = []
            equation_num = []

            num = 0
            while num < len(equation):
                print(len(equation))
                x = equation[num]

                if x.lstrip('-').isdigit():
                    if x == '-0':
                        raise RuntimeError
                    equation_num.append(float(x))

                elif '.' in x:
                    equation_num.append(float(x))
                elif x == '+':
                    equation_funt.append(0)
                elif x == '-':
                    equation_funt.append(1)
                elif x == 'x':
                    equation_funt.append(2)
                elif x == '/':
                    equation_funt.append(3)
                else:
                    raise RuntimeError

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
                        if n2 != 0:
                            total = n1 / n2
                        else:
                            raise RuntimeError

                    n1 = total
                    n += 1

                if '.' in str(total):
                    if str(total).endswith('.0'):
                        total = round(total)

                self.numberDisplay.setText(f'{total}')
        except RuntimeError:
            self.numberDisplay.setText('INVALID')

    def division(self) -> str:
        """
        Adds a division symbol to the number display and handles
        the ZeroDivisionError by setting the number display to 'cannot divide by zero'.
        """
        try:
            display = self.numberDisplay.toPlainText()
            display += ' / '
            self.numberDisplay.setText(display)

        except ZeroDivisionError:
            self.numberDisplay.setText('cannot divide by zero')

    def multiplication(self) -> str:
        """
        Adds a multiplication symbol to the number display.
        """
        display = self.numberDisplay.toPlainText()
        display += ' x '
        self.numberDisplay.setText(display)

    def subtraction(self) -> str:
        """
        Adds a subtraction symbol to the number display.
        """
        display = self.numberDisplay.toPlainText()
        display += ' - '
        self.numberDisplay.setText(display)

    def addition(self) -> str:
        """
        Adds an addition symbol to the number display.
        """
        display = self.numberDisplay.toPlainText()
        display += ' + '
        self.numberDisplay.setText(display)

    def zero(self) -> str:
        """
        Displays the number 0.
        """
        display = self.numberDisplay.toPlainText()
        display += '0'
        self.numberDisplay.setText(display)

    def one(self) -> str:
        """
        Displays the number 1.
        """
        display = self.numberDisplay.toPlainText()
        display += '1'
        self.numberDisplay.setText(display)

    def two(self) -> str:
        """
        Displays the number 2.
        """
        display = self.numberDisplay.toPlainText()
        display += '2'
        self.numberDisplay.setText(display)

    def three(self) -> str:
        """
        Displays the number 3.
        """
        display = self.numberDisplay.toPlainText()
        display += '3'
        self.numberDisplay.setText(display)

    def four(self) -> str:
        """
        Displays the number 4.
        """
        display = self.numberDisplay.toPlainText()
        display += '4'
        self.numberDisplay.setText(display)

    def five(self) -> str:
        """
        Displays the number 5.
        """
        display = self.numberDisplay.toPlainText()
        display += '5'
        self.numberDisplay.setText(display)

    def six(self) -> str:
        """
        Displays the number 6.
        """
        display = self.numberDisplay.toPlainText()
        display += '6'
        self.numberDisplay.setText(display)

    def seven(self) -> str:
        """
        Displays the number 7.
        """
        display = self.numberDisplay.toPlainText()
        display += '7'
        self.numberDisplay.setText(display)

    def eight(self) -> str:
        """
        Displays the number 8.
        """
        display = self.numberDisplay.toPlainText()
        display += '8'
        self.numberDisplay.setText(display)

    def nine(self) -> str:
        """
        Displays the number 9.
        """
        display = self.numberDisplay.toPlainText()
        display += '9'
        self.numberDisplay.setText(display)

    def negative(self) -> None:
        """
        If empty, displays the negative symbol when clicked.
        """
        display = self.numberDisplay.toPlainText()
        display2 = display.split()
        print(display2)
        if display2 == []:
            self.numberDisplay.setText("-")
        elif '-' in display2[len(display2) - 1]:
            pass
        else:
            final_display = ''
            neg_check = display2[(len(display2) - 1)]
            print(display2)

            if neg_check == '+':
                self.numberDisplay.setText(f'{display} -')
            elif neg_check == '-':
                pass
            elif neg_check == "x":
                self.numberDisplay.setText(f'{display} -')
            elif neg_check == "/":
                self.numberDisplay.setText(f'{display} -')
            elif neg_check == 0:
                final_display += f'-{neg_check}'
            else:
                neg_check = f'-{neg_check}'

                display2.pop(len(display2) - 1)
                num = 0
                while num < len(display2):
                    final_display += display2[num]
                    final_display += ' '
                    num += 1
                final_display += f'{neg_check}'
                print(neg_check)
                self.numberDisplay.setText(final_display)

    def decimal(self) -> None:
        """
        Displays the decimal symbol if clicked. Returns invalid if it's placed after an operator.
        """
        display = self.numberDisplay.toPlainText()
        display2 = display.split()
        decimal_check = display2[(len(display2) - 1)]
        print(decimal_check)
        deci = False

        if '.' in decimal_check:
            deci = True
            self.numberDisplay.setText(display)
        elif decimal_check == '+':
            deci = True
            self.numberDisplay.setText("INVALID")
        elif decimal_check == '-':
            deci = True
            self.numberDisplay.setText("INVALID")
        elif decimal_check == 'x':
            deci = True
            self.numberDisplay.setText("INVALID")
        elif decimal_check == '/':
            deci = True
            self.numberDisplay.setText("INVALID")

        print(deci)

        if deci == False:
            final_display = ''
            num = 0
            while num < (len(display2) - 1):
                final_display += display2[num]
                final_display += ' '
                num += 1
            final_display += f'{display2[num]}.'
            self.numberDisplay.setText(final_display)
