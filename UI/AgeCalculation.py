# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgeCalculation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(40, 130, 91, 51))
        self.save.setObjectName("save")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(40, 80, 91, 51))
        self.return_2.setObjectName("return_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 71))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 80, 501, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(29)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
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
        self.save.setText(_translate("MainWindow", "Save"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Age Calculation</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ar_36_m"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ar_36_air"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ar_36_Ca"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ar_37_m"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ar_37_ca"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ar_38_m"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ar_38_Air"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Air_38_K"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ar_39_m"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Ar_39_K"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Ar_39_Ca"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Ar_40_m"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Ar_40_r"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Ar_40_air"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Ar_40_K"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "Ar_39_K_40_r"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "Ar_36_air_40_r"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "Ar_39_K_36_Air"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "F(Ar_40_r/Ar_39_K)"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "G(Ar_40_m/Ar_39_m)"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "B(Ar_36_m/Ar_39_M)"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "D(Ar_37_m/Ar_39_m)"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "J"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "T"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "Ar_40_r_ratio"))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "C1"))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "C2"))
        item = self.tableWidget.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "C3"))
        item = self.tableWidget.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "C4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sigma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

