from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from src.config import getScheudle
from src.config import findEmployeeColumns
from src.config import findScheudleColumns
from src.config import insertAppoint

#global variables
appointmentID = 0

class Ui_Appointment(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 600)
        MainWindow.setStyleSheet("background-color: rgb(128,128,128)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.receptionTable = QtWidgets.QTableWidget(self.centralwidget)
        self.receptionTable.setGeometry(QtCore.QRect(0, 70, 561, 321))
        self.receptionTable.setStyleSheet("background-color:white")
        self.receptionTable.setObjectName("receptionTable")
        self.receptionTable.setColumnCount(0)
        self.receptionTable.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 231, 41))
        self.label.setStyleSheet("font-size:20px solid;")
        self.label.setObjectName("label")
        self.doctorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.doctorInput.setGeometry(QtCore.QRect(40, 430, 221, 31))
        self.doctorInput.setStyleSheet("background-color:white")
        self.doctorInput.setObjectName("doctorInput")
        self.findDoctor = QtWidgets.QPushButton(self.centralwidget)
        self.findDoctor.setGeometry(QtCore.QRect(260, 430, 101, 31))
        self.findDoctor.setStyleSheet("background-color: #8d917a;")
        self.findDoctor.setObjectName("findDoctor")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 470, 131, 16))
        self.label_2.setStyleSheet("font-size:14px\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.patientInput = QtWidgets.QLineEdit(self.centralwidget)
        self.patientInput.setGeometry(QtCore.QRect(570, 230, 221, 31))
        self.patientInput.setStyleSheet("background-color:white")
        self.patientInput.setObjectName("patientInput")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 180, 71, 41))
        self.label_3.setStyleSheet("font-size: 20px solid;")
        self.label_3.setObjectName("label_3")
        self.appointButton = QtWidgets.QPushButton(self.centralwidget)
        self.appointButton.setGeometry(QtCore.QRect(790, 230, 101, 31))
        self.appointButton.setStyleSheet("background-color: #8d917a;")
        self.appointButton.setObjectName("appointButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 270, 131, 16))
        self.label_4.setStyleSheet("font-size:14px")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.findDoctor.clicked.connect(self.showScheudle)
        self.appointButton.clicked.connect(self.updateAppointTable)
        self.receptionTable.cellClicked.connect(self.getData)

    def getData(self):
         global appointmentID
         current_row = self.receptionTable.currentRow()
         current_column = self.receptionTable.currentColumn()
         insertID = self.receptionTable.item(current_row,current_column)
         appointmentID = insertID.text()

    def showScheudle(self):
        nameArr = []
        empInput = self.doctorInput.text()
        fio_parts = empInput.split(" ")
        nameArr.append(fio_parts[0])
        nameArr.append(fio_parts[1])
        nameArr.append(fio_parts[2])
        rows = getScheudle(nameArr)

        column_names = findScheudleColumns()
        self.receptionTable.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.receptionTable.setColumnCount(len(column_names))  # Устанавливаем количество столбцов в таблице

        self.receptionTable.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.receptionTable.setItem(i, j, item)
    def updateAppointTable(self):
        nameArr = []
        patientInput = self.patientInput.text()
        fio_parts = patientInput.split(" ")
        nameArr.append(fio_parts[0])
        nameArr.append(fio_parts[1])
        nameArr.append(fio_parts[2])
        insertAppoint(nameArr,appointmentID)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Доступные приемы"))
        self.findDoctor.setText(_translate("MainWindow", "Найти"))
        self.label_2.setText(_translate("MainWindow", "ФИО Сотрудника"))
        self.label_3.setText(_translate("MainWindow", "Запись"))
        self.appointButton.setText(_translate("MainWindow", "Добавить"))
        self.label_4.setText(_translate("MainWindow", "ФИО Пациента"))