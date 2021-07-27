# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AirRatioStatistics.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 110, 791, 71))
        self.label.setObjectName("label")
        self.numSelectedFiles = QtWidgets.QLabel(self.centralwidget)
        self.numSelectedFiles.setGeometry(QtCore.QRect(210, 620, 121, 31))
        self.numSelectedFiles.setObjectName("numSelectedFiles")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(30, 200, 91, 51))
        self.return_2.setObjectName("return_2")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(30, 250, 91, 51))
        self.save.setObjectName("save")
        self.new_2 = QtWidgets.QPushButton(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(30, 300, 91, 51))
        self.new_2.setObjectName("new_2")
        self.RatioTable = QtWidgets.QTableWidget(self.centralwidget)
        self.RatioTable.setGeometry(QtCore.QRect(210, 490, 301, 111))
        self.RatioTable.setObjectName("RatioTable")
        self.RatioTable.setColumnCount(2)
        self.RatioTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.RatioTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RatioTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RatioTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RatioTable.setHorizontalHeaderItem(1, item)
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Air Ratio Statistics</span></p></body></html>"))
        self.numSelectedFiles.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">TextLabel</span></p></body></html>"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.new_2.setText(_translate("MainWindow", "New"))
        item = self.RatioTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "mean"))
        item = self.RatioTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "std"))
        item = self.RatioTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ar 40/36"))
        item = self.RatioTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ar 38/36"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

