# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LinearRegression.ui'
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
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(180, 40, 511, 79))
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 70, 16))
        self.label.setObjectName("label")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(30, 70, 91, 51))
        self.save.setObjectName("save")
        self.return_2 = QtWidgets.QPushButton(self.centralwidget)
        self.return_2.setGeometry(QtCore.QRect(30, 20, 91, 51))
        self.return_2.setObjectName("return_2")
        self.reselect = QtWidgets.QPushButton(self.centralwidget)
        self.reselect.setGeometry(QtCore.QRect(30, 120, 91, 51))
        self.reselect.setObjectName("reselect")
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
        self.photo.setGeometry(QtCore.QRect(150, 150, 600, 450))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../Figures/cat.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Description"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.return_2.setText(_translate("MainWindow", "Return"))
        self.reselect.setText(_translate("MainWindow", "Reselect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

