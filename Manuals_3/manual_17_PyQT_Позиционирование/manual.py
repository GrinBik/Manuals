import sys
from PyQt6.QtWidgets import QMainWindow, QStackedLayout, QHBoxLayout, QVBoxLayout, QApplication, QWidget, QGridLayout
from PyQt6.QtWidgets import QTabWidget
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

        # widget = Color('red')
        # self.setCentralWidget(widget)

        layout = QVBoxLayout()

        inner = QHBoxLayout()
        for color in ('red', 'orange', 'yellow', 'green'):
            inner.addWidget(Color(color))
        layout.addLayout(inner)

        layout.addWidget(Color('red'))
        layout.setSpacing(5)
        layout.addWidget(Color('orange'))
        layout.addWidget(Color('yellow'))

        inner_2 = QGridLayout()
        inner_2.addWidget(Color('red'), 0, 3)
        inner_2.addWidget(Color('green'), 1, 1)
        inner_2.addWidget(Color('blue'), 2, 2)
        inner_2.addWidget(Color('purple'), 3, 0)
        inner_2.setSpacing(0)
        layout.addLayout(inner_2)

        layout.addWidget(Color('green'))
        layout.addWidget(Color('#4286f4'))
        layout.addWidget(Color('blue'))

        inner_3 = QStackedLayout()
        inner_3.addWidget(Color("red"))
        inner_3.addWidget(Color("green"))
        inner_3.addWidget(Color("blue"))
        inner_3.addWidget(Color("yellow"))
        inner_3.setCurrentIndex(2)
        # layout.addLayout(inner_3)

        layout.addWidget(Color('purple'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        tabs = QTabWidget()
        tabs.setMovable(True)
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
        # self.setCentralWidget(tabs)

    def initUI(self):
        self.setGeometry(150, 200, 600, 600)
        self.setWindowTitle('Colors')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
