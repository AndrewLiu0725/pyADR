import subprocess
import os

for file in os.listdir("UI"):
    if file[-3:] == '.ui':
        subprocess.call(["pyuic5", '-x', 'UI/'+file, '-o', 'UI/'+file[:-3]+'.py'])