# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 12/31/2021
# ===============================================================================

import platform
import sys
import subprocess
import os
import shutil

msg = r'''
                  __     ______  ______ 
                 /  \   |  ___ \|  ___ \
                / /\ \  | |   \ | |___)|
  _______    __/ /__\ \ | |   | |  __  /
 |  __ \ \  / /  ____  \| |___/ | |  \ \
 | |__) \ \/ /__/     \_|______/|_|   \_\
 |  ___/ \  /
 | |     / /
 |_|    /_/

Developer: An-Jun (Andrew) Liu
Date: 07/23/2021
Updated: 12/31/2021
---*---*---*---*---*---*---*---*---*---*---*---*
Welcome to the pyADR Installer.
Press "Enter" to continue!
---*---*---*---*---*---*---*---*---*---*---*---*'''
print(msg)
input()

IS_MAC = platform.system() == 'Darwin'
IS_WINDOWS = platform.system() == 'Windows'

appName = 'pyADR'
filename = appName+'.bat' if IS_WINDOWS else appName+'.sh'
dir_path = os.path.dirname(os.path.realpath(__file__))

# write the file
with open(filename, 'w') as icon:
    if IS_WINDOWS:
        icon.write('@echo off\n')
        anaconda_folder = sys.executable[:-10]
        icon.write('call {}Scripts/activate.bat {}\n'.format(anaconda_folder, anaconda_folder))
    icon.write('cd {}\n'.format(dir_path))
    icon.write('{} {}'.format(sys.executable, os.path.abspath('NTNU_DataReduction.py')))

# set the permission
if IS_WINDOWS:
    subprocess.call(['CACLS', os.path.abspath(filename), '/e', '/p', 'Everyone:f'])
else:
    subprocess.call(['chmod', '777', os.path.abspath(filename)])

print("Successfully created the script in the working folder!")

# also create icon in the desktop
HOME = os.path.expanduser('~')
desktop_icon = os.path.join(HOME, 'DESKTOP', filename)
shutil.copyfile(os.path.abspath(filename), desktop_icon)

# set the permission
if IS_WINDOWS:
    subprocess.call(['CACLS', desktop_icon, '/e', '/p', 'Everyone:f'])
else:
    subprocess.call(['chmod', '777', desktop_icon])

print("Successfully created the script on the Desktop!")
print('Installation Complete!')