# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 12/28/2021
# ===============================================================================

# import python module
import numpy as np 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests

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
        self.T0CalculationPage = LinearRegressionPage()
        self.insertPhoto(self.T0CalculationPage, [100, 230, 670, 450])
        self.ReselectDialog = ReselectTable()
        self.T0StatisticsPage = T0Statistics()
        self.insertPhoto(self.T0StatisticsPage, [150, 175, 600, 250])
        self.MassRatioPage = MassRatio()
        self.AirRatioStatisticsPage = AirRatioStatistics()
        self.insertPhoto(self.AirRatioStatisticsPage, [200, 200, 350, 275])
        self.AgeCalculationPage = AgeCalculation()
        self.ParameterSettingPage = ParameterSetting()

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
        for i in range(self.widget.count()):
            self.insertLogo(self.widget.widget(i))

        # others
        self.fitting_function_list = ["Linear", "Average"]
        self.mass_pair = ['Ar40/36', 'Ar37/39', 'Ar38/36', 'Ar40/38', 'Ar40/39']
        self.data_folder = 'Data/'
        self.screenshot_folder = 'Figures'
        with open('.app_info.txt', 'r') as f:
            self.app_info = f.readlines()

    def insertPhoto(self, page, coordinate):
        # coordinate = [x, y, w, h]
        page.photo = QtWidgets.QLabel(page.centralwidget)
        page.photo.setGeometry(QtCore.QRect(coordinate[0], coordinate[1], coordinate[2], coordinate[3]))
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
        self.HomePage.PS_button.clicked.connect(self.toPS)
        self.HomePage.actionParameter_Setting.triggered.connect(self.toPS)
        self.HomePage.actionAbout_pyADR.triggered.connect(self.systemInfo)
        self.HomePage.actionCheck_Update.triggered.connect(self.checkVersion)

        # click button on Linear Regression Page
        self.T0CalculationPage.return_2.clicked.connect(self.toMain)
        self.T0CalculationPage.save.clicked.connect(self.LRP_save)
        self.T0CalculationPage.reselect.clicked.connect(self.LRP_reselect)
        self.T0CalculationPage.linear.clicked.connect(self.LRP_useLinear)
        self.T0CalculationPage.average.clicked.connect(self.LRP_useAverage)
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

    # popup message box
    def Popup(self, msg_type, msg_title, msg_content):
        '''
        msg_type:
        0 NoIcon
        1 Information
        2 Warning
        3 Critical
        4 Question
        '''
        msg = QtWidgets.QMessageBox()
        msg.setIcon(msg_type)
        msg.setText("<font size = 10> {} </font> ".format(msg_title))
        msg.setInformativeText("<font size = 5> {} </font> ".format(msg_content.replace('\n', '<br>')))
        msg.setWindowTitle("")
        msg.exec_()

    # adjust table column and row size
    def TableAdjust(self, table):
        header = table.horizontalHeader()
        for i in range(table.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = table.verticalHeader()
        for i in range(table.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

    # display system info
    def systemInfo(self):
        self.Popup(1, "System Info", "".join(self.app_info))

    # check if current app is up to date
    def checkVersion(self):
        app_info_url = 'https://raw.githubusercontent.com/AndrewLiu0725/pyADR/main/.app_info.txt'
        try:
            page = requests.get(app_info_url)
            if page.ok:
                latest_version = page.text.split('\n')[1].rstrip()
                current_version = self.app_info[1].rstrip()
                version_msg = "Installed Version: {}\nLatest Version: {}\n".format(current_version, latest_version)
                if current_version == latest_version:
                    self.Popup(1, "No updates available at this time", version_msg)
                else:
                    git_repo_url = "https://github.com/AndrewLiu0725/pyADR.git"
                    self.Popup(1, "There are updates available at this time", version_msg+"Please go to {} to update to the latest version!\n".format(git_repo_url))
            else:
                self.Popup(2, "HTTP request failed!", "HTTP status {}".format(page.status_code))
        except:
            self.Popup(2, "No internet connection!", "Please check your internet connection!")

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
        # fill the table and set the item as disabled
        for i in range(self.numParamters):
            item = QtWidgets.QTableWidgetItem(self.parameters[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
            self.ParameterSettingPage.ParameetrTable.setItem(i, 0, item)
            
        # show the page
        self.TableAdjust(self.ParameterSettingPage.ParameetrTable)
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
            content = item.text().rstrip()

            # value changed
            if content != self.parameters[i]:
                error_type = 0
                # check if valid
                try:
                    if self.ParameterSettingPage.ParameetrTable.verticalHeaderItem(i).text() == 'numCycle':
                        if int(content) <= 0:
                            error_type = 1
                    else:
                        if float(content) < 0:
                            error_type = 2
                except:
                    error_type = 1 if i > 9 else 2
                
                # new valid value
                if error_type == 0:
                    self.parameters[i] = content # update the parameter
                    changed = 1 # need rewrite setting.csv

                # restore the value
                else:
                    item.setText(self.parameters[i]) 
                    invalid = 1
                    error_msg += '{} should be a {}.\n\n'.format(self.parameters_name[i], 
                    'positive integer' if error_type == 1 else 'non-negative number')

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
            self.Popup(2, 'Invalid Typed Parameters!', error_msg)
        

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
            try:
                J = float(self.parameters[self.parameters_name.index('J value')])
                J_std = float(self.parameters[self.parameters_name.index('J std')])
                self.AgeCalculation_result = Utilities.calcAge(measurement, J, J_std, [float(x) for x in self.parameters[:8]])
            
                # fill the table
                for i in range(53):
                    item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.AgeCalculation_result[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                    self.AgeCalculationPage.tableWidget.setItem(i//2 if i < 48 else i-24, i%2 if i < 48 else 0, item)

                self.AgeCalculationPage.age.setText('Age = {:.5} Ma'.format(self.AgeCalculation_result[46]/10**6))
                self.AgeCalculationPage.age.setFont(QtGui.QFont('Times', 20))

                # show the page
                self.TableAdjust(self.AgeCalculationPage.tableWidget)
                self.widget.setCurrentIndex(6)
            except:
                self.Popup(2, "Error!", "Please check the selected data format or the parameters!")

    def AC_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Age Calculation result" , self.data_folder, "(*.csv)")
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
            try:
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
                self.TableAdjust(self.AirRatioStatisticsPage.RatioTable)
                self.widget.setCurrentIndex(4)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")

    def ARS_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Air Ratio Statistics result" , self.data_folder, "(*.csv)")
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
            try:
                self.ratio_result = Utilities.calculateMassRatio(mass, bg)

                for i in range(5):
                    for j in range(5):
                        item = QtWidgets.QTableWidgetItem('{:0.5e}'.format(self.ratio_result[i][j]))
                        
                        item.setFlags(QtCore.Qt.ItemIsEnabled) # disable edit
                        if i < 3:
                            self.MassRatioPage.ValueTable.setItem(j, i, item)
                        else:
                            self.MassRatioPage.RatioTable.setItem(j, i-3, item)

                self.TableAdjust(self.MassRatioPage.ValueTable)
                self.TableAdjust(self.MassRatioPage.RatioTable)
                self.widget.setCurrentIndex(3)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")
        else:
            self.Popup(2, "Wrong Usage!", "Please select exactly one mass file first and then eactly one preline file")

    def MR_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement T0 result" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,Raw,Measurment,Measurement's Sigma\n")
            f.writelines(["Ar{},{},{},{}\n".format(i+36, self.ratio_result[0][i], self.ratio_result[1][i], self.ratio_result[2][i]) for i in range(5)])
            f.close()

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Measurement Ratio result" , self.data_folder, "(*.csv)")
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
            try:
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
                self.TableAdjust(self.T0StatisticsPage.tableWidget)
                self.widget.setCurrentIndex(2)
            except:
                self.Popup(2, "Error!", "Please check the selected data format!")

    def T0S_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save statistics
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Statistics result" , self.data_folder, "(*.csv)")
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
            
            self.numCycle = int(self.parameters[self.parameters_name.index("numCycle")])

            self.LRP_setReselectTable() # setup the reselect table here
            
            # collect the raw data
            if not self.LRP_loadRawData(filename):
                return 

            self.T0_fitting_function = 0 # default fitting function is linear
            self.mask = np.ones((5, self.numCycle)) # 1 means select this data point

            result = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask) # make LRP
            [self.tmp_T0, self.tmp_T0_SIGMA] = result[1:]
            self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
            self.T0CalculationPage.current_fit_func.setText("Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

            # show the page
            self.widget.setCurrentIndex(1)

    def LRP_loadRawData(self, filename):
        try:
            with open(filename, 'r') as f:
                data = f.readlines()

            # find the starting line of meaningful data
            for i in reversed(range(len(data))):
                stl = i
                if len(data[i].split()) == 4:
                    break
            stl -= (6*self.numCycle-2)

            # extract the data
            self.v_t = np.zeros((5, self.numCycle, 2))
            for i in range(self.numCycle):
                for j in range(5):
                    self.v_t[j, i, 0] = float((data[stl + 6*i + j].split())[2])
                    self.v_t[j, i, 1] = float((data[stl + 6*i + j].split())[3])
            return 1

        except:
            self.Popup(2, "Error!", "Please check the selected data format or the parameter numCycle!")
            return 0


    def LRP_save(self):
        # save screenshot
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save Screenshot" , self.screenshot_folder, "Images (*.png *.jpg *.jpeg)")
        if len(filename) > 0:
            self.widget.grab().save(filename)

        # save T0
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.widget, "Save T0 Calculation result" , self.data_folder, "(*.csv)")
        if len(filename) > 0:
            f = open(filename, 'w')
            f.write("Mass,T0,T0_SIGMA\n")
            f.writelines(["Ar{},{},{}\n".format(i+36, self.tmp_T0[i], self.tmp_T0_SIGMA[i]) for i in range(5)])
            f.close()

    def LRP_setReselectTable(self):
        w = self.ReselectDialog.frameGeometry().width()
        h = self.ReselectDialog.frameGeometry().height()
        self.ReselectDialog.ReselectTable = QtWidgets.QTableWidget(self.ReselectDialog)
        self.ReselectDialog.ReselectTable.setGeometry(QtCore.QRect(int(0.1*w), int(0.2*h), int(0.8*w), int(0.5*h)))
        self.ReselectDialog.ReselectTable.setObjectName("ReselectTable")
        self.ReselectDialog.ReselectTable.setColumnCount(self.numCycle)
        self.ReselectDialog.ReselectTable.setRowCount(5)
        self.ReselectDialog.ReselectTable.setVerticalHeaderLabels(['Ar {}'.format(i) for i in range(36, 41)])
        self.ReselectDialog.ReselectTable.setHorizontalHeaderLabels(['{}'.format(i) for i in range(1, self.numCycle+1)])
        
        header = self.ReselectDialog.ReselectTable.horizontalHeader()
        for i in range(self.ReselectDialog.ReselectTable.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.ReselectDialog.ReselectTable.verticalHeader()
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.ReselectDialog.ReselectTable.setItem(i, j, item)

    def LRP_reselect(self):
        self.ReselectDialog.show()
        self.ReselectDialog.buttonBox.accepted.connect(self.LRP_checkReselectTable)

    def LRP_checkReselectTable(self):
        for i in range(self.ReselectDialog.ReselectTable.rowCount()):
            for j in range(self.ReselectDialog.ReselectTable.columnCount()):
                item = self.ReselectDialog.ReselectTable.item(i, j)
                if item.checkState() == QtCore.Qt.Unchecked:
                    self.mask[i, j] = 0
                else:
                    self.mask[i, j] = 1

        result = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask)
        [self.tmp_T0, self.tmp_T0_SIGMA] = result[1:3]
        self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.ReselectDialog.close()

        if result[0] == 1:
            self.Popup(2, "Fitting Error!", "Unable to fit the manually selected data with {} fucntion!".format(self.fitting_function_list[self.T0_fitting_function]))

    def LRP_useLinear(self):
        self.LRP_switch_fitting_func(0)
    
    def LRP_useAverage(self):
        self.LRP_switch_fitting_func(1)

    def LRP_switch_fitting_func(self, fit_func_type):
        self.T0_fitting_function = fit_func_type
        result = Utilities.calculateT0(self.T0_fitting_function, self.v_t, self.mask) # make LRP
        [self.tmp_T0, self.tmp_T0_SIGMA] = result[1:3]
        self.T0CalculationPage.photo.setPixmap(QtGui.QPixmap(".work/LR.png")) # set image in the page
        self.T0CalculationPage.current_fit_func.setText("Current fitting function: {}".format(self.fitting_function_list[self.T0_fitting_function]))

        if result[0] == 1:
            self.Popup(2, "Fitting Error!", "Unable to fit the data with {} fucntion after manually removing the outliers!".format(self.fitting_function_list[self.T0_fitting_function]))


# main program
# ===============================================================================
ntnu_arar_app = App()
ntnu_arar_app.run()