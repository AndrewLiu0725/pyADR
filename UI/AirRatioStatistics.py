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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(30, 90, 113, 51))
        self.return_2.setObjectName("return_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 791, 71))
        self.label.setObjectName("label")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(30, 150, 113, 51))
        self.save.setObjectName("save")
        self.RatioTable = QtWidgets.QTableWidget(self.centralwidget)
        self.RatioTable.setGeometry(QtCore.QRect(480, 180, 191, 121))
        self.RatioTable.setObjectName("RatioTable")
        self.RatioTable.setColumnCount(1)
        self.RatioTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setItem(1, 0, item)
        self.numSelectedFiles = QtWidgets.QLabel(self.centralwidget)
        self.numSelectedFiles.setGeometry(QtCore.QRect(480, 330, 121, 31))
        self.numSelectedFiles.setObjectName("numSelectedFiles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # insert photo
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(175, 125, 225, 375))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../Figures/cat.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Air Ratio Statistics</span></p></body></html>"))
        self.save.setText(_translate("MainWindow", "Save"))
        item = self.RatioTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mean"))
        item = self.RatioTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "STD"))
        item = self.RatioTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Air Ratio"))
        __sortingEnabled = self.RatioTable.isSortingEnabled()
        self.RatioTable.setSortingEnabled(False)
        self.RatioTable.setSortingEnabled(__sortingEnabled)
        self.numSelectedFiles.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">TextLabel</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

