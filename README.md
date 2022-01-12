![logo](.work/logo.png)
# pyADR
## Introduction
pyADR is created by An-Jun (Andrew) Liu and is to automate Professor Mary Yeh's ArAr experiment data reduction process by providing a GUI that provides its own data analysis tools.
The following functions are provided:
1. T0 calculation
2. T0 statistics
3. Sample Measurement T0 and mass ratio calculation
4. Air ratio statistics
5. Age calculation

## Prerequisites
1. Anaconda3 (recommeded for Windows users)

(The following packages usually are already installed when you install Anaconda3.)

2. Python3
3. python related modules:
    * numpy
    * PyQt5
    * sys
    * matplotlib
    * scipy
    * requests
4. Additional python related modules for installation:
    * platform
    * subprocess
    * os
    * shutil

## User Guide
### Installation
1. Click the "Code" button on this github page and then 
    * either download and unzip this repo.
    * or clone it to your working folder by the following commad.
    ```
    git clone https://github.com/AndrewLiu0725/pyADR.git
    ```
2. Open the terminal (on Windows, recommend using Anaconda's prompt shell unless you already setup the environment variables in your prefered terminal) and type the following commands
    ```
    cd /path to folder you get in the previous step/
    python install.py
    ```
    A batch file named `pyADR.bat` (on Windows) or bash file named `pyADR.sh` (on Mac) will be created both in your working folder and on the desktop.

3. Click `pyADR.bat` (on Windows) or `pyADR.sh` (on Mac) and then pyADR will be launched.

### Change the parameters
1. To enter the parameter setting page,
    * either click `Parameter Setting` in the menubar.
    * or click the Parameter Setting button on the homepage.
2. Click Change button if you want to change the constants and the parameters pyADR uses.
3. Click Save button if you have changed the parameters, or the values you changed won't be saved.

### Raw data format
The raw data format should be as follow:
```
some headers

Cycle Number, Ar36, Current, Time
Cycle Number, Ar37, Current, Time
Cycle Number, Ar38, Current, Time
Cycle Number, Ar39, Current, Time
Cycle Number, Ar40, Current, Time

data for next cycle
...
```
**Note that there should be exactly one blank line between the data block of each cycle.**

**Please refer to the sample data in the 'Data/TestData' folder to see the format.**

### Main functions
Please refer to this document for further instructions.

### Note
The key in parameters and the raw data could be in standard (e.g. 0.11) and scientific (e.g. 1.1e-1) notations.

## Examples:
### 1. Age Calculation
1. Set the J value = 0.026703 and J std = 0.000035 on the Parameter Setting page (if you forget how to set the parameters, please read [this section](#change-the-parameters) again).
2. Click the Age Calculation button on the homepage.
3. Select file 'TestData_Measurement.csv' in the 'Data/TestData' folder.
4. The resultant age should be around 28Ma.

## Words from the developer
If you find this application useful, please star this repo. Your support is greatly appreciated!