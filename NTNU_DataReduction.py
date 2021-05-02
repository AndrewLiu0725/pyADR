# import python module
import numpy as np 
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# import UI
import UI.DataReduction
import UI.LinearRegression
import UI.T0Statistics
import UI.MassRatio

# import utilities
import Utilities

TEST = 0

# load UI
# ===============================================================================
class HomePage(QtWidgets.QMainWindow, UI.DataReduction.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class LinearRegressionPage(QtWidgets.QMainWindow, UI.LinearRegression.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class T0Statistics(QtWidgets.QMainWindow, UI.T0Statistics.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class MassRatio(QtWidgets.QMainWindow, UI.MassRatio.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)


# main app
# ===============================================================================
class App():
    def __init__(self):
        # initilization for GUI
        QtWidgets.QApplication.setStyle('Fusion')
        self.app = QtWidgets.QApplication(sys.argv)
        self.HomePage = HomePage()
        self.LinearRegressionPage = LinearRegressionPage()
        self.T0Statistics = T0Statistics()
        self.MassRatio = MassRatio()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.HomePage)
        self.widget.addWidget(self.LinearRegressionPage)
        self.widget.addWidget(self.T0Statistics)
        self.widget.addWidget(self.MassRatio)
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(800)

    def run(self):
        # deal with click or keyin events
        self.HomePage.LRP.clicked.connect(self.toLRP)
        self.HomePage.T0S.clicked.connect(self.toT0S)
        self.HomePage.Ratio.clicked.connect(self.toRatio)
        self.LinearRegressionPage.return_2.clicked.connect(self.toMain)
        self.T0Statistics.Return.clicked.connect(self.toMain)
        self.MassRatio.Return.clicked.connect(self.toMain)

        self.widget.show()

        # close program when pressing x(esc)
        sys.exit(self.app.exec_())
    
    # methods added for UI operation
    # ===============================================================================
    # methods for switching pages
    def toRatio(self):
        # select mass and preline
        mass, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select mass file" , "./", "")
        bg, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select preline file" , "./", "")

        if len(mass) > 0 and len(bg) > 0:
            ratio_result = Utilities.calculateMassRatio(mass, bg)

            for i in range(5):
                item = QtWidgets.QTableWidgetItem(str(ratio_result[i])[:11])
                item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                self.MassRatio.List.setItem(i, 0, item)

            self.widget.setCurrentIndex(3)
        else:
            self.warningPopup("Please select one mass file and one preline file")

    def toT0S(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files to get T0 statistics" , "./", "") # select list of files

        if len(filelist) > 0:
            # set the cell of the table of the T0 statistics
            T0_statistics = Utilities.getT0Statistics(filelist)
            for i in range(5):
                for j in range(2):
                    item = QtWidgets.QTableWidgetItem(str(T0_statistics[i, j])[:11])
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.T0Statistics.List.setItem(i, j, item)

            # show the page
            self.widget.setCurrentIndex(2) 

    def toLRP(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0" , "./", "") # select file
        
        if len(filename) > 0:
            Utilities.calculateT0(filename, 1) # make LRP
            self.LinearRegressionPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page

            # show the page
            self.widget.setCurrentIndex(1)

    def toMain(self):
        self.widget.setCurrentIndex(0)

    # warning message box
    def warningPopup(self, waring_msg):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Warning")
        msg.setInformativeText(waring_msg)
        msg.setWindowTitle("")
        msg.exec_()

# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()