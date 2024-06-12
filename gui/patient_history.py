from PyQt5 import QtCore, QtGui, QtWidgets
from src.config import patientHistory
from src.config import patientSickDays

class Ui_PatientHistory(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 600)
        MainWindow.setStyleSheet("background-color: rgb(128,128,128);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.patientId = QtWidgets.QLineEdit(self.centralwidget)
        self.patientId.setGeometry(QtCore.QRect(20, 450, 191, 31))
        self.patientId.setStyleSheet("background-color:#FDF5E6;")
        self.patientId.setObjectName("patientId")
        self.showResult = QtWidgets.QPushButton(self.centralwidget)
        self.showResult.setGeometry(QtCore.QRect(210, 450, 121, 31))
        self.showResult.setStyleSheet("background-color: #8d917a;\n"
"")
        self.showResult.setObjectName("showResult")
        self.diseasesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.diseasesTable.setGeometry(QtCore.QRect(20, 70, 401, 321))
        self.diseasesTable.setStyleSheet("background-color:#FDF5E6;")
        self.diseasesTable.setObjectName("diseasesTable")
        self.diseasesTable.setColumnCount(0)
        self.diseasesTable.setRowCount(0)
        self.sickDaysTable = QtWidgets.QTableWidget(self.centralwidget)
        self.sickDaysTable.setGeometry(QtCore.QRect(450, 70, 411, 321))
        self.sickDaysTable.setStyleSheet("background-color:#FDF5E6;")
        self.sickDaysTable.setObjectName("sickDaysTable")
        self.sickDaysTable.setColumnCount(0)
        self.sickDaysTable.setRowCount(0)
        self.disease = QtWidgets.QLabel(self.centralwidget)
        self.disease.setGeometry(QtCore.QRect(130, 40, 101, 21))
        self.disease.setStyleSheet("font-size:16px\n"
"")
        self.disease.setObjectName("disease")
        self.sickDays = QtWidgets.QLabel(self.centralwidget)
        self.sickDays.setGeometry(QtCore.QRect(600, 40, 101, 20))
        self.sickDays.setStyleSheet("font-size:16px\n"
"")
        self.sickDays.setObjectName("sickDays")
        self.patient = QtWidgets.QLabel(self.centralwidget)
        self.patient.setGeometry(QtCore.QRect(60, 480, 131, 20))
        self.patient.setStyleSheet("font-size:14px")
        self.patient.setObjectName("patient")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showResult.clicked.connect(self.getPatientId)

    def getPatientId(self):
        patId = self.patientId.text()
        rows = patientHistory(patId)


        column_names = ['Диагноз','Дата_приема','Врач','Лечение']
        self.diseasesTable.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.diseasesTable.setColumnCount(len(column_names))  # Устанавливаем количество столбцов в таблице

        self.diseasesTable.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.diseasesTable.setItem(i, j, item)

        rows = patientSickDays(patId)
        column_names = ['Дата_начала','Дата_окончания','Открывший_врач','Закрывший_врач','Дата_приема']
        self.sickDaysTable.setRowCount(len(rows))  # Устанавливаем количество строк в таблице
        self.sickDaysTable.setColumnCount(len(column_names))  # Устанавливаем количество столбцов в таблице

        self.sickDaysTable.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.sickDaysTable.setItem(i, j, item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showResult.setText(_translate("MainWindow", "Показать результат"))
        self.disease.setText(_translate("MainWindow", "Заболевания"))
        self.sickDays.setText(_translate("MainWindow", "Больничные"))
        self.patient.setText(_translate("MainWindow", "id Пациента"))
