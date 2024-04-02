from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Login")
        # self.setGeometry(300, 250, 350, 500)
        self.setFixedSize(500, 300)

        self.text = QtWidgets.QLabel("Введите логин", self)
        self.text.move(10, 10)
        # self.text.setFixedWidth(50)
        self.text.adjustSize()

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Войти")
        self.btn1.move(0, 30)
        self.btn1.clicked.connect(self.command)

    def command(self):
        print(1)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
