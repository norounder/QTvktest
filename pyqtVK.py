import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.TeTest = QtWidgets.QPlainTextEdit()
        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.layout.addWidget(self.TeTest)
        self.setCentralWidget(self.main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
