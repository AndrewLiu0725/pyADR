# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 07/23/2021
# ===============================================================================

import platform
import sys
import subprocess
import os

IS_MAC = platform.system() == 'Darwin'
IS_WINDOWS = platform.system() == 'Windows'

appName = 'NTNU_DataReduction'
filename = appName+'.bat' if IS_WINDOWS else appName+'.sh'
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(filename, 'w') as icon:
    icon.write('cd {}\n'.format(dir_path))
    icon.write('{} {}'.format(sys.executable, os.path.abspath('NTNU_DataReduction.py')))
subprocess.call(['chmod', 'u+x', os.path.abspath(filename)])

print('Installation Complete!')