# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParameterSetting.ui'
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
        self.ParameetrTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ParameetrTable.setGeometry(QtCore.QRect(200, 90, 281, 191))
        self.ParameetrTable.setObjectName("ParameetrTable")
        self.ParameetrTable.setColumnCount(1)
        self.ParameetrTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ParameetrTable.setHorizontalHeaderItem(0, item)
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(40, 130, 91, 51))
        self.change.setObjectName("change")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(40, 180, 91, 51))
        self.save.setObjectName("save")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(40, 80, 91, 51))
        self.return_2.setObjectName("return_2")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(40, 230, 91, 51))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 71))
        self.label.setObjectName("label")
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
        item = self.ParameetrTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Background Ar 40/36"))
        item = self.ParameetrTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Background Ar 38/36"))
        item = self.ParameetrTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "numCycle"))
        item = self.ParameetrTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "basline (autoselect outlier)"))
        item = self.ParameetrTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "maxfev (curve_fit)"))
        item = self.ParameetrTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        self.change.setText(_translate("MainWindow", "Change"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Parameter Setting</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

