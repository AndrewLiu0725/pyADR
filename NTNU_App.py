# import python module
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import pywinauto
import time
import numpy as np 
from PIL import Image
import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2

# import utility
from TextExtractor import TextExtractor

# import UI
import UI.AnalyticalParameters_UI
import UI.Homepage_UI
import UI.ValveActuatorControl_UI
from UI.OnOffSwitch import ToggleSwitch

DEBUG = 1

"""
all the corss class methods must write in App() class 
"""

# Open window for each UI
# ===============================================================================
class HomePage(QtWidgets.QMainWindow, UI.Homepage_UI.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class AnalyticalParameters(QtWidgets.QMainWindow, UI.AnalyticalParameters_UI.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class ValveActuatorControl(QtWidgets.QMainWindow, UI.ValveActuatorControl_UI.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)



# main class
# ===============================================================================
class App():
    def __init__(self):
        # initilization for GUI
        self.app = QtWidgets.QApplication(sys.argv)
        self.homepage = HomePage()
        self.AnalyticalParam = AnalyticalParameters()
        self.AnalyticalParam.TableContent = []
        self.AnalyticalParam_table_initialized = 0
        self.ValveActuatorControl = ValveActuatorControl()
        self.ValveActuatorControl_status = []
        self.ValveActuatorControl_status_initialized = 0

        # initialization for HTBasic
        app = pywinauto.application.Application(backend="uia").start(r"C:\Program Files (x86)\HTBwin10\HTBwin.exe")
        main_dlg = app["TransEra - HTBasic - [Untitled]"]
        main = main_dlg.wrapper_object()
        main.iface_transform.Move(0, 0) # move the window to top-left corner
        main.iface_transform.Resize(900, 600) # change width and height
        pywinauto.keyboard.send_keys("^o")
        LoadBasic = main_dlg['Open File']
        HTBasic_filepath = "D:\ARARSTAR\BLP3600\COLLECT\ARAUTO-3600m2020C"
        LoadBasic.child_window(title="File name:", auto_id="1148", control_type="ComboBox").child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys(HTBasic_filepath+"{ENTER}")
        LoadBasic.child_window(title="Open", auto_id="1", control_type="Button").click()
        self.HTBasic_dlg = app["TransEra - HTBasic - [{}]".format(HTBasic_filepath)]
        self.HTBasic_dlg.child_window(title="Run", control_type="Button").click()

    def run(self):
        # deal with click or keyin events
        self.homepage.pushButton.clicked.connect(self.enter_AnalyticalParam)
        self.homepage.pushButton_3.clicked.connect(self.enter_ValveActuatorControl)
        self.AnalyticalParam.pushButton.clicked.connect(self.exit_AnalyticalParam)
        self.ValveActuatorControl.pushButton.clicked.connect(self.exit_ValveActuatorControl)


        # start from main page
        self.homepage.show()

        # close program when pressing x(esc)
        sys.exit(self.app.exec_())

    # event solver
    # ===============================================================================
    def enter_ValveActuatorControl(self):
        self.HTBasic_dlg.type_keys("99")
        self.HTBasic_dlg.type_keys("{ENTER}")

        if not self.ValveActuatorControl_status_initialized:
            # take screentshot from console if first enter
            read_status = False
            while not read_status:
                time.sleep(0.5)
                Image.fromarray((np.asarray(self.HTBasic_dlg.capture_as_image()).copy())[200:300, 580:650]).save("./Figures/screenshot.png")
                status = TextExtractor("./Figures/screenshot.png").split('\n')[:-1]
                if len(status) == 6: read_status = True
            if DEBUG: print("The status in ValveActuatorControl is:\n",status)
            self.ValveActuatorControl_StatusSetup(status)
            self.ValveActuatorControl_status_initialized = 1

        self.ValveActuatorControl.show()
        self.homepage.hide()
        self.ValveActuatorControl.tableWidget.itemChanged.connect(self.ValveActuatorControl_StatusChange) # detect cell change

    def exit_ValveActuatorControl(self):
        self.HTBasic_dlg.type_keys("0")
        self.HTBasic_dlg.type_keys("{ENTER}")
        self.homepage.show()
        self.ValveActuatorControl.hide()

    def ValveActuatorControl_StatusSetup(self, status):
        for i in range(self.ValveActuatorControl.tableWidget.rowCount()):
            self.ValveActuatorControl_status.append(status[i])
            item = ToggleSwitch() # use switch.isChecked() to find its label
            if status[i] == "OPEN": item.setChecked(True)
            item.clicked.connect(self.ValveActuatorControl_StatusChange)
            self.ValveActuatorControl.tableWidget.setCellWidget(i, 0, item)

    def ValveActuatorControl_StatusChange(self):
        for i in range(self.ValveActuatorControl.tableWidget.rowCount()):
            current_status = "OPEN" if self.ValveActuatorControl.tableWidget.cellWidget(i, 0).isChecked() else "CLOSED"
            if current_status != self.ValveActuatorControl_status[i]:
                if DEBUG: print("row {} is switch from {} to {}".format(i+1, self.ValveActuatorControl_status[i], current_status))
                self.ValveActuatorControl_status[i] = current_status
                

    def enter_AnalyticalParam(self):
        self.HTBasic_dlg.type_keys("77")
        self.HTBasic_dlg.type_keys("{ENTER}")
        
        if not self.AnalyticalParam_table_initialized:
            # take screentshot from console if first enter
            read_status = False
            while not read_status:
                time.sleep(0.5)
                Image.fromarray((np.asarray(self.HTBasic_dlg.capture_as_image()).copy())[135:360, 480:520]).save("./Figures/screenshot.png")
                status = TextExtractor("./Figures/screenshot.png").split('\n')[:-1]
                if len(status) == 14: read_status = True
            if DEBUG: print("The status in AnalyticalParam is:\n",status)
            self.AnalyticalParam_TableSetup(status)
            self.AnalyticalParam_table_initialized = 1
        self.AnalyticalParam.show()
        self.homepage.hide()
        self.AnalyticalParam.tableWidget.itemChanged.connect(self.AnalyticalParam_parameter_change) # detect cell change

    def exit_AnalyticalParam(self):
        self.HTBasic_dlg.type_keys("0")
        self.HTBasic_dlg.type_keys("{ENTER}")
        self.homepage.show()
        self.AnalyticalParam.hide()
        

    def AnalyticalParam_TableSetup(self, dafault_value):
        # initialize the table (read the output from HTBasic)
        self.AnalyticalParam.TableContent = [] # a list of string
        for i in range(self.AnalyticalParam.tableWidget.rowCount()):
            val =  dafault_value[i]
            item = QtWidgets.QTableWidgetItem(val)
            self.AnalyticalParam.TableContent.append(val)
            self.AnalyticalParam.tableWidget.setItem(i, 0, item)


    def AnalyticalParam_parameter_change(self):
        for i in range(self.AnalyticalParam.tableWidget.rowCount()):
            show_warning = 0
            content = self.AnalyticalParam.tableWidget.item(i, 0).text()

            # check if the typed parameter is invalid
            if i < 7: # typed parameter must be number
                warning_msg = "Please key in positive integer!"
                try:
                    if int(content) <= 0:
                        show_warning = 1

                except: # not number
                    show_warning = 1

            else: # typed parameter must be yes or no
                warning_msg = "Please key in either yes or no!"
                if (content != "no") and (content != "yes"):
                    show_warning = 1 

            
            if show_warning:
                self.warningPopup(warning_msg)
                item = QtWidgets.QTableWidgetItem(str(self.AnalyticalParam.TableContent[i]))
                self.AnalyticalParam.tableWidget.setItem(i, 0, item)

            else:
                if content != self.AnalyticalParam.TableContent[i]: # parameter changed
                    self.AnalyticalParam.TableContent[i] = content # change the table content in GUI class
                    # send signal to HTBasic
                    if DEBUG: print("will type:", str(i+1)+"{ENTER}", content+"{ENTER}")
                    self.HTBasic_dlg.type_keys(str(i+1)) # which parameter
                    self.HTBasic_dlg.type_keys("{ENTER}")
                    time.sleep(0.1)
                    if (content == "no") or (content == "yes"):
                        self.HTBasic_dlg.type_keys(content[0]) # send y/n only (not yes/no)
                        self.HTBasic_dlg.type_keys("{ENTER}")
                    else:
                        self.HTBasic_dlg.type_keys(content)
                        self.HTBasic_dlg.type_keys("{ENTER}")


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