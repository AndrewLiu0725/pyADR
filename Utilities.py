# ===============================================================================
# Copyright 2021 An-Jun Liu
# Last Modified Date: 07/23/2021
# ===============================================================================

import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.function_base import diff
from numpy.testing._private.utils import measure
from scipy.optimize import curve_fit
from scipy.sparse import base

DEBUG = 1

# Utilities function
def ratioSigma(mu_y, sigma_y, mu_x, sigma_x):
    return np.sqrt((sigma_y/mu_x)**2 + (sigma_x*mu_y/(mu_x**2))**2)

def minusSigma(sigma_x, sigma_y):
    return np.sqrt(sigma_x**2 + sigma_y**2)

# T0 regression fitting functions
# ===============================================================================
def linear(x, a, b):
    return a*x + b


def asymptotic(x, a, b, c, n):
    return a * x ** n  / (x ** n + b) + c

fit_func_list = [linear, asymptotic]

# functions for button
# ===============================================================================
def calculateT0(fit_function_type, numCycle, threshold, max_iteration, filepath = None, v_t = None, mask = None):
    """
    Input:
    1. fit_function_type: 0 for linear, 1 for exponential

    2. numCycle, threshold, and max_iteration are settting parameters

    3. filepath: needs if is first entry

    4. v_t: needs if is reselected or switch fitting function

    5. mask: needs if is reselected


    How to assign the argument:
    1. first entry: filepath

    2. reselected: v_t, mask

    3. switch fitting function: v_t

    Output:
    return [status, T0, T0_SIGMA, v_t]

    status: 

    0 successful

    1 failed at fitting data from which the outliers are removed

    2 failed at fitting raw data
    
    """

    # initialize
    T0 = np.zeros(5)
    T0_SIGMA = np.zeros(5)
    status = 0

    # collect data if is first entry
    if filepath is not None:
        with open(filepath, 'r') as f:
            data = f.readlines()

        # find data starting line
        for i in reversed(range(len(data))):
            stl = i
            if len(data[i].split()) == 4:
                break
        stl -= (6*numCycle-2)

        # catch the data
        v_t = np.zeros((5, numCycle, 2))

        for i in range(numCycle):
            for j in range(5):
                v_t[j, i, 0] = float((data[stl + 6*i + j].split())[2])
                v_t[j, i, 1] = float((data[stl + 6*i + j].split())[3])

    fig, axs = plt.subplots(2, 3, figsize = (12,8))

    f = fit_func_list[fit_function_type]

    #  recognize the outlier first (use Ar 40) if first entry or switch the fitting function
    if mask is None:
        t = v_t[4, :, 1]
        v = v_t[4, :, 0]
        mask = np.zeros((5, numCycle))

        try:
            popt, _ = curve_fit(f, t, v, maxfev = max_iteration)
        except:
            # only possible to enter this line when switching fitting function
            # since it's always possible to fit the raw data with default fitting function (linear)
            status = 2
            return [status, None, None, None]

        baseline = threshold*np.std(np.abs(v - f(t, *popt))) # std of the error

        # autoselect the outlier
        for j in range(numCycle):
            if np.abs(v[j] - f(t[j], *popt)) > baseline:
                mask[:, j] = 1 # mark this cycle as outlier

    # go over Ar 36 to 40
    for i in range(5):
        # first linear regression 
        # fit whole data (no outlier is removed)
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        
        try:
            popt, _ = curve_fit(f, t, v, maxfev = max_iteration)

        except:
            # only possible to enter this line when switching fitting function
            # since it's always possible to fit the raw data with default fitting function (linear)
            status = 2
            return [status, None, None, None]

        T0[i] = f(0, *popt)
        T0_SIGMA[i] = np.std(np.abs(v - f(t, *popt))) # std of the error of first fit
 
        axs[i//3, i%3].plot(t, v, marker = 'o', label = "experiment data")
        axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line")
        axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")

        # second linear regression 
        # remove the outliers
        valid_indices = np.where(mask[i, :] == 0)[0]
        outlier_indices = np.where(mask[i, :] > 0)[0]

        t = v_t[i, valid_indices, 1]
        v = v_t[i, valid_indices, 0]

        try:
            popt, _ = curve_fit(f, t, v, maxfev = max_iteration)
            T0[i] = f(0, *popt)
            T0_SIGMA[i] = np.std(np.abs(v - f(t, *popt))) # std of the error of second fit
            axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line\n(exclude outliers)")
        except:
            status = 1

        axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
        axs[i//3, i%3].legend()
        axs[i//3, i%3].set_title("Ar {}\n{} = {} ".format(i+36, r'$T_{0}$', '{:0.5e}'.format(T0[i])))
    
    axs[1,2].axis('off')
    plt.tight_layout()
    plt.savefig(".work/LR.png", dpi = 200)

    return [status, T0, T0_SIGMA, None if filepath is None else v_t]



def getT0Statistics(filelist):
    result = np.zeros((len(filelist), 5))

    for i, filename in enumerate(filelist):
        with open(filename, 'r') as f:
            data = f.readlines()
        for j in range(5):
            result[i, j] = float(data[j+1].split(',')[1])

    # calculate statistics
    statistics = np.zeros((5, 2))

    for i in range(5):
        statistics[i, 0] = np.mean(result[:, i])
        statistics[i, 1] = np.std(result[:, i])

    # plot T0 distribution
    fig, axs = plt.subplots(1, 5, figsize = (12,4))
    for i in range(5):
        axs[i].plot(np.zeros(len(filelist)), result[:, i], marker = 'x', markersize = 10, linestyle = 'None')
        axs[i].errorbar(0, statistics[i, 0], yerr = statistics[i, 1], color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
        axs[i].set_aspect(7/axs[i].get_data_ratio())
        axs[i].axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
        axs[i].set_title("Ar {}".format(36+i))

    #plt.show()
    plt.savefig(".work/T0S.png", dpi = 200)

    return statistics


pair_indices = [[4, 0], [1, 3], [2, 0], [4, 2], [4, 3]]
#               40/36    37/39   38/36   40/38   40/39
def calculateMassRatio(mass_filename, background_filename):
    raw = np.zeros((5, 2))
    preline = np.zeros((5,2))

    with open(mass_filename, 'r') as f:
        data = f.readlines()
    for i in range(5):
        raw[i, 0] = float(data[i+1].split(',')[1]) # T0
        raw[i, 1] = float(data[i+1].split(',')[2]) # T0_SIGMA

    with open(background_filename, 'r') as f:
        data = f.readlines()
    for i in range(5):
        preline[i, 0] = float(data[i+1].split(',')[1]) # T0
        preline[i, 1] = float(data[i+1].split(',')[2]) # T0_SIGMA

    measurement = raw[:, 0] - preline[:, 0] # 36 37 38 39 40 (Measurement)
    measurement_std = minusSigma(raw[:, 1], preline[:, 1])

    ratio = np.zeros(5)
    ratio_std = np.zeros(5)
    for i in range(5):
        y, x = pair_indices[i][0], pair_indices[i][1]
        ratio[i] = measurement[y]/measurement[x]
        ratio_std[i] = ratioSigma(measurement[y], measurement_std[y], measurement[x], measurement_std[x])

    return [raw[:, 0], measurement, measurement_std, ratio, ratio_std]



def getAirRatioStatistics(filelist, background1, background2):
    '''
    background1: published Ar 40/36 air background
    background2: published Ar 38/36 air background
    '''
    ratios = np.zeros((2, len(filelist))) # [ratio pair, ratio value]

    for i, filename in enumerate(filelist):
        with open(filename, 'r') as f:
            data = f.readlines()
        ratios[0, i] = float(data[1].split(',')[1]) - background1 
        ratios[1, i] = float(data[3].split(',')[1]) - background2 

    # calculate statistics
    statistics = np.zeros((2, 2)) # [ratio pair, mean/std]
    for i in range(2):
        statistics[i, 0] = np.mean(ratios[i, :])
        statistics[i, 1] = np.std(ratios[i, :])

    # plot air ratio distribution
    fig, axs = plt.subplots(1, 2, figsize = (6,4))
    ratio_pair = ["Ar 40/36", "Ar 38/36"]
    for i in range(2):
        axs[i].plot(np.zeros(len(filelist)), ratios[i, :], marker = 'x', markersize = 10, linestyle = 'None')
        axs[i].errorbar(0, statistics[i, 0], yerr = statistics[i, 1], color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
        axs[i].set_aspect(7/axs[i].get_data_ratio())
        axs[i].axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
        axs[i].set_title(ratio_pair[i])

    #plt.show()
    plt.savefig(".work/ARS.png", dpi = 200)

    return statistics

def calcAge(measurement_filename, J, J_std, constants):
    # collect data
    data = np.zeros((5, 2))

    with open(measurement_filename, 'r') as f:
        tmp_data = f.readlines()

    for i in range(5):
        data[i, 0] = float(tmp_data[i+1].split(',')[2])
        data[i, 1] = float(tmp_data[i+1].split(',')[3])

    # Ar component calculation
    Ar_37_m = data[1, 0]
    Ar_37_m_std = data[1, 1]
    Ar_37_Ca = Ar_37_m
    Ar_37_Ca_std = Ar_37_m_std

    Ar_36_m = data[0, 0]
    Ar_36_m_std = data[0, 1]
    Ar_36_Ca = Ar_37_Ca * constants[1]
    Ar_36_Ca_std = Ar_37_Ca_std * constants[1]
    Ar_36_Air = Ar_36_m - Ar_36_Ca
    Ar_36_Air_std = minusSigma(Ar_36_m_std, Ar_36_Ca_std)

    Ar_39_m = data[3, 0]
    Ar_39_m_std = data[3, 1]
    Ar_39_Ca = Ar_37_Ca * constants[0]
    Ar_39_Ca_std = Ar_37_Ca_std * constants[0]
    Ar_39_K = Ar_39_m - Ar_39_Ca
    Ar_39_K_std = minusSigma(Ar_39_m_std, Ar_39_Ca_std)

    Ar_38_m = data[2, 0]
    Ar_38_m_std = data[2, 1]
    Ar_38_K = Ar_39_K * constants[3]
    Ar_38_K_std = Ar_39_K_std * constants[3]
    Ar_38_Air = Ar_38_m - Ar_38_K
    Ar_38_Air_std = minusSigma(Ar_38_m_std, Ar_38_K_std)

    Ar_40_m = data[4, 0]
    Ar_40_m_std = data[4, 1]
    Ar_40_air = Ar_36_Air * constants[5]
    Ar_40_air_std = Ar_36_Air_std * constants[5]
    Ar_40_K = Ar_39_K * constants[2]
    Ar_40_K_std = Ar_39_K_std * constants[2]
    Ar_40_radioactive = Ar_40_m - Ar_40_air - Ar_40_K
    Ar_40_radioactive_std = np.sqrt(Ar_40_m_std**2 + Ar_40_air_std**2 + Ar_40_K_std**2)
    Ar_40_radioactive_ratio = Ar_40_radioactive / data[4, 0]


    # ratio calculation
    Ar_39_K_40_r_ratio =  Ar_39_K / Ar_40_radioactive
    Ar_39_K_40_r_ratio_std = ratioSigma(Ar_39_K, Ar_39_K_std, Ar_40_radioactive, Ar_40_radioactive_std)
    Ar_36_Air_40_r_ratio = Ar_36_Air / Ar_40_radioactive
    Ar_36_Air_40_r_ratio_std = ratioSigma(Ar_36_Air, Ar_36_Air_std, Ar_40_radioactive, Ar_40_radioactive_std)
    Ar_39_K_36_Air = Ar_39_K / Ar_36_Air
    Ar_39_K_36_Air_std = ratioSigma(Ar_39_K, Ar_39_K_std, Ar_36_Air, Ar_36_Air_std)

    # Age calculation
    C1, C2, C3, C4 = constants[5], constants[1], constants[2], constants[0]
    G = Ar_40_m / Ar_39_m
    G_std = ratioSigma(Ar_40_m, Ar_40_m_std, Ar_39_m, Ar_39_m_std)
    B = Ar_36_m / Ar_39_m
    B_std = ratioSigma(Ar_36_m, Ar_36_m_std, Ar_39_m, Ar_39_m_std)
    D = Ar_37_m / Ar_39_m
    D_std = ratioSigma(Ar_37_m, Ar_37_m_std, Ar_39_m, Ar_39_m_std)
    F = Ar_40_radioactive / Ar_39_K
    F_std = np.sqrt(G_std**2 + (C1*B_std)**2 + ((C4*G - C1*C4*B + C1*C2)*D_std)**2)

    T = np.log(1 + J*F) / constants[7]
    T_std = np.sqrt((J**2 * F_std**2 + F**2 * J_std**2)/ ((constants[7]*(1+F*J))**2))

    return [Ar_36_m, Ar_36_m_std, Ar_36_Air, Ar_36_Air_std, Ar_36_Ca, Ar_36_Ca_std,
            Ar_37_m, Ar_37_m_std, Ar_37_Ca, Ar_37_Ca_std,
            Ar_38_m, Ar_38_m_std, Ar_38_Air, Ar_38_Air_std, Ar_38_K, Ar_38_K_std,
            Ar_39_m, Ar_39_m_std, Ar_39_K, Ar_39_K_std, Ar_39_Ca, Ar_39_Ca_std,
            Ar_40_m, Ar_40_m_std, Ar_40_radioactive, Ar_40_radioactive_std, Ar_40_air, Ar_40_air_std, Ar_40_K, Ar_40_K_std,
            Ar_39_K_40_r_ratio, Ar_39_K_40_r_ratio_std, Ar_36_Air_40_r_ratio, Ar_36_Air_40_r_ratio_std, Ar_39_K_36_Air, Ar_39_K_36_Air_std,
            F, F_std, G, G_std, B, B_std, D, D_std,
            J, J_std,
            T, T_std,
            Ar_40_radioactive_ratio, C1, C2, C3, C4
            ]
    


if __name__ == "__main__":
    print(calculateT0(1, filepath='./Data/AS20210429a'))
    #getT0Statistics(["./Data/AS20210429a.csv", "./Data/AS20210429b.csv", "./Data/AS20210429c.csv"])
    #print(getAirRatioStatistics(["./Data/ratio_a.csv", "./Data/ratio_b.csv", "./Data/ratio_c.csv"]))
    #print(calculateMassRatio("./Data/AS20210429a", "./Data/pb20210429a"))
    #print("test")