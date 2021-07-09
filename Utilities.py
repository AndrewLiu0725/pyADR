import numpy as np 
import matplotlib.pyplot as plt
from numpy.lib.function_base import diff
from scipy.optimize import curve_fit
from scipy.sparse import base

DEBUG = 1

# T0 regression fitting functions
# ===============================================================================
def linear(x, a, b):
    return a*x + b

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

def asymptotic(x, a, b, n):
    return a * x ** n  / (x ** n + b)

fit_func_list = [linear, quadratic]

# functions for button
# ===============================================================================
def calculateT0(filepath, action_type, mask, fit_function_type):
    """
    action_type: 0 for reference (first entry or switch fitting function), 1 for reselect
    fit_function_type: 0 for linear, 1 for exponential
    """

    # collect data
    f = open(filepath)
    data = f.readlines()
    numCycle = int((data[0].split())[0])

    v_t = np.zeros((5, numCycle, 2))
    T0 = np.zeros(5)
    T0_SIGMA = np.zeros(5)

    for i in range(numCycle):
        for j in range(5):
            v_t[j, i, 0] = (data[2 + 6*i + j].split())[2]
            v_t[j, i, 1] = (data[2 + 6*i + j].split())[3]

    fig, axs = plt.subplots(2, 3, figsize = (12,8))

    f = fit_func_list[fit_function_type]

    # if is reference, recognize the outlier first (use Ar 40)
    if not action_type:
        t = v_t[4, :, 1]
        v = v_t[4, :, 0]
        mask = np.zeros(numCycle)
        try:
            popt, pcov = curve_fit(f, t, v)
        except:
            return None
        baseline = 2.5*np.std(np.abs(v - f(t, *popt))) # std of the error
        for j in range(numCycle):
            if np.abs(v[j] - f(t[j], *popt)) > baseline:
                mask[j] = 1 # mark this point as outlier

    # go over Ar 36 to 40
    for i in range(5):
        # first linear regression 
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        
        popt, pcov = curve_fit(f, t, v)
        T0[i] = f(0, *popt)
        T0_SIGMA[i] = np.std(np.abs(v - f(t, *popt))) # std of the error of first fit
 
        axs[i//3, i%3].plot(t, v, marker = 'o', label = "experiment data")
        # fit whole data (no outlier is removed)
        axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line")
        axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")

        # remove the outliers
        if action_type:
            valid_indices = np.where(mask[i, :] == 0)[0]
            outlier_indices = np.where(mask[i, :] > 0)[0]
        else:
            valid_indices = np.where(mask == 0)[0]
            outlier_indices = np.where(mask > 0)[0]

        # second linear regression 
        t = v_t[i, valid_indices, 1]
        v = v_t[i, valid_indices, 0]

        if len(valid_indices) > 1: # 1 bucause one line needs at least 2 points
            try:
                popt, pcov = curve_fit(f, t, v)
                T0[i] = f(0, *popt)
                T0_SIGMA[i] = np.std(np.abs(v - f(t, *popt))) # std of the error of second fit
                axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line\n(exclude outliers)")
            except:
                return None

        axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
        axs[i//3, i%3].legend()
        axs[i//3, i%3].set_title("Ar {}\n{} = {} ".format(i+36, r'$T_{0}$', T0[i]))
    
    axs[1,2].axis('off')
    plt.tight_layout()
    #plt.show()
    plt.savefig(".work/LR.png", dpi = 200)

    return [T0, T0_SIGMA]



def getT0Statistics(filelist):
    result = np.zeros((len(filelist), 5))

    for i, filename in enumerate(filelist):
        f = open(filename, 'r')
        data = f.readlines()
        for j in range(5):
            result[i, j] = float(data[j+1].split(',')[1])
        f.close()

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



def calculateMassRatio(mass_filename, background_filename):
    T0 = np.zeros((2, 2, 5))

    for i in range(2):
        f = open(mass_filename if i == 0 else background_filename, 'r')
        data = f.readlines()
        for j in range(5):
            T0[i, 0, j] = float(data[j+1].split(',')[1]) # T0
            T0[i, 1, j] = float(data[j+1].split(',')[2]) # T0_SIGMA
        f.close()

    result = T0[0, 0, :] - T0[1, 0, :] # 36 37 38 39 40
    diff_std = np.sqrt(T0[0, 1, :]**2 + T0[1, 1, :]**2)

    ratio = np.zeros(5)
    ratio[0] = result[4]/result[0] # 40/36
    ratio[1] = result[1]/result[3] # 37/39
    ratio[2] = result[2]/result[0] # 38/36
    ratio[3] = result[4]/result[2] # 40/38
    ratio[4] = result[4]/result[3] # 40/39

    return [T0[0, 0, :], result, diff_std, ratio]

def getAirRatioStatistics(filelist):
    ratios = np.zeros((2, len(filelist))) # [ratio pair, ratio value]

    for i, filename in enumerate(filelist):
        f = open(filename, 'r')
        data = f.readlines()
        ratios[0, i] = float(data[1].split(',')[5]) - 298.56 # published Ar 40/36 air background
        ratios[1, i] = float(data[3].split(',')[5]) - 0.18850 # published Ar 38/36 air background
        f.close()

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


if __name__ == "__main__":
    #getT0Statistics(["./Data/AS20210429a.csv", "./Data/AS20210429b.csv", "./Data/AS20210429c.csv"])
    print(getAirRatioStatistics(["./Data/ratio_a.csv", "./Data/ratio_b.csv", "./Data/ratio_c.csv"]))
    #print(calculateMassRatio("./Data/AS20210429a", "./Data/pb20210429a"))
    #print("test")