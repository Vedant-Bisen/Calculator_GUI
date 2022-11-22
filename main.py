import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setGeometry(1400, 300, 400, 500)
        self.setWindowTitle("Calculator")
        self.initUI()
        self.buttons()

    def initUI(self):
        self.textbox = QtWidgets.QLabel(self)
        self.textbox.setGeometry(100, 200, 200, 50)
        self.textbox.setStyleSheet("border : 1px solid black")
        self.textbox.setText("0")

        self.acc = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = ""

    def buttons(self):
        self.button0 = QtWidgets.QPushButton(self)
        self.button0.setGeometry(100, 400, 50, 50)
        self.button0.setText("0")
        self.button0.clicked.connect(self.but0)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(100, 350, 50, 50)
        self.button1.setText("1")
        self.button1.clicked.connect(self.but1)

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setGeometry(150, 350, 50, 50)
        self.button2.setText("2")
        self.button2.clicked.connect(self.but2)

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setGeometry(200, 350, 50, 50)
        self.button3.setText("3")
        self.button3.clicked.connect(self.but3)

        self.button4 = QtWidgets.QPushButton(self)
        self.button4.setGeometry(100, 300, 50, 50)
        self.button4.setText("4")
        self.button4.clicked.connect(self.but4)

        self.button5 = QtWidgets.QPushButton(self)
        self.button5.setGeometry(150, 300, 50, 50)
        self.button5.setText("5")
        self.button5.clicked.connect(self.but5)
        
        self.button6 = QtWidgets.QPushButton(self)
        self.button6.setGeometry(200, 300, 50, 50)
        self.button6.setText("6")
        self.button6.clicked.connect(self.but6)

        self.button7 = QtWidgets.QPushButton(self)
        self.button7.setGeometry(100, 250, 50, 50)
        self.button7.setText("7")
        self.button7.clicked.connect(self.but7)

        self.button8 = QtWidgets.QPushButton(self)
        self.button8.setGeometry(150, 250, 50, 50)
        self.button8.setText("8")
        self.button8.clicked.connect(self.but8)

        self.button9 = QtWidgets.QPushButton(self)
        self.button9.setGeometry(200, 250, 50, 50)
        self.button9.setText("9")
        self.button9.clicked.connect(self.but9)

        self.button_enter = QtWidgets.QPushButton(self)
        self.button_enter.setGeometry(150, 400, 100, 50)
        self.button_enter.setText("Enter")
        self.button_enter.clicked.connect(self.but_enter)

        self.button_plus = QtWidgets.QPushButton(self)
        self.button_plus.setGeometry(250, 400, 50, 50)
        self.button_plus.setText("+")
        self.button_plus.clicked.connect(self.but_add)

        self.button_minus = QtWidgets.QPushButton(self)
        self.button_minus.setGeometry(250, 350, 50, 50)
        self.button_minus.setText("-")
        self.button_minus.clicked.connect(self.but_min)

        self.button_multi = QtWidgets.QPushButton(self)
        self.button_multi.setGeometry(250, 300, 50, 50)
        self.button_multi.setText("x")
        self.button_multi.clicked.connect(self.but_multi)

        self.button_div = QtWidgets.QPushButton(self)
        self.button_div.setGeometry(250, 250, 50, 50)
        self.button_div.setText("/")
        self.button_div.clicked.connect(self.but_div)

        self.button_clear = QtWidgets.QPushButton(self)
        self.button_clear.setGeometry(100, 450, 200, 50)
        self.button_clear.setText("Clear")
        self.button_clear.clicked.connect(self.but_clear)

    def but0(self):
        self.flag1 = str(self.acc)+str(0)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but1(self):
        self.flag1 = str(self.acc)+str(1)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))
        
    def but2(self):
        self.flag1 = str(self.acc)+str(2)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but3(self):
        self.flag1 = str(self.acc)+str(3)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but4(self):
        self.flag1 = str(self.acc)+str(4)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but5(self):
        self.flag1 = str(self.acc)+str(5)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but6(self):
        self.flag1 = str(self.acc)+str(6)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but7(self):
        self.flag1 = str(self.acc)+str(7)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but8(self):
        self.flag1 = str(self.acc)+str(8)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but9(self):
        self.flag1 = str(self.acc)+str(0)
        self.acc = int(self.flag1)
        self.flag1 = 0
        self.textbox.setText(str(self.acc))

    def but_add(self):
        if self.acc == 0:
            self.textbox.setText("Please enter a num first!")
        else:
            self.but_enter()
            self.flag3 = "add"
            self.acc = 0

    def but_min(self):
        if self.acc == 0:
            self.textbox.setText("Please enter a num first!")
        else:
            self.but_enter()
            self.flag3 = "sub"
            self.acc = 0

    def but_multi(self):
        if self.acc == 0:
            self.textbox.setText("Please enter a num first!")
        else:
            self.but_enter()
            self.flag3 = "mul"
            self.acc = 0

    def but_div(self):
        if self.acc == 0:
            self.textbox.setText("Please enter a num first!")
        else:
            self.but_enter()
            self.flag3 = "div"
            self.acc = 0

    def but_enter(self):
        if self.flag3 == "add":
            self.flag2 += self.acc
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""

        elif self.flag3 == "sub":
            self.flag2 -= self.acc
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""

        elif self.flag3 == "mul":
            self.flag2 *= self.acc
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""

        elif self.flag3 == "div":
            if self.acc == 0:
                self.textbox.setText("Cannot Divide by zero!")
            else:
                self.flag2 /= self.acc
                self.textbox.setText(str(self.flag2))
                self.flag3 = ""

        else:
            self.flag2 = self.acc
        
    def but_clear(self):
        self.textbox.setText(" ")
        self.acc = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = ""

def main():
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()