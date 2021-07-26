# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 07/23/2021
# ===============================================================================

# import python module
import numpy as np 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# import UI
import UI.HomePage
import UI.LinearRegression
import UI.T0Statistics
import UI.MassRatio
import UI.AirRatioStatistics
import UI.ReselectDialog
import UI.ParameterSetting
import UI.AgeCalculation

# import utilities
import Utilities



# load UI
# ===============================================================================
class HomePage(QtWidgets.QMainWindow, UI.HomePage.Ui_MainWindow):
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

class ParameterSetting(QtWidgets.QMainWindow, UI.ParameterSetting.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class AgeCalculation(QtWidgets.QMainWindow, UI.AgeCalculation.Ui_MainWindow):
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
        self.insertLogo(self.HomePage)
        self.T0CalculationPage = LinearRegressionPage()
        self.insertPhoto(self.T0CalculationPage, [150, 250, 600, 450])
        self.insertLogo(self.T0CalculationPage)
        self.T0StatisticsPage = T0Statistics()
        self.insertPhoto(self.T0StatisticsPage, [150, 175, 600, 250])
        self.insertLogo(self.T0StatisticsPage)
        self.MassRatioPage = MassRatio()
        self.insertLogo(self.MassRatioPage)
        self.AirRatioStatisticsPage = AirRatioStatistics()
        self.insertPhoto(self.AirRatioStatisticsPage, [200, 200, 350, 275])
        self.insertLogo(self.AirRatioStatisticsPage)
        self.ReselectDialog = ReselectTable()
        self.ParameterSettingPage = ParameterSetting()
        self.insertLogo(self.ParameterSettingPage)
        self.AgeCalculationPage = AgeCalculation()
        self.insertLogo(self.AgeCalculationPage)
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.HomePage)
        self.widget.addWidget(self.T0CalculationPage)
        self.widget.addWidget(self.T0StatisticsPage)
        self.widget.addWidget(self.MassRatioPage)
        self.widget.addWidget(self.AirRatioStatisticsPage)
        self.widget.addWidget(self.ParameterSettingPage)
        self.widget.addWidget(self.AgeCalculationPage)
        self.widget.setFixedHeight(700)
        self.widget.setFixedWidth(800)

        # others
        self.fitting_function_list = ["Linear", "Asymptotic"]
        self.mass_pair = ['Ar40/36', 'Ar37/39', 'Ar38/36', 'Ar40/38', 'Ar40/39']
        self.data_folder = 'Data/'
        self.screenshot_folder = 'Figures'

    def insertPhoto(self, page, coordinate):
        # coordinate = [x, y, w, h]
        page.photo = QtWidgets.QLabel(page.centralwidget)
        page.photo.setGeometry(QtCore.QRect(coordinate[0], coordinate[1], coordinate[2], coordinate[3]))
        page.photo.setText("")
        page.photo.setPixmap(QtGui.QPixmap(".work/cat.png"))
        page.photo.setScaledContents(True)
        page.photo.setObjectName("photo")

    def insertLogo(self, page):
        # coordinate = [x, y, w, h]
        page.logo = QtWidgets.QLabel(page.centralwidget)
        page.logo.setGeometry(QtCore.QRect(50, 25, 700, 75))
        page.logo.setText("")
        page.logo.setPixmap(QtGui.QPixmap(".work/logo.png"))
        page.logo.setScaledContents(True)
        page.logo.setObjectName("logo")

    # ===============================================================================
    def run(self):
        # load parameters
        self.loadParameterSeting()

        # deal with click or keyin events
        # click button on Homepage
        self.HomePage.LRP.clicked.connect(self.toLRP)
        self.HomePage.T0S.clicked.connect(self.toT0S)
        self.HomePage.MR.clicked.connect(self.toMR)
        self.HomePage.ARS.clicked.connect(self.toARS)
        self.HomePage.AC.clicked.connect(self.toAC)
        self.HomePage.actionParameter_Setting.triggered.connect(self.toPS)

        # click button on Linear Regression Page
        self.T0CalculationPage.return_2.clicked.connect(self.toMain)
        self.T0CalculationPage.save.clicked.connect(self.LRP_save)
        self.T0CalculationPage.reselect.clicked.connect(self.LRP_reselect)
        self.T0CalculationPage.linear.clicked.connect(self.LRP_useLinear)
        self.T0CalculationPage.asymptotic.clicked.connect(self.LRP_useAsymptotic)
        self.T0CalculationPage.new_2.clicked.connect(self.toLRP)

        # click button on T0 statistics page
        self.T0StatisticsPage.return_2.clicked.connect(self.toMain)
        self.T0StatisticsPage.save.clicked.connect(self.T0S_save)
        self.T0StatisticsPage.new_2.clicked.connect(self.toT0S)

        # click button on Mass Ratio page
        self.MassRatioPage.return_2.clicked.connect(self.toMain)
        self.MassRatioPage.save.clicked.connect(self.MR_save)
        self.MassRatioPage.new_2.clicked.connect(self.toMR)

        # click button on Air Ratio Statistics page
        self.AirRatioStatisticsPage.return_2.clicked.connect(self.toMain)
        self.AirRatioStatisticsPage.save.clicked.connect(self.ARS_save)
        self.AirRatioStatisticsPage.new_2.clicked.connect(self.toARS)

        # click button on Parameter Setting page
        self.ParameterSettingPage.return_2.clicked.connect(self.toMain)
        self.ParameterSettingPage.change.clicked.connect(self.PS_change)
        self.ParameterSettingPage.save.clicked.connect(self.PS_save)
        self.ParameterSettingPage.cancel.clicked.connect(self.PS_cancel)

        # click button on Age Calculation page
        self.AgeCalculationPage.return_2.clicked.connect(self.toMain)
        self.AgeCalculationPage.save.clicked.connect(self.AC_save)
        self.AgeCalculationPage.new_2.clicked.connect(self.toAC)

        self.widget.show()

        # close program when pressing x(esc)
        sys.exit(self.app.exec_())
    
    # methods added for UI operation
    # ===============================================================================
    # back to Homepage
    def toMain(self):
        self.widget.setCurrentIndex(0)

    # warning message box
    def Popup(self, msg_type, msg_content):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(msg_type)
        msg.setInformativeText(msg_content)
        msg.setWindowTitle("")
        msg.exec_()

    # methods for parameters setting page
    # ===============================================================================
    def loadParameterSeting(self):
        with open('.work/setting.csv', 'r') as f:
            data = f.readlines()

        self.numParamters = int(data[1].split(',')[1])
        self.parameters = []
        self.parameters_name = []
        # first row is header and second row is # of parameters
        for i in range(self.numParamters):
            self.parameters_name.append(data[i+2].split(',')[0].rstrip())
            self.parameters.append(data[i+2].split(',')[1].rstrip())


    def toPS(self):
        # load the parameters from setting file
        self.loadParameterSeting()

        # fill the table and set the item as disabled
        for i in range(self.numParamters):
            item = QtWidgets.QTableWidgetItem(self.parameters[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.ParameterSettingPage.ParameetrTable.setItem(i, 0, item)
            
        # show the page
        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()
        self.widget.setCurrentIndex(5)

    def PS_change(self):
        # show the save and cancel button, hide the change button
        self.ParameterSettingPage.cancel.show()
        self.ParameterSettingPage.save.show()
        self.ParameterSettingPage.change.hide()

        # enable edit (need better way to implement)
        for i in range(self.numParamters):
            item = QtWidgets.QTableWidgetItem(self.parameters[i])
            self.ParameterSettingPage.ParameetrTable.setItem(i, 0, item) # make cell editable

    def PS_save(self):
        error_msg = ''
        changed = 0
        invalid = 0

        for i in range(self.numParamters):
            item = self.ParameterSettingPage.ParameetrTable.item(i, 0)
            content = item.text()

            # value changed
            if content != self.parameters[i]:
                error_type = 0
                # check if valid
                try:
                    if i > 9:
                        if int(content) <= 0:
                            error_type = 1
                    else:
                        if float(content) <= 0:
                            error_type = 2
                except:
                    error_type = 1 if i > 9 else 2
                
                # new valid value
                if error_type == 0:
                    self.parameters[i] = content.rstrip() # update the parameter
                    changed = 1 # need rewrite setting.csv

                # restore the value
                else:
                    item.setText(self.parameters[i]) 
                    invalid = 1
                    error_msg += '{} should be {}\n\n'.format(self.parameters_name[i], 
                    'positive integer' if error_type == 1 else 'positive number')

            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit

        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()

        # rewite setting.csv with update parameters value if necessary
        if changed:
            new_ps = ['parameter,value\n', 'numParameters,{}\n'.format(self.numParamters)]
            for i in range(self.numParamters):
                new_ps.append('{},{}\n'.format(self.parameters_name[i], self.parameters[i]))

            with open('.work/setting.csv', 'w') as f:
                f.writelines(new_ps)

        if invalid:
            self.Popup('Warning!', error_msg)
        

    def PS_cancel(self):
        # restore to previous value
        for i in range(self.numParamters):
            item = self.ParameterSettingPage.ParameetrTable.item(i, 0)
            item.setText(self.parameters[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit

        self.ParameterSettingPage.change.show()
        self.ParameterSettingPage.cancel.hide()
        self.ParameterSettingPage.save.hide()


    # methods for age calculation page
    # ===============================================================================
    def toAC(self):
        measurement, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select measurement file (csv)" , self.data_folder, "(*.csv)")
        if len(measurement) > 0:
            # ask J and J_std
            for i in range(2):
                text, ok = QtWidgets.QInputDialog.getText(self.widget, 'Set j value' if i == 0 else 'Set sigma J', 
                'please key in J value' if i == 0 else 'please key in sigma J value')
                if ok:
                    try:
                        if float(text) < 0:
                            self.Popup('Warning!', "please key in non-negative number!")
                            return
                        else:
                            if i == 0:
                                J = float(text)
                            else:
                                J_std = float(text)
                    except:
                        self.Popup('Warning!', "please key in non-negative number!")
                        return
                else:
                    return

            self.AgeCalculation_result = Utilities.calcAge(measurement, J, J_std, [float(x) for x in self.parameters[:8]])
        
            # fill the table
            for i in range(53):
                item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.AgeCalculation_result[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                self.AgeCalculationPage.tableWidget.setItem(i//2 if i < 48 else i-24, i%2 if i < 48 else 0, item)

            self.AgeCalculationPage.age.setText('Age = {:.5} Ma'.format(self.AgeCalculation_result[46]/10**6))
            self.AgeCalculationPage.age.setFont(QtGui.QFont('Times', 20))

            # show the page
            self.widget.setCurrentIndex(6)

    def AC_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Age Calculation Date" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Variable,Value,Sigma\n")
            for i in range(self.AgeCalculationPage.tableWidget.rowCount()):
                f.write('{},{},{}\n'.format(self.AgeCalculationPage.tableWidget.verticalHeaderItem(i).text(),
                self.AgeCalculation_result[2*i] if i < 24 else self.AgeCalculation_result[i + 24],
                self.AgeCalculation_result[2*i+1] if i < 24 else 'N/A'))
            f.close()



    # methods for Air Ratio Statistics
    # ===============================================================================
    def toARS(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get Air Ratio statistics" , self.data_folder, "(*.csv)") # select list of files

        if len(filelist) > 0:
            # set the cell of the table of the T0 statistics
            self.AirRatio_statistics_result = Utilities.getAirRatioStatistics(filelist, float(self.parameters[5]), float(self.parameters[6]))
            for i in range(2):
                for j in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.AirRatio_statistics_result[i, j]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.AirRatioStatisticsPage.RatioTable.setItem(j, i, item)

            # set # of selected files
            self.AirRatioStatisticsPage.numSelectedFiles.setText("n = {}".format(len(filelist)))
            self.AirRatioStatisticsPage.numSelectedFiles.setFont(QtGui.QFont('Times', 20))

            # set image
            self.AirRatioStatisticsPage.photo.setPixmap(QtGui.QPixmap(".work/ARS.png"))

            # show the page
            self.widget.setCurrentIndex(4)

    def ARS_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Air Ratio Statistics" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Air Ratio,Mean,STD\n")
            f.write("Ar 40/36,{},{}\n".format(self.AirRatio_statistics_result[0, 0], self.AirRatio_statistics_result[0, 1]))
            f.write("Ar 38/36,{},{}\n".format(self.AirRatio_statistics_result[1, 0], self.AirRatio_statistics_result[1, 1]))
            f.close()

    # methods for Mass Ratio
    # ===============================================================================
    def toMR(self):
        # select mass and preline
        mass, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select mass file (csv)" , self.data_folder, "(*.csv)")
        bg, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select preline file (csv)" , self.data_folder, "(*.csv)")

        if len(mass) > 0 and len(bg) > 0:
            self.ratio_result = Utilities.calculateMassRatio(mass, bg)

            for i in range(5):
                for j in range(5):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.ratio_result[i][j]))
                    
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    if i < 3:
                        self.MassRatioPage.ValueTable.setItem(j, i, item)
                    else:
                        self.MassRatioPage.RatioTable.setItem(j, i-3, item)

            self.widget.setCurrentIndex(3)
        else:
            self.Popup("Warning!", "Please select one mass file and one preline file")

    def MR_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement T0" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Raw,Measurment,Measurement's Sigma\n")
            f.writelines(["Ar{},{},{},{}\n".format(i+36, self.ratio_result[0][i], self.ratio_result[1][i], self.ratio_result[2][i]) for i in range(5)])
            f.close()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement Ratio" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Ratio,Value,Ratio's Sigma\n")
            f.writelines(["{},{},{}\n".format(self.mass_pair[i], self.ratio_result[3][i], self.ratio_result[4][i]) for i in range(5)])
            f.close()


    # methods for T0 Statistics
    # ===============================================================================
    def toT0S(self):
        filelist, _ = QtWidgets.QFileDialog.getOpenFileNames(self.widget, "Select files (csv) to get T0 statistics" , self.data_folder, "(*.csv)") # select list of files

        if len(filelist) > 0:
            # set the cell of the table of the T0 statistics
            self.T0_statistics_result = Utilities.getT0Statistics(filelist)
            for i in range(5):
                for j in range(2):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.T0_statistics_result[i, j]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.T0StatisticsPage.tableWidget.setItem(j, i, item)

            # set # of selected files
            self.T0StatisticsPage.numSelectedFiles.setText("n = {}".format(len(filelist)))
            self.T0StatisticsPage.numSelectedFiles.setFont(QtGui.QFont('Times', 20))

            # set image
            self.T0StatisticsPage.photo.setPixmap(QtGui.QPixmap(".work/T0S.png"))

            # show the page
            self.widget.setCurrentIndex(2) 

    def T0S_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Statistics" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Mean,STD\n")
            f.writelines(["Ar{},{},{}\n".format(i+36, self.T0_statistics_result[i,0], self.T0_statistics_result[i,1]) for i in range(5)])
            f.close()

    
    # methods for T0 Calculation Page
    # ===============================================================================
    def toLRP(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.widget, "Select file to calculate T0" , self.data_folder, "") # select file
        if len(filename) > 0:
            self.T0_fitting_function = 0 # default fitting function is linear
            result = Utilities.calculateT0(self.T0_fitting_function, int(self.parameters[10]), float(self.parameters[8]), int(self.parameters[9]), filepath = filename) # make LRP
            [self.tmp_T0, self.tmp_T0_SIGMA, self.tmp_v_t] = result[1:]
            self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
            self.T0CalculationPage.current_fit_func.setText("Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            if result[0] == 1:
                self.Popup("Warning!", "Unable to fit the data with {} fucntion after removing the auto-selected outliers!".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def LRP_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save T0
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,T0,T0_SIGMA\n")
            f.writelines(["Ar{},{},{}\n".format(i+36, self.tmp_T0[i], self.tmp_T0_SIGMA[i]) for i in range(5)])
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

        result = Utilities.calculateT0(self.T0_fitting_function, int(self.parameters[10]), float(self.parameters[8]), int(self.parameters[9]), v_t=self.tmp_v_t, mask=mask)
        [self.tmp_T0, self.tmp_T0_SIGMA] = result[1:3]
        self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.ReselectDialog.close()

        if result[0] == 1:
            self.Popup("Warning!", "Unable to fit the selected data with {} fucntion!".format(self.fitting_function_list[self.T0_fitting_function]))


    def LRP_useLinear(self):
        self.LRP_switch_fitting_func(0)
    
    def LRP_useAsymptotic(self):
        self.LRP_switch_fitting_func(1)

    def LRP_switch_fitting_func(self, fit_func_type):
        result = Utilities.calculateT0(fit_func_type, int(self.parameters[10]), float(self.parameters[8]), int(self.parameters[9]), v_t=self.tmp_v_t) # make LRP

        if result[0] == 2:
            self.Popup("Warning!", "Unable to fit the raw data with {} fucntion!".format(self.fitting_function_list[fit_func_type]))
        
        else:
            [self.tmp_T0, self.tmp_T0_SIGMA] = result[1:3]
            self.T0_fitting_function = fit_func_type
            self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
            self.T0CalculationPage.current_fit_func.setText("Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            if result[0] == 1:
                self.Popup("Warning!", "Unable to fit the data with {} fucntion after removing the auto-selected outliers!".format(self.fitting_function_list[self.T0_fitting_function]))


# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()