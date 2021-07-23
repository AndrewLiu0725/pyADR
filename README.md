# Name of the App
## Introduction
This application is to automate Professor Mary Yeh's ArAr experiment data reduction process by providing a GUI which provides its own data analysis tool.
The following functions are provided:
1. T0 calculation
2. T0 statistics
3. Sample Measurement T0 and mass ratio calculation
4. Air ratio statistics
5. Age calculation

## Prerequisites
1. Python3
2. python related modules (usually already installed when you installed your python3):
(1). numpy
(2). PyQt5
(3). sys
(4). matplotlib
(5). scipy

## User Guide
### Installation
1. Download or clone this repo
2. Open the terminal and type the following commands
```
cd /path to folder you get in the previous step/
python install.py
```
A batch file (on Windows) or (on Mac) will be created.
3. Click the icon and then the application will be launched.

### Change the parameters
1. In the menubar, click "Parameter Setting", the the parameter setting page will show up. 
2. Click Change button if you want to change the constants and the parameters this application uses.
3. Click Save button if you have changed the parameters, or the values you changed won't be saved.

### Main functions
Please refer to this document for further instructions.

## Example:
### Age Calculation
1. Click the Age Calculation button in the homepage
2. Select file 'TestData_Measurement.csv' in the 'Data/TestDate' folder
3. Key in J = 0.026703 and Sigma J = 0.000035
4. The age should be around 28Ma