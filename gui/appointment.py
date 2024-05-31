from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from src.config import connectDB
from src.config import findEmployeeColumns
from src.config import findEmployee
from src.config import findPatient
from src.config import findPatientColumns
from gui.admin import Ui_Admin

import sys



class Ui_Auth(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 562)
        MainWindow.setStyleSheet("background-color:#a68b8b")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.admin = QtWidgets.QPushButton(self.centralwidget)
        self.admin.setGeometry(QtCore.QRect(120, 240, 121, 31))
        self.admin.setStyleSheet("background-color: #ffc4c4\n"
"")
        self.admin.setObjectName("admin")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(260, 240, 121, 31))
        self.update.setStyleSheet("background-color: #ffc4c4\n"
"")
        self.update.setObjectName("update")
        self.addEmpOrPatient = QtWidgets.QPushButton(self.centralwidget)
        self.addEmpOrPatient.setGeometry(QtCore.QRect(400, 240, 151, 31))
        self.addEmpOrPatient.setStyleSheet("background-color: #ffc4c4\n"
"")
        self.addEmpOrPatient.setObjectName("addEmpOrPatient")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 130, 181, 41))
        self.label.setStyleSheet("font-size: 19px\n"
"")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 110, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 370, 491, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 100, 491, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(570, 110, 20, 271))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.admin.clicked.connect(self.openAdmin)
    def openAdmin(self):
        self.adm = Ui_Admin()
        self.adm.show()

    # def appointmetCall(self):
    #     a = QApplication(sys.argv)
    #     auth = QMainWindow()
    #     win_auth = Ui_Auth()
    #     win_auth.setupUi(auth)
    #     auth.show()






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.admin.setText(_translate("MainWindow", "Администратор"))
        self.update.setText(_translate("MainWindow", "Запись на прием"))
        self.addEmpOrPatient.setText(_translate("MainWindow", "Добавить врача/пациента"))
        self.label.setText(_translate("MainWindow", "Роль для входа"))

def mainWinCall():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    window = Ui_Auth()
    window.setupUi(main_window)
    main_window.show()


    sys.exit(app.exec_())