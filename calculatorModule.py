class Formulas:
    def division(self):
        try:
            display = self.numberDisplay.toPlainText()
            display += ' / '
            self.numberDisplay.setText(display)

        except ZeroDivisionError:
            self.numberDisplay.setText('cannot divide by zero')

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