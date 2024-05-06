import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow

class CalculatorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.current_expression = ""
        
    

    def init_UI(self):
         self.ui.push_0.clicked.connect(lambda: self.add_num("0"))
         self.ui.push_1.clicked.connect(lambda: self.add_num("1"))
         self.ui.push_2.clicked.connect(lambda: self.add_num("2"))
         self.ui.push_3.clicked.connect(lambda: self.add_num("3"))
         self.ui.push_4.clicked.connect(lambda: self.add_num("4"))
         self.ui.push_5.clicked.connect(lambda: self.add_num("5"))
         self.ui.push_6.clicked.connect(lambda: self.add_num("6"))
         self.ui.push_7.clicked.connect(lambda: self.add_num("7"))
         self.ui.push_8.clicked.connect(lambda: self.add_num("8"))
         self.ui.push_9.clicked.connect(lambda: self.add_num("9"))

         self.ui.push_del.clicked.connect(self.del_num)
         self.ui.push_clear.clicked.connect(self.clear_label)
         self.ui.pushButton_19.clicked.connect(self.add_point)

         self.ui.push_plus.clicked.connect(lambda: self.add_sign("+"))
         self.ui.push_minus.clicked.connect(lambda: self.add_sign("-"))
         self.ui.push_multiply.clicked.connect(lambda: self.add_sign("*"))
         self.ui.push_share.clicked.connect(lambda: self.add_sign("/"))

         self.ui.pushButton_20.clicked.connect(self.decision)
    

    def add_num(self, value: str):
        if self.ui.label.text() == "":
            self.ui.label.setText(value)
        else:
            self.ui.label.setText(self.ui.label.text() + value)
    
    def clear_label(self) -> None:
        self.ui.label.clear()
    
    def add_point(self) -> None:
        if "." not in self.ui.label.text() and self.ui.label.text() != "":
            self.ui.label.setText(self.ui.label.text() + ".")

    def add_sign(self, math_sign: str):
        if self.ui.label.text():
            text = self.ui.label.text()
            if text:
                last_char = text[-1]
                if last_char in ('+', '-', '*', '/'):
                    self.del_num()
                    self.ui.label.setText(self.ui.label.text() + math_sign)
                else:
                    self.ui.label.setText(self.ui.label.text() + math_sign)
    
    def decision(self) -> None:
        if self.ui.label.text():
            decision_num = self.ui.label.text()
            last_char = decision_num[-1]
            if last_char not in ('+', '-', '*', '/'):
                parts = decision_num.split('/')
                for i in range(1, len(parts)):
                    if float(parts[i]) == 0:
                        self.ui.label.clear()
                        self.ui.label.setText("На ноль делить нельзя!!!")
                        return
                decision_num = eval(decision_num)
                self.ui.label.clear()
                self.ui.label.setText(str(decision_num))

    def del_num(self) -> None:
        text = self.ui.label.text()
        new_text = text[:-1]
        self.ui.label.setText(new_text)


app = QtWidgets.QApplication([])
application = CalculatorApp()
application.show()
sys.exit(app.exec())