# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 132, 791, 61))
        self.label.setMinimumSize(QtCore.QSize(519, 43))
        self.label.setObjectName("label")
        self.LRP = QtWidgets.QPushButton(self.centralwidget)
        self.LRP.setGeometry(QtCore.QRect(210, 250, 421, 51))
        self.LRP.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.LRP.setObjectName("LRP")
        self.T0S = QtWidgets.QPushButton(self.centralwidget)
        self.T0S.setGeometry(QtCore.QRect(210, 320, 421, 51))
        self.T0S.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.T0S.setObjectName("T0S")
        self.MR = QtWidgets.QPushButton(self.centralwidget)
        self.MR.setGeometry(QtCore.QRect(210, 390, 421, 51))
        self.MR.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.MR.setObjectName("MR")
        self.ARS = QtWidgets.QPushButton(self.centralwidget)
        self.ARS.setGeometry(QtCore.QRect(210, 460, 421, 51))
        self.ARS.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.ARS.setObjectName("ARS")
        self.AC = QtWidgets.QPushButton(self.centralwidget)
        self.AC.setGeometry(QtCore.QRect(210, 530, 421, 51))
        self.AC.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.AC.setObjectName("AC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionParameter_Setting = QtWidgets.QAction(MainWindow)
        self.actionParameter_Setting.setObjectName("actionParameter_Setting")
        self.menuMenu.addAction(self.actionParameter_Setting)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">pyADR</span></p></body></html>"))
        self.LRP.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.LRP.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.LRP.setText(_translate("MainWindow", "Calculate T0"))
        self.T0S.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.T0S.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.T0S.setText(_translate("MainWindow", "T0 Statistics"))
        self.MR.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.MR.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.MR.setText(_translate("MainWindow", "Mass Ratio"))
        self.ARS.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ARS.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.ARS.setText(_translate("MainWindow", "Air Ratio Statistics"))
        self.AC.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.AC.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.AC.setText(_translate("MainWindow", "Age Calculation"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionParameter_Setting.setText(_translate("MainWindow", "Parameter Setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

