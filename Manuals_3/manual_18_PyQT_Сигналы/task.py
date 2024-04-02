from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
import random
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 493)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.text_feild = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.text_feild.setGeometry(QtCore.QRect(20, 10, 561, 261))
        self.text_feild.setObjectName("text_feild")

        self.clear_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(20, 300, 561, 91))
        self.clear_btn.setObjectName("clear_btn")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.clear_btn.clicked.connect(self.text_feild.clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear_btn.clicked.connect(self.clear)

    def clear(self):
        # self.text_feild.clear()
        sender = self.sender()
        self.text_feild.setText(sender.text() + ' была нажата')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            # self.close()
            self.jump()

    def jump(self):
        self.setGeometry(random.randint(0, 1920), random.randint(0, 1080), 595, 493)


def application():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
