import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtCore, QtGui


class P1Main(QMainWindow):
    def __init__(self):
        super(P1Main, self).__init__()
        uic.loadUi('P1Main.ui', self)
        self.initUI()

    def initUI(self):
        self.E1R.clicked.connect(self.run)
        self.E2R.clicked.connect(self.run2)

    def run(self):
        self.B1 = P1B1()
        self.B1.show()

    def run2(self):
        self.B2 = P1B2()
        self.B2.show()


class P1B1(QWidget):
    def __init__(self):
        super(P1B1, self).__init__()
        uic.loadUi('P1B1.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.shat)
        self.E1B.clicked.connect(self.run)

    def run(self):
        self.B0 = P1Main()
        self.B0.show()

    def shat(self):
        a = int(self.X1B.text())
        self.label.setText(str(a + 2))

class P1B2(QWidget):
    def __init__(self):
        super(P1B2, self).__init__()
        uic.loadUi('P1B2.ui', self)
        self.initUI()
        self.E1B.clicked.connect(self.run)

    def run(self):
        self.B0 = P1Main()
        self.B0.show()

    def initUI(self):
        self.pushButton.clicked.connect(self.shat)

    def shat(self):
        a = int(self.X1B.text())
        self.X2B.setText(str(a + 2))


app = QApplication(sys.argv)
ex = P1Main()
ex.show()
sys.exit(app.exec_())



