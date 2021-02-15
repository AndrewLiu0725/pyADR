# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complex_Homepage.ui'
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
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 240, 241, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 241, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 150, 241, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 330, 241, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 430, 241, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 430, 241, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 441, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 240, 241, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 330, 241, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSaving_folder = QtWidgets.QAction(MainWindow)
        self.actionSaving_folder.setObjectName("actionSaving_folder")
        self.actionHTBasics_file = QtWidgets.QAction(MainWindow)
        self.actionHTBasics_file.setObjectName("actionHTBasics_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEdit_saving_folder = QtWidgets.QAction(MainWindow)
        self.actionEdit_saving_folder.setObjectName("actionEdit_saving_folder")
        self.actionEdit_HTBasic_file_path = QtWidgets.QAction(MainWindow)
        self.actionEdit_HTBasic_file_path.setObjectName("actionEdit_HTBasic_file_path")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionmore = QtWidgets.QAction(MainWindow)
        self.actionmore.setObjectName("actionmore")
        self.menuSetting.addAction(self.actionEdit_saving_folder)
        self.menuSetting.addAction(self.actionEdit_HTBasic_file_path)
        self.menuSetting.addAction(self.actionExit_2)
        self.menuSetting.addAction(self.actionmore)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_5.setText(_translate("MainWindow", "Run samples on Multiplier"))
        self.pushButton.setText(_translate("MainWindow", "Configure analytical parameters"))
        self.pushButton_4.setText(_translate("MainWindow", "Run samples on Faraday"))
        self.pushButton_3.setText(_translate("MainWindow", "Configure valve driver operation"))
        self.pushButton_6.setText(_translate("MainWindow", "Configure magnetic field"))
        self.pushButton_8.setText(_translate("MainWindow", "Data Analysis"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">NTNU ArAr Lab </span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Configure low furnace"))
        self.pushButton_7.setText(_translate("MainWindow", "Run LabView\'s scan"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionSaving_folder.setText(_translate("MainWindow", "Saving folder"))
        self.actionHTBasics_file.setText(_translate("MainWindow", "HTBasics file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEdit_saving_folder.setText(_translate("MainWindow", "Edit saving folder"))
        self.actionEdit_HTBasic_file_path.setText(_translate("MainWindow", "Edit HTBasic file path"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionmore.setText(_translate("MainWindow", "more"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

