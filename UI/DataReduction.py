# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataReduction.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 32, 791, 61))
        self.label.setMinimumSize(QtCore.QSize(519, 43))
        self.label.setObjectName("label")
        self.LRP = QtWidgets.QPushButton(self.centralwidget)
        self.LRP.setGeometry(QtCore.QRect(210, 150, 421, 51))
        self.LRP.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.LRP.setObjectName("LRP")
        self.T0S = QtWidgets.QPushButton(self.centralwidget)
        self.T0S.setGeometry(QtCore.QRect(210, 220, 421, 51))
        self.T0S.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.T0S.setObjectName("T0S")
        self.Ratio = QtWidgets.QPushButton(self.centralwidget)
        self.Ratio.setGeometry(QtCore.QRect(210, 290, 421, 51))
        self.Ratio.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.Ratio.setObjectName("Ratio")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">NTNU ArAr Lab Data Reduction</span></p></body></html>"))
        self.LRP.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.LRP.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.LRP.setText(_translate("MainWindow", "Make Linear Regression Plot"))
        self.T0S.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.T0S.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.T0S.setText(_translate("MainWindow", "T0 Statistics"))
        self.Ratio.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.Ratio.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.Ratio.setText(_translate("MainWindow", "Mass Ratio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

