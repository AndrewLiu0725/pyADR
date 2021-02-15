import sys
import UI.AnalyticalParameters_UI
import UI.Homepage_UI
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import logging
import pywinauto

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
        # initilize
        self.app = QtWidgets.QApplication(sys.argv)
        self.homepage = HomePage()
        self.analyticalparam = AnalyticalParameters()
        self.analyticalparam.TableContent = []
        self.analyticalparam_table_initialized = 0

        app = pywinauto.application.Application(backend="uia").start(r"C:\Program Files (x86)\HTBwin10\HTBwin.exe")
        main_dlg = app["TransEra - HTBasic - [Untitled]"]
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
            a = [random.randint(1, 100) for _ in range(14)] # change here
            self.analyticalparam_tableSetup(a)
            self.analyticalparam_table_initialized = 1
        self.homepage.hide()
        self.analyticalparam.show()
        self.analyticalparam.tableWidget.itemChanged.connect(self.analyticalparam_setting_change) 

    def exit_analyticalparam(self):
        self.analyticalparam.hide()
        self.homepage.show()

    def analyticalparam_tableSetup(self, dafault_value):
        # initialize the table (read the output from HTBasic)
        self.analyticalparam.TableContent = []
        for i in range(self.analyticalparam.tableWidget.rowCount()):
            val =  dafault_value[i]
            item = QtWidgets.QTableWidgetItem(str(val))
            self.analyticalparam.TableContent.append(val)
            self.analyticalparam.tableWidget.setItem(i, 0, item)


    def analyticalparam_setting_change(self):
        for i in range(self.analyticalparam.tableWidget.rowCount()):
            show_warning = 0
            try:
                val = int(self.analyticalparam.tableWidget.item(i, 0).text())
                if val <= 0:
                    show_warning = 1
                else:
                    if val != self.analyticalparam.TableContent[i]:
                        self.analyticalparam.TableContent[i] = val

            except:
                show_warning = 1
            
            if show_warning:
                self.warningPopup("Please key in positive integer!")
                item = QtWidgets.QTableWidgetItem(str(self.analyticalparam.TableContent[i]))
                self.analyticalparam.tableWidget.setItem(i, 0, item)

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