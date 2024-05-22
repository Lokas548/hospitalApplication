from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
import sys

def application():
    app = QApplication(sys.argv)
    win = QMainWindow

    win.setWindowTitle("Больница")

    win.show()
    sys.exit(app.exec_())
