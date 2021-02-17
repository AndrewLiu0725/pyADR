import sys
import UI.AnalyticalParameters_UI
import UI.Homepage_UI
from PyQt5 import QtCore, QtGui, QtWidgets
import logging
import pywinauto
import time
import numpy as np 
from PIL import Image
from TextExtractor import TextExtractor
import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2

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



# main class
# ===============================================================================
class App():
    def __init__(self):
        # initilization for GUI
        self.app = QtWidgets.QApplication(sys.argv)
        self.homepage = HomePage()
        self.analyticalparam = AnalyticalParameters()
        self.analyticalparam.TableContent = []
        self.analyticalparam_table_initialized = 0

        # initialization for HTBasic
        app = pywinauto.application.Application(backend="uia").start(r"C:\Program Files (x86)\HTBwin10\HTBwin.exe")
        main_dlg = app["TransEra - HTBasic - [Untitled]"]
        main = main_dlg.wrapper_object()
        main.iface_transform.Move(0, 0) # move the window to top-left corner
        main.iface_transform.Resize(600, 600) # change width and height
        pywinauto.keyboard.send_keys("^o")
        LoadBasic = main_dlg['Open File']
        HTBasic_filepath = "D:\ARARSTAR\BLP3600\COLLECT\ARAUTO-3600m2020C"
        LoadBasic.child_window(title="File name:", auto_id="1148", control_type="ComboBox").child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys(HTBasic_filepath+"{ENTER}")
        LoadBasic.child_window(title="Open", auto_id="1", control_type="Button").click()
        self.HTBasic_dlg = app["TransEra - HTBasic - [{}]".format(HTBasic_filepath)]
        self.HTBasic_dlg.child_window(title="Run", control_type="Button").click()

    def run(self):
        # deal with click or keyin events
        self.homepage.pushButton.clicked.connect(self.enter_analyticalparam)
        self.analyticalparam.pushButton.clicked.connect(self.exit_analyticalparam)

        # start from main page
        self.homepage.show()

        # close program when pressing x(esc)
        sys.exit(self.app.exec_())

    # event solver
    # ===============================================================================
    def enter_analyticalparam(self):
        self.HTBasic_dlg.type_keys("77{ENTER}")
        
        if not self.analyticalparam_table_initialized:
            # take screentshot from console if first enter
            time.sleep(0.5)
            Image.fromarray((np.asarray(self.HTBasic_dlg.capture_as_image()).copy())[135:360, 480:520]).save("./Figures/screenshot.png")
            status = TextExtractor("./Figures/screenshot.png").split('\n')[:-1]
            if DEBUG: print("The status in AP is:\n",status)
            self.analyticalparam_tableSetup(status)
            self.analyticalparam_table_initialized = 1
        self.analyticalparam.show()
        self.homepage.hide()
        self.analyticalparam.tableWidget.itemChanged.connect(self.analyticalparam_parameter_change) # detect cell change

    def exit_analyticalparam(self):
        self.HTBasic_dlg.type_keys("0{ENTER}")
        self.homepage.show()
        self.analyticalparam.hide()
        

    def analyticalparam_tableSetup(self, dafault_value):
        # initialize the table (read the output from HTBasic)
        self.analyticalparam.TableContent = [] # a list of string
        for i in range(self.analyticalparam.tableWidget.rowCount()):
            val =  dafault_value[i]
            item = QtWidgets.QTableWidgetItem(val)
            self.analyticalparam.TableContent.append(val)
            self.analyticalparam.tableWidget.setItem(i, 0, item)


    def analyticalparam_parameter_change(self):
        for i in range(self.analyticalparam.tableWidget.rowCount()):
            show_warning = 0
            content = self.analyticalparam.tableWidget.item(i, 0).text()

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
                item = QtWidgets.QTableWidgetItem(str(self.analyticalparam.TableContent[i]))
                self.analyticalparam.tableWidget.setItem(i, 0, item)

            else:
                if content != self.analyticalparam.TableContent[i]: # parameter changed
                    self.analyticalparam.TableContent[i] = content # change the table content in GUI class
                    # send signal to HTBasic
                    if DEBUG: print("will type:", str(i+1)+"{ENTER}", content+"{ENTER}")
                    self.HTBasic_dlg.type_keys(str(i+1)+"{ENTER}") # which parameter
                    time.sleep(0.1)
                    self.HTBasic_dlg.type_keys(content[0]+"{ENTER}") # assign value


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