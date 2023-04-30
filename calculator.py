from calculatorGUI import *

def main():
    MainWindow = Tk()
    MainWindow.geometry('500x600')
    MainWindow.resizable(False, False)

    Ui_MainWindow(MainWindow)
    MainWindow.mainloop()

if __name__ == '__main__':
    main()