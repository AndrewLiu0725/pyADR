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

TEST = 1

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
        if TEST:
            mass = "Data/AS20210429a"
            bg = "Data/pb20210429a"

        ratio_result = Utilities.calculateMassRatio(mass, bg)

        for i in range(5):
            item = QtWidgets.QTableWidgetItem(str(ratio_result[i])[:11])
            self.MassRatio.List.setItem(i, 0, item)

        self.widget.setCurrentIndex(3)

    def toT0S(self):
        # select list of files
        if TEST:
            filelist = ["Data/AS20210429a", "Data/AS20210429b", "Data/AS20210429c"]

        # set the cell of the table of the T0 statistics
        T0_statistics = Utilities.getT0Statistics(filelist)
        for i in range(5):
            for j in range(2):
                item = QtWidgets.QTableWidgetItem(str(T0_statistics[i, j])[:11])
                self.T0Statistics.List.setItem(i, j, item)

        # show the page
        self.widget.setCurrentIndex(2) 

    def toLRP(self):
        # show up scroll down to choose file to male LRP
        if TEST:
            filename = "Data/pb20210429a"
        
        Utilities.calculateT0(filename, 1) # make LRP
        self.LinearRegressionPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page

        # show the page
        self.widget.setCurrentIndex(1)

    def toMain(self):
        self.widget.setCurrentIndex(0)

# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()