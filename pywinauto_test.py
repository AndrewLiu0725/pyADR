from pywinauto import application
from pywinauto import keyboard

# Open ARAUTO-3600.bas
app = application.Application(backend="uia").start(r"C:\Program Files (x86)\HTBwin10\HTBwin.exe")
main_dlg = app["TransEra - HTBasic - [Untitled]"]
keyboard.send_keys("^o")
LoadBasic = main_dlg['Open File']
HTBasic_filepath = "D:\ARARSTAR\BLP3600\COLLECT\ARAUTO-3600m2020C"
#LoadBasic.child_window(title="File name:", auto_id="1148", control_type="ComboBox").Edit.type_keys(HTBasic_filepath)
LoadBasic.child_window(title="File name:", auto_id="1148", control_type="ComboBox").child_window(title="File name:", auto_id="1148", control_type="Edit").type_keys(HTBasic_filepath+"{ENTER}")
LoadBasic.child_window(title="Open", auto_id="1", control_type="Button").click()
#LoadBasic.child_window(title="Open", auto_id="1", control_type="Button").click()
#LoadBasic.Open4.click()
#LoadBasic.Open4.click()
#main_dlg = app.child_window(title="TransEra - HTBasic - [{}.bas]".format(HTBasic_filepath), control_type="Window")
main_dlg = app["TransEra - HTBasic - [{}]".format(HTBasic_filepath)]
#main_dlg.Run.click()
main_dlg.child_window(title="Run", control_type="Button").click()
#main_dlg.print_control_identifiers()
main_dlg.type_keys("77{ENTER}")
#main_dlg.type_keys("{ENTER}")

# functions to interact with .bas file

# interactive GUI for user