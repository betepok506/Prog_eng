from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Задание Названия главного окна
        self.title = "Главная форма"
        # Объявление параметров Размеров окна
        self.top = 200
        self.left = 500
        self.width = 750
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        font_size = 25
        tEdit_height = 60
        tEdit_width = 160
        self.tEdit_mn1 = QLineEdit('',self)
        self.tEdit_mn1.setGeometry(75,75,tEdit_width,tEdit_height)
        font = self.tEdit_mn1.font()
        font.setPointSize(font_size)
        self.tEdit_mn1.setFont(font)

        self.tEdit_mn2 = QLineEdit('', self)
        self.tEdit_mn2.setGeometry(300, 75, tEdit_width, tEdit_height)
        font = self.tEdit_mn2.font()
        font.setPointSize(font_size)
        self.tEdit_mn2.setFont(font)

        self.tEdit_rez = QLineEdit('', self)
        self.tEdit_rez.setGeometry(525, 75, tEdit_width, tEdit_height)
        self.tEdit_rez.setReadOnly(True)
        font = self.tEdit_mn2.font()
        font.setPointSize(font_size)
        self.tEdit_rez.setFont(font)

        self.button = QPushButton('Посчитать', self)
        self.button.setGeometry(320, 200,100,50)
        self.button.clicked.connect(self.buttonClicked1)

        self.label_mul = QLabel(self)
        self.label_mul.setText('x')
        self.label_mul.setGeometry(260,70,40,tEdit_height)
        font = self.label_mul.font()
        font.setPointSize(font_size)
        self.label_mul.setFont(font)

        self.label_res = QLabel(self)
        self.label_res.setText('=')
        self.label_res.setGeometry(485, 70, 40, tEdit_height)
        font = self.label_res.font()
        font.setPointSize(font_size)
        self.label_res.setFont(font)

        self.show()


    def buttonClicked1(self):
        try:
            num1 = int(self.tEdit_mn1.text())
        except:
            QMessageBox.critical(self, "Ошибка", f"Первый операнд некорректный", QMessageBox.Ok)

            return
        try:
            num2 = int(self.tEdit_mn2.text())
        except:
            QMessageBox.critical(self, "Ошибка", f"Второй операнд некорректный", QMessageBox.Ok)
            return

        if num1<100 and num2<100:
            self.tEdit_rez.setText(f'{num1*num2}')
        else:
            QMessageBox.critical(self, "Ошибка", f"Числа слишком большие", QMessageBox.Ok)
            return


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())