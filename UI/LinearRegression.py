# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/LinearRegression.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(110, 130, 641, 61))
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 110, 70, 16))
        self.label.setObjectName("label")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(0, 170, 91, 51))
        self.save.setObjectName("save")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(0, 120, 91, 51))
        self.return_2.setObjectName("return_2")
        self.reselect = QtWidgets.QPushButton(self.centralwidget)
        self.reselect.setGeometry(QtCore.QRect(0, 220, 91, 51))
        self.reselect.setObjectName("reselect")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 390, 81, 91))
        self.label_2.setObjectName("label_2")
        self.linear = QtWidgets.QPushButton(self.centralwidget)
        self.linear.setGeometry(QtCore.QRect(0, 490, 91, 51))
        self.linear.setObjectName("linear")
        self.average = QtWidgets.QPushButton(self.centralwidget)
        self.average.setGeometry(QtCore.QRect(0, 540, 91, 51))
        self.average.setObjectName("average")
        self.current_fit_func = QtWidgets.QLabel(self.centralwidget)
        self.current_fit_func.setGeometry(QtCore.QRect(110, 200, 511, 16))
        self.current_fit_func.setObjectName("current_fit_func")
        self.new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(0, 270, 91, 51))
        self.new_2.setObjectName("new_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Description"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.reselect.setText(_translate("MainWindow", "Reselect"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">fitting </p><p align=\"center\">function</p><p align=\"center\">options</p></body></html>"))
        self.linear.setText(_translate("MainWindow", "Linear"))
        self.average.setText(_translate("MainWindow", "Average"))
        self.current_fit_func.setText(_translate("MainWindow", "Current fitting function:"))
        self.new_2.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

