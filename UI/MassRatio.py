# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MassRatio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(20, 190, 113, 51))
        self.return_2.setObjectName("return_2")
        self.RatioTable = QtWidgets.QTableWidget(self.centralwidget)
        self.RatioTable.setGeometry(QtCore.QRect(200, 420, 311, 201))
        self.RatioTable.setObjectName("RatioTable")
        self.RatioTable.setColumnCount(2)
        self.RatioTable.setRowCount(5)
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
        self.RatioTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setHorizontalHeaderItem(1, item)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.RatioTable.setItem(4, 0, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 126, 791, 71))
        self.label.setObjectName("label")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(20, 240, 113, 51))
        self.save.setObjectName("save")
        self.ValueTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ValueTable.setGeometry(QtCore.QRect(200, 200, 481, 201))
        self.ValueTable.setObjectName("ValueTable")
        self.ValueTable.setColumnCount(3)
        self.ValueTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.ValueTable.setItem(4, 2, item)
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
        self.return_2.setText(_translate("MainWindow", "Return"))
        item = self.RatioTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ar 40/36"))
        item = self.RatioTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ar 37/39"))
        item = self.RatioTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ar 36/38"))
        item = self.RatioTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ar 40/38"))
        item = self.RatioTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "AR 40/39"))
        item = self.RatioTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ratio"))
        item = self.RatioTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sigma"))
        __sortingEnabled = self.RatioTable.isSortingEnabled()
        self.RatioTable.setSortingEnabled(False)
        self.RatioTable.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Mass Ratio</span></p></body></html>"))
        self.save.setText(_translate("MainWindow", "Save"))
        item = self.ValueTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ar 36"))
        item = self.ValueTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ar 37"))
        item = self.ValueTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ar 38"))
        item = self.ValueTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ar 39"))
        item = self.ValueTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ar 40"))
        item = self.ValueTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Raw"))
        item = self.ValueTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Measurement"))
        item = self.ValueTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sigma"))
        __sortingEnabled = self.ValueTable.isSortingEnabled()
        self.ValueTable.setSortingEnabled(False)
        self.ValueTable.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

