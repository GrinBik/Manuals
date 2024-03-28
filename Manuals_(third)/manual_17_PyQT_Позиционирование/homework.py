# Создать окно, использующее относительное позиционирование по макету QGridLayout.
# Заполнить макет разноцветными квадратами так, чтобы получилась шахматная доска.
import sys
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QGridLayout
from PyQt6.QtWidgets import QTabWidget, QPushButton
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        grid = QGridLayout()
        color = ['white', 'black']
        for i in range(8):
            for j in range(8):
                grid.addWidget(Color(color[(i+j) % 2]), i, j)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def initUI(self):
        self.setGeometry(150, 200, 600, 600)
        self.setWindowTitle('Colors')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
