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
import UI.AirRatioStatistics
import UI.ReselectDialog

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

class AirRatioStatistics(QtWidgets.QMainWindow, UI.AirRatioStatistics.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class ReselectTable(QtWidgets.QDialog, UI.ReselectDialog.Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
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
        self.AirRatioStatistics = AirRatioStatistics()
        self.ReselectDialog = ReselectTable()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.HomePage)
        self.widget.addWidget(self.LinearRegressionPage)
        self.widget.addWidget(self.T0Statistics)
        self.widget.addWidget(self.MassRatio)
        self.widget.addWidget(self.AirRatioStatistics)
        self.widget.setFixedHeight(600)
        self.widget.setFixedWidth(800)

    def run(self):
        # deal with click or keyin events
        # click button on Homepage
        self.HomePage.LRP.clicked.connect(self.toLRP)
        self.HomePage.T0S.clicked.connect(self.toT0S)
        self.HomePage.MR.clicked.connect(self.toMR)
        self.HomePage.ARS.clicked.connect(self.toARS)

        # click button on Linear Regression Page
        self.LinearRegressionPage.return_2.clicked.connect(self.toMain)
        self.LinearRegressionPage.save.clicked.connect(self.LRP_save)
        self.LinearRegressionPage.reselect.clicked.connect(self.LRP_reselect)

        # click button on T0 statistics page
        self.T0Statistics.return_2.clicked.connect(self.toMain)
        self.T0Statistics.save.clicked.connect(self.T0S_save)

        # click button on Mass Ratio page
        self.MassRatio.return_2.clicked.connect(self.toMain)
        self.MassRatio.save.clicked.connect(self.MR_save)

        # click button on Air Ratio Statistics page
        self.AirRatioStatistics.return_2.clicked.connect(self.toMain)
        self.AirRatioStatistics.save.clicked.connect(self.ARS_save)

        self.widget.show()

        # close program when pressing x(esc)
        sys.exit(self.app.exec_())
    
    # methods added for UI operation
    # ===============================================================================
    # back to Homepage
    def toMain(self):
        self.widget.setCurrentIndex(0)

    # methods for Air Ratio Statistics
    def toARS(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Air Ratio statistics" , "./", "(*.csv)") # select list of files

        if len(filelist) > 0:
            # set the cell of the table of the T0 statistics
            self.AirRatio_statistics_result = Utilities.getAirRatioStatistics(filelist)
            for i in range(2):
                item = QtWidgets.QTableWidgetItem('{}'.format(round(self.AirRatio_statistics_result[i],2)))
                item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                self.AirRatioStatistics.RatioTable.setItem(i, 0, item)

            # set # of selected files
            self.AirRatioStatistics.numSelectedFiles.setText("n = {}".format(len(filelist)))
            self.AirRatioStatistics.numSelectedFiles.setFont(QtGui.QFont('Times', 20))

            # set image
            self.AirRatioStatistics.photo.setPixmap(QtGui.QPixmap(".work/ARS.png"))

            # show the page
            self.widget.setCurrentIndex(4)

    def ARS_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , "./", "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Air Ratio Statistics" , "./", "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Air Ratio,Mean,STD\n")
            f.write("Ar 40/39,{},{}\n".format(self.AirRatio_statistics_result[0], self.AirRatio_statistics_result[1]))
            f.close()

    # methods for Mass Ratio
    def toMR(self):
        # select mass and preline
        mass, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select mass file (csv)" , "./", "(*.csv)")
        bg, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select preline file (csv)" , "./", "(*.csv)")

        if len(mass) > 0 and len(bg) > 0:
            self.ratio_result = Utilities.calculateMassRatio(mass, bg)

            for i in range(2):
                for j in range(5):
                    item = QtWidgets.QTableWidgetItem(str(self.ratio_result[i][j])[:11])
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    if i == 0:
                        self.MassRatio.ValueTable.setItem(j, 0, item)
                    else:
                        self.MassRatio.RatioTable.setItem(j, 0, item)

            self.widget.setCurrentIndex(3)
        else:
            self.Popup("Warning!", "Please select one mass file and one preline file")

    def MR_save(self):
        mass_pair = ['Ar40/36', 'Ar37/39', 'Ar36/38', 'Ar40/38', 'Ar40/39']
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Mass Ratio" , "./", "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Mass - Sample blank,Mass Pair,Ratio\n")
            f.writelines(["Ar{},{},{},{}\n".format(i+36, self.ratio_result[0][i], mass_pair[i], self.ratio_result[1][i]) for i in range(5)])
            f.close()


    # methods for T0 Statistics
    def toT0S(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get T0 statistics" , "./", "(*.csv)") # select list of files

        if len(filelist) > 0:
            # set the cell of the table of the T0 statistics
            self.T0_statistics_result = Utilities.getT0Statistics(filelist)
            for i in range(5):
                for j in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.4e}'.format(self.T0_statistics_result[i, j]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.T0Statistics.tableWidget.setItem(j, i, item)

            # set # of selected files
            self.T0Statistics.numSelectedFiles.setText("n = {}".format(len(filelist)))
            self.T0Statistics.numSelectedFiles.setFont(QtGui.QFont('Times', 20))

            # set image
            self.T0Statistics.photo.setPixmap(QtGui.QPixmap(".work/T0S.png"))

            # show the page
            self.widget.setCurrentIndex(2) 

    def T0S_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , "./", "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Statistics" , "./", "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Mean,STD\n")
            f.writelines(["Ar{},{},{}\n".format(i+36, self.T0_statistics_result[i,0], self.T0_statistics_result[i,1]) for i in range(5)])
            f.close()

    
    # methods for Linear Regression Page
    def toLRP(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0" , "./", "") # select file
        if len(filename) > 0:
            self.tmp_T0 = Utilities.calculateT0(filename, 0, None) # make LRP
            self.LinearRegressionPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page

            # show the page
            self.widget.setCurrentIndex(1)

            self.filename = filename

    def LRP_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , "./", "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save T0
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0" , "./", "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,T0\n")
            f.writelines(["Ar{},{}\n".format(i+36, self.tmp_T0[i]) for i in range(5)])
            f.close()

    def LRP_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.LRP_checkReselectTable)

    def LRP_checkReselectTable(self):
        mask = np.zeros((5, 8))
        for i in range(self.ReselectDialog.tableWidget.rowCount()):
            for j in range(self.ReselectDialog.tableWidget.columnCount()):
                item = self.ReselectDialog.tableWidget.item(i, j)
                if item.checkState() == QtCore.Qt.Unchecked:
                    mask[i, j] = 1
        Utilities.calculateT0(self.filename, 1, mask)
        self.LinearRegressionPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.ReselectDialog.close()
    

    # warning message box
    def Popup(self, msg_type, msg_content):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(msg_type)
        msg.setInformativeText(msg_content)
        msg.setWindowTitle("")
        msg.exec_()

# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()