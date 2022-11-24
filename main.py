import sys,math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()                           #Initialising new window
        self.setGeometry(1400, 300, 400, 500)                       #Setting window geometry
        self.setWindowTitle("Calculator")                           #Setting window title
        self.initUI()                                               #Calling init UI    
        self.buttonsUI()                                            #Calling buttons UI

    def initUI(self):
        self.textbox = QtWidgets.QLabel(self)                       #Creating textbox to show output
        self.textbox.setGeometry(100, 200, 200, 50)
        self.textbox.setStyleSheet("border : 1px solid black")      #1px border to textbox
        self.textbox.setText("0")

        self.acc = 0                                                #Creating acc
        self.flag1 = 0                                              #flag1 to store values when writing numbers
        self.flag2 = 0                                              #flag2 to store values when operants are applied
        self.flag3 = ""                                             #flag3 to store values of the prev operant 
        self.flag4 = "close"

    def buttonsUI(self):
        self.button0 = QtWidgets.QPushButton(self)                  #Creating button  
        self.button0.setGeometry(100, 400, 50, 50)                  #Settign geometry to button
        self.button0.setText("0")                                   #Setting text to button 
        self.button0.clicked.connect(self.but0)                     #Connecting button to function

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
        
        self.button_sin = QtWidgets.QPushButton(self)                                 
        self.button_sin.setGeometry(50, 250, 50, 50)                  
        self.button_sin.setText("sin")                                   
        self.button_sin.clicked.connect(self.but_sin)
        
        self.button_cos = QtWidgets.QPushButton(self)                                 
        self.button_cos.setGeometry(50, 300, 50, 50)                  
        self.button_cos.setText("cos")                                   
        self.button_cos.clicked.connect(self.but1) 
        
        self.button_tan = QtWidgets.QPushButton(self)                                 
        self.button_tan.setGeometry(50, 350, 50, 50)                  
        self.button_tan.setText("tan")                                   
        self.button_tan.clicked.connect(self.but1)

    def but0(self):
        self.flag1 = str(self.acc)+str(0)                           #Setting first flag to value in acc plus the cliked value
        self.acc = int(self.flag1)                                  #converting acc to the int of flag value added
        self.flag1 = 0                                              #Setting flag to 0
        self.textbox.setText(str(self.acc))                         #Displaying on textBox

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

    def but_clear(self):
        self.textbox.setText(" ")
        self.acc = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = ""

    def but_sin(self):
        self.but_enter()
        self.flag4 = "open"
        self.flag2 = float(math.sin(self.flag2))
        self.flag3 = "sin"
    
    def but_cos(self):
        self.but_enter()
        self.flag3 = float(math.cos(self.flag2))
        self.flag3 = "cos"
        
    def but_tan(self):
        self.but_enter()
        self.flag3 = float(math.tan(self.flag3))
        self.flag3 = "tan"

    def but_clear(self):
        self.textbox.setText(" ")
        self.acc = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = ""
       
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
                
        elif self.flag3 == "sin":
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""
        
        elif self.flag3 == "cos":
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""
            
        elif self.flag3 == "tan":
            self.textbox.setText(str(self.flag2))
            self.flag3 = ""

        else:
            self.flag2 = self.acc

            
def main():
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()