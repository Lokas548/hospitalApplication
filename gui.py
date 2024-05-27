from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from config import connectDB
from config import findEmployeeColumns
from config import findEmployee
from config import findPatient
from config import findPatientColumns
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 765)
        MainWindow.setStyleSheet("background-color: rgb(128,128,128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.querryResult = QtWidgets.QTableWidget(self.centralwidget)
        self.querryResult.setGeometry(QtCore.QRect(0, 0, 911, 481))
        self.querryResult.setStyleSheet("background-color: white;\n"
"")
        self.querryResult.setObjectName("querryResult")
        self.querryResult.setColumnCount(0)
        self.querryResult.setRowCount(0)
        self.findEmploye = QtWidgets.QPushButton(self.centralwidget)
        self.findEmploye.setGeometry(QtCore.QRect(250, 650, 151, 41))
        self.findEmploye.setStyleSheet("background-color: #8d917a;")
        self.findEmploye.setObjectName("findEmploye")
        self.findPatient = QtWidgets.QPushButton(self.centralwidget)
        self.findPatient.setGeometry(QtCore.QRect(680, 650, 151, 41))
        self.findPatient.setStyleSheet("background-color: #8d917a;")
        self.findPatient.setObjectName("findPatient")
        self.employeeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.employeeInput.setGeometry(QtCore.QRect(80, 650, 171, 41))
        self.employeeInput.setStyleSheet("background-color: #8d917a;\n"
"border: 1px solid black;")
        self.employeeInput.setText("")
        self.employeeInput.setObjectName("employeeInput")
        self.patientInput = QtWidgets.QLineEdit(self.centralwidget)
        self.patientInput.setGeometry(QtCore.QRect(510, 650, 171, 41))
        self.patientInput.setStyleSheet("background-color: #8d917a;\n"
"border: 1px solid black;")
        self.patientInput.setObjectName("patientInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 530, 101, 31))
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 530, 101, 31))
        self.label_2.setObjectName("label_2")
        self.employeeSurname = QtWidgets.QRadioButton(self.centralwidget)
        self.employeeSurname.setGeometry(QtCore.QRect(90, 560, 95, 20))
        self.employeeSurname.setObjectName("employeeSurname")
        self.employeeId = QtWidgets.QRadioButton(self.centralwidget)
        self.employeeId.setGeometry(QtCore.QRect(90, 580, 95, 20))
        self.employeeId.setObjectName("employeeId")
        self.employeeDepartment = QtWidgets.QRadioButton(self.centralwidget)
        self.employeeDepartment.setGeometry(QtCore.QRect(90, 600, 95, 20))
        self.employeeDepartment.setObjectName("employeeDepartment")
        self.patientSurname = QtWidgets.QRadioButton(self.centralwidget)
        self.patientSurname.setGeometry(QtCore.QRect(510, 560, 95, 20))
        self.patientSurname.setObjectName("patientSurname")
        self.patientId = QtWidgets.QRadioButton(self.centralwidget)
        self.patientId.setGeometry(QtCore.QRect(510, 580, 95, 20))
        self.patientId.setObjectName("patientId")
        self.patientPolicy = QtWidgets.QRadioButton(self.centralwidget)
        self.patientPolicy.setGeometry(QtCore.QRect(510, 600, 111, 20))
        self.patientPolicy.setObjectName("patientPolicy")
        self.employeePosition = QtWidgets.QRadioButton(self.centralwidget)
        self.employeePosition.setGeometry(QtCore.QRect(210, 600, 95, 20))
        self.employeePosition.setObjectName("employeePosition")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 520, 531, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 530, 20, 221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(530, 520, 381, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(840, 530, 141, 231))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 500, 121, 21))
        self.label_3.setStyleSheet("font-size: 19px\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 500, 111, 21))
        self.label_4.setStyleSheet("font-size:19px")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Все что связанно с поиском сотрудников
        self.findEmploye.clicked.connect(self.employeeDrawResult)
        self.findPatient.clicked.connect(self.patientDrawResult)

    def employeeDrawResult(self):
        dataTypeArr = []
        empInput = self.employeeInput.text()
        #Done
        if(self.employeeId.isChecked()):
            dataTypeArr.append("id_сотрудника")
            dataTypeArr.append(empInput)
            rows = findEmployee(dataTypeArr)
        #Done
        elif(self.employeeDepartment.isChecked()):
            dataTypeArr.append("НаименованиеОтделение")
            dataTypeArr.append(str(empInput))
            rows = findEmployee(dataTypeArr)
        #Done
        elif(self.employeePosition.isChecked()):
            dataTypeArr.append("НаименованиеДолжность")
            dataTypeArr.append(str(empInput))
            rows = findEmployee(dataTypeArr)
        elif (self.employeeSurname.isChecked()):
            dataTypeArr.append("ФИО")
            fio_parts = empInput.split(" ")
            dataTypeArr.append(fio_parts[0])
            dataTypeArr.append(fio_parts[1])
            dataTypeArr.append(fio_parts[2])
            print(dataTypeArr[1],dataTypeArr[2],dataTypeArr[3])
            rows = findEmployee(dataTypeArr)
        else:
            dataTypeArr.append("*")
            rows = findEmployee(dataTypeArr)

        column_names = findEmployeeColumns()
        self.querryResult.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.querryResult.setColumnCount(len(column_names))  # Устанавливаем количество столбцов в таблице

        self.querryResult.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.querryResult.setItem(i, j, item)

    def patientDrawResult(self):
        dataTypeArr1 = []
        patientInput = self.patientInput.text()
        print(1)
        #Done
        if(self.patientId.isChecked()):
            dataTypeArr1.append("id_пациента")
            dataTypeArr1.append(patientInput)
            rows = findPatient(dataTypeArr1)
        #Done
        elif (self.patientSurname.isChecked()):
            print(12)
            dataTypeArr1.append("ФИО")
            fio_parts = patientInput.split(" ")
            dataTypeArr1.append(fio_parts[0])
            dataTypeArr1.append(fio_parts[1])
            dataTypeArr1.append(fio_parts[2])
            print(dataTypeArr1[1],dataTypeArr1[2],dataTypeArr1[3])
            rows = findPatient(dataTypeArr1)
        #Done
        elif (self.patientPolicy.isChecked()):
            dataTypeArr1.append("Номер_полиса")
            dataTypeArr1.append(patientInput)
            rows = findPatient(dataTypeArr1)
        else:
            dataTypeArr1.append("*")
            rows = findPatient(dataTypeArr1)
        #Done

        column_names = findPatientColumns()
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
        self.findEmploye.setText(_translate("MainWindow", "Найти "))
        self.findPatient.setText(_translate("MainWindow", "Найти "))
        self.label.setText(_translate("MainWindow", "Фильтр поиска"))
        self.label_2.setText(_translate("MainWindow", "Фильтр поиска"))
        self.employeeSurname.setText(_translate("MainWindow", "ФИО"))
        self.employeeId.setText(_translate("MainWindow", "Id"))
        self.employeeDepartment.setText(_translate("MainWindow", "Отделение"))
        self.patientSurname.setText(_translate("MainWindow", "ФИО"))
        self.patientId.setText(_translate("MainWindow", "Id"))
        self.patientPolicy.setText(_translate("MainWindow", "Номер полиса"))
        self.employeePosition.setText(_translate("MainWindow", "Должнось"))
        self.label_3.setText(_translate("MainWindow", "Пациенты"))
        self.label_4.setText(_translate("MainWindow", "Сотрудники"))



def application():
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(main_win)
    connectDB()

    main_win.show()
    sys.exit(app.exec_())