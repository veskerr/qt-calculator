#from distutils.log import error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(360, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 360, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(116, 185, 200);")
        self.push_1 = QtWidgets.QPushButton(self.centralwidget)
        self.push_1.setGeometry(QtCore.QRect(0, 220, 90, 80))
        self.push_1.setFont(font)
        self.push_1.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_2 = QtWidgets.QPushButton(self.centralwidget)
        self.push_2.setGeometry(QtCore.QRect(90, 220, 90, 80))
        self.push_2.setFont(font)
        self.push_2.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_3 = QtWidgets.QPushButton(self.centralwidget)
        self.push_3.setGeometry(QtCore.QRect(180, 220, 90, 80))
        self.push_3.setFont(font)
        self.push_3.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_4 = QtWidgets.QPushButton(self.centralwidget)
        self.push_4.setGeometry(QtCore.QRect(0, 140, 90, 80))
        self.push_4.setFont(font)
        self.push_4.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_5 = QtWidgets.QPushButton(self.centralwidget)
        self.push_5.setGeometry(QtCore.QRect(90, 140, 90, 80))
        self.push_5.setFont(font)
        self.push_5.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_6 = QtWidgets.QPushButton(self.centralwidget)
        self.push_6.setGeometry(QtCore.QRect(180, 140, 90, 80))
        self.push_6.setFont(font)
        self.push_6.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_7 = QtWidgets.QPushButton(self.centralwidget)
        self.push_7.setGeometry(QtCore.QRect(0, 60, 90, 80))
        self.push_7.setFont(font)
        self.push_7.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_8 = QtWidgets.QPushButton(self.centralwidget)
        self.push_8.setGeometry(QtCore.QRect(90, 60, 90, 80))
        self.push_8.setFont(font)
        self.push_8.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_9 = QtWidgets.QPushButton(self.centralwidget)
        self.push_9.setGeometry(QtCore.QRect(180, 60, 90, 80))
        self.push_9.setFont(font)
        self.push_9.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_0 = QtWidgets.QPushButton(self.centralwidget)
        self.push_0.setGeometry(QtCore.QRect(0, 300, 140, 80))
        self.push_0.setFont(font)
        self.push_0.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_eq = QtWidgets.QPushButton(self.centralwidget)
        self.push_eq.setGeometry(QtCore.QRect(140, 300, 130, 80))
        self.push_eq.setFont(font)
        self.push_eq.setStyleSheet("background-color: rgb(255, 88, 91);")
        self.push_mul = QtWidgets.QPushButton(self.centralwidget)
        self.push_mul.setGeometry(QtCore.QRect(270, 60, 90, 80))
        self.push_mul.setFont(font)
        self.push_mul.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_div = QtWidgets.QPushButton(self.centralwidget)
        self.push_div.setGeometry(QtCore.QRect(270, 140, 90, 80))
        self.push_div.setFont(font)
        self.push_div.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_plus = QtWidgets.QPushButton(self.centralwidget)
        self.push_plus.setGeometry(QtCore.QRect(270, 220, 90, 80))
        self.push_plus.setFont(font)

        self.push_plus.setStyleSheet("background-color: rgb(85, 122, 255);")
        self.push_minus = QtWidgets.QPushButton(self.centralwidget)
        self.push_minus.setGeometry(QtCore.QRect(270, 300, 90, 80))
        self.push_minus.setFont(font)
        self.push_minus.setStyleSheet("background-color: rgb(85, 122, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_functions()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.push_1.setText(_translate("MainWindow", "1"))
        self.push_2.setText(_translate("MainWindow", "2"))
        self.push_3.setText(_translate("MainWindow", "3"))
        self.push_4.setText(_translate("MainWindow", "4"))
        self.push_5.setText(_translate("MainWindow", "5"))
        self.push_6.setText(_translate("MainWindow", "6"))
        self.push_7.setText(_translate("MainWindow", "7"))
        self.push_8.setText(_translate("MainWindow", "8"))
        self.push_9.setText(_translate("MainWindow", "9"))
        self.push_0.setText(_translate("MainWindow", "0"))
        self.push_eq.setText(_translate("MainWindow", "="))
        self.push_mul.setText(_translate("MainWindow", " * "))
        self.push_div.setText(_translate("MainWindow", " / "))
        self.push_plus.setText(_translate("MainWindow", " + "))
        self.push_minus.setText(_translate("MainWindow", " - "))

    def add_functions(self):
        self.push_0.clicked.connect(
            lambda: self.write_number(self.push_0.text()))
        self.push_1.clicked.connect(
            lambda: self.write_number(self.push_1.text()))
        self.push_2.clicked.connect(
            lambda: self.write_number(self.push_2.text()))
        self.push_3.clicked.connect(
            lambda: self.write_number(self.push_3.text()))
        self.push_4.clicked.connect(
            lambda: self.write_number(self.push_4.text()))
        self.push_5.clicked.connect(
            lambda: self.write_number(self.push_5.text()))
        self.push_6.clicked.connect(
            lambda: self.write_number(self.push_6.text()))
        self.push_7.clicked.connect(
            lambda: self.write_number(self.push_7.text()))
        self.push_8.clicked.connect(
            lambda: self.write_number(self.push_8.text()))
        self.push_9.clicked.connect(
            lambda: self.write_number(self.push_9.text()))
        self.push_plus.clicked.connect(
            lambda: self.write_number(self.push_plus.text()))
        self.push_minus.clicked.connect(
            lambda: self.write_number(self.push_minus.text()))
        self.push_mul.clicked.connect(
            lambda: self.write_number(self.push_mul.text()))
        self.push_div.clicked.connect(
            lambda: self.write_number(self.push_div.text()))
        self.push_eq.clicked.connect(self.get_result)
    def write_number(self, number):
        if self.label_result.text() == "0" or self.is_equal == True:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text()+number)
    def get_result(self):
        if not self.is_equal:
            result = eval(self.label_result.text())
            self.label_result.setText("Результат:"+str(result))
            self.is_equal = True
        else:
            ...

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec_()