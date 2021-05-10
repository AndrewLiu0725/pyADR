# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReselectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 395)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(120, 40, 481, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(5)
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)

        # add
        header = self.tableWidget.horizontalHeader()
        for i in range(self.tableWidget.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.tableWidget.setItem(i, j, item)

        self.retranslateUi(Dialog)
        #self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Ar 36"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Ar 37"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Ar 38"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Ar 39"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Ar 40"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "cycle 1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "cycle 2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "cycle 3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "cycle 4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "cycle 5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "cycle 6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "cycle 7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "cycle 8"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

