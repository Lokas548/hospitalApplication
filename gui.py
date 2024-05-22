from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys

from config import findEmployee
from config import findEmployeeColumns
from config import connectDB

# input_ui_file = "mainWindow.ui"
# output_py_file = "output.py"
#
# subprocess.call(["pyuic5",     input_ui_file, "-o", output_py_file])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.querryResult = QtWidgets.QTableWidget(self.centralwidget)
        self.querryResult.setGeometry(QtCore.QRect(10, 10, 621, 541))
        self.querryResult.setObjectName("querryResult")
        self.querryResult.setColumnCount(0)
        self.querryResult.setRowCount(0)
        self.findEmploye = QtWidgets.QPushButton(self.centralwidget)
        self.findEmploye.setGeometry(QtCore.QRect(10, 640, 151, 41))
        self.findEmploye.setObjectName("findEmploye")
        self.findPatient = QtWidgets.QPushButton(self.centralwidget)
        self.findPatient.setGeometry(QtCore.QRect(200, 640, 151, 41))
        self.findPatient.setObjectName("findPatient")
        self.addEmploye = QtWidgets.QPushButton(self.centralwidget)
        self.addEmploye.setGeometry(QtCore.QRect(930, 270, 151, 41))
        self.addEmploye.setObjectName("addEmploye")
        self.addPatient = QtWidgets.QPushButton(self.centralwidget)
        self.addPatient.setGeometry(QtCore.QRect(930, 500, 151, 41))
        self.addPatient.setObjectName("addPatient")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Все что связанно с поиском сотрудников
        self.findEmploye.clicked.connect(self.drawResult)

    def drawResult(self):
        rows = findEmployee()
        column_names = findEmployeeColumns()
        self.querryResult.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.querryResult.setColumnCount(len(column_names))  # Устанавливаем количество столбцов в таблице

        self.querryResult.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.querryResult.setItem(i, j, item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findEmploye.setText(_translate("MainWindow", "Найти сотрудника"))
        self.findPatient.setText(_translate("MainWindow", "Найти Пациента"))
        self.addEmploye.setText(_translate("MainWindow", "Добавить сотрудника"))
        self.addPatient.setText(_translate("MainWindow", "Добавить пациента"))



def application():
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(main_win)
    connectDB()

    main_win.show()
    sys.exit(app.exec_())

