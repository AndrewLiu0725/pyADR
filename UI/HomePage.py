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
        self.label.setGeometry(QtCore.QRect(8, 132, 781, 91))
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
        self.PS_button = QtWidgets.QPushButton(self.centralwidget)
        self.PS_button.setGeometry(QtCore.QRect(210, 600, 421, 51))
        self.PS_button.setStyleSheet("font: 20pt \".AppleSystemUIFont\";")
        self.PS_button.setObjectName("PS_button")
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
        self.actionAbout_pyADR = QtWidgets.QAction(MainWindow)
        self.actionAbout_pyADR.setObjectName("actionAbout_pyADR")
        self.actionCheck_Update = QtWidgets.QAction(MainWindow)
        self.actionCheck_Update.setObjectName("actionCheck_Update")
        self.menuMenu.addAction(self.actionAbout_pyADR)
        self.menuMenu.addAction(self.actionCheck_Update)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionParameter_Setting)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">pyADR</span></p></body></html>"))
        self.LRP.setToolTip(_translate("MainWindow", "<html><head/><body><p>T0 Calculation:</p><p>Please select the raw data file for which you want to calculate the T<span style=\" vertical-align:sub;\">0</span> with valid data format (refer to the example in README)!</p></body></html>"))
        self.LRP.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.LRP.setText(_translate("MainWindow", "Calculate T0"))
        self.T0S.setToolTip(_translate("MainWindow", "<html><head/><body><p>T0 Statistics:</p><p>Please select all the files (the raw files output by the <span style=\" font-style:italic;\">Calculate T0 page</span>) for which you want to compute the statistics of the T<span style=\" vertical-align:sub;\">0</span> values.</p></body></html>"))
        self.T0S.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.T0S.setText(_translate("MainWindow", "T0 Statistics"))
        self.MR.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mass Ratio Calculation:</p><p>Please select one mass file first and then one preline file. Both files are the raw files output by <span style=\" font-style:italic;\">Calculate T0 page</span>.</p></body></html>"))
        self.MR.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.MR.setText(_translate("MainWindow", "Mass Ratio"))
        self.ARS.setToolTip(_translate("MainWindow", "<html><head/><body><p>Air Ratio Statistics:</p><p>Please select all the files (the ratio files output by the <span style=\" font-style:italic;\">Mass Ratio Page</span>) for which you want to compute the statistics of the air ratios.</p></body></html>"))
        self.ARS.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.ARS.setText(_translate("MainWindow", "Air Ratio Statistics"))
        self.AC.setToolTip(_translate("MainWindow", "<html><head/><body><p>Age Calculation:</p><p>Please select one file (the measurement file output by the <span style=\" font-style:italic;\">Mass Ratio Page</span>) that you want to calculate the age for.</p></body></html>"))
        self.AC.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.AC.setText(_translate("MainWindow", "Age Calculation"))
        self.PS_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Production Ratio 39Ar/37Ar(ca)</p><p>Production Ratio 36Ar/37Ar(ca)</p><p>Production Ratio 40Ar/39Ar(k)</p><p>Production Ratio 38Ar/39Ar(k)</p><p>Production Ratio 36Ar/38Ar(cl)</p><p>Atmospheric Ratio 40/36(a)</p><p>Atmospheric Ratio 38/36(a)</p><p>λ</p><p>J value</p><p>J std</p><p>numCycle</p></body></html>"))
        self.PS_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>what is this</p></body></html>"))
        self.PS_button.setText(_translate("MainWindow", "Parameter Setting"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionParameter_Setting.setText(_translate("MainWindow", " Parameter Setting"))
        self.actionAbout_pyADR.setText(_translate("MainWindow", " About pyADR"))
        self.actionCheck_Update.setText(_translate("MainWindow", " Check Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

