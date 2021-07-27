# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 07/23/2021
# ===============================================================================

import platform
import sys
import subprocess
import os
import shutil

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
    subprocess.call(['chmod', 'u+x', os.path.abspath(filename)])

# also create icon in the desktop
HOME = os.path.expanduser('~')
subprocess.call(['cp', os.path.abspath(filename), os.path.join(HOME, 'DESKTOP', filename)])

print('Installation Complete!')