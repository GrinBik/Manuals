from PyQt6 import QtWidgets
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Ball")
        self.setStyleSheet("background-image: url(ball.jpg);border-image: url(ball.jpg);")
        self.setGeometry(800, 600, 150, 150)
        self.setFixedSize(150, 150)


def application():
    app = QtWidgets.QApplication(sys.argv)
    ball = Window()
    ball.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
