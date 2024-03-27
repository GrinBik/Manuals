# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 600)
        MainWindow.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.label.setStyleSheet("background-image: url(background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.plus = QtWidgets.QLabel(parent=self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(260, 210, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.plus.setFont(font)
        self.plus.setStyleSheet("color: rgb(0, 170, 127);")
        self.plus.setObjectName("plus")
        self.eq = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eq.setGeometry(QtCore.QRect(550, 200, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.eq.setFont(font)
        self.eq.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.eq.setObjectName("eq")
        self.eq.clicked.connect(self.summa)
        self.num1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(60, 190, 171, 101))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(340, 190, 161, 101))
        self.num2.setObjectName("num2")
        self.result = QtWidgets.QLabel(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(720, 200, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(0, 170, 127);")
        self.result.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def summa(self):
        a = int(self.num1.text())
        b = int(self.num2.text())

        self.result.setText(str(a + b))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.eq.setText(_translate("MainWindow", "="))
        self.result.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
