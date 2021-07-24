![logo](.work/logo.png)
# pyADR
## Introduction
pyADR is created by An-Jun (Andrew) Liu and is to automate Professor Mary Yeh's ArAr experiment data reduction process by providing a GUI which provides its own data analysis tool.
The following functions are provided:
1. T0 calculation
2. T0 statistics
3. Sample Measurement T0 and mass ratio calculation
4. Air ratio statistics
5. Age calculation

## Prerequisites
1. Anaconda3
The followings are usually already installed when you install Anaconda3
2. Python3
3. python related modules:
* numpy
* PyQt5
* sys
* matplotlib
* scipy
4. Additional python related modules for installation:
* platform
* subprocess
* os

## User Guide
### Installation
1. Download or clone this repo
2. Open the terminal (on Windows, recommend using Anaconda's prompt shell) and type the following commands
```
cd /path to folder you get in the previous step/
python install.py
```
A batch file (on Windows) or bash file (on Mac) will be created.

3. Click the file named pyADR and then the application will be launched.

### Change the parameters
1. In the menubar, click "Parameter Setting", the the parameter setting page will show up. 
2. Click Change button if you want to change the constants and the parameters this application uses.
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
***Note that there should be a blank line between the data block of each cycle.***
***Please refer to the sample data in the 'Data/TestData' folder to see the format.***

### Main functions
Please refer to this document for further instructions.

### Note
The key in parameters and the raw data should be either in regular number or in scientific notation like 1.0e-2.

## Example:
### Age Calculation
1. Click the Age Calculation button in the homepage
2. Select file 'TestData_Measurement.csv' in the 'Data/TestData' folder
3. Key in J = 0.026703 and Sigma J = 0.000035
4. The age should be around 28Ma

## Words from the developer
If you find this application useful, please star this repo.