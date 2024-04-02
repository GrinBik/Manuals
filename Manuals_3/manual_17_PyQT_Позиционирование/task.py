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

        # Tabs
        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.setStyleSheet("font: 22px")

        # Move
        move = QWidget(self)
        btn = QPushButton(move)
        btn.setText("Кнопка")
        btn.move(200, 200)

        tabs.addTab(move, '.move()')

        # QVBoxLayout, QHBoxLayout
        layout = QVBoxLayout()
        inner = QHBoxLayout()
        for color in ('red', 'orange', 'yellow', 'green'):
            inner.addWidget(Color(color))
        layout.addLayout(inner)
        layout.addWidget(Color('orange'))
        layout.addWidget(Color('yellow'))
        widget = QWidget()
        widget.setLayout(layout)

        tabs.addTab(widget, 'H-box/V-box')

        # Grid
        grid = QGridLayout()
        grid.addWidget(Color('red'), 0, 3)
        grid.addWidget(Color('green'), 1, 1)
        grid.addWidget(Color('blue'), 2, 2)
        grid.addWidget(Color('purple'), 3, 0)
        widget = QWidget()
        widget.setLayout(grid)

        tabs.addTab(widget, 'Grid')

        self.setCentralWidget(tabs)

    def initUI(self):
        self.setGeometry(150, 200, 600, 600)
        self.setWindowTitle('Colors')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
