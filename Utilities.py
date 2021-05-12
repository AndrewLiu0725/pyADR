import numpy as np 
import matplotlib.pyplot as plt

DEBUG = 1

def calculateT0(filepath, action_type, mask):
    """
    action_type: 0 for reference, 1 for reselect
    """

    # collect data
    f = open(filepath)
    data = f.readlines()
    numCycle = int((data[0].split())[0])

    v_t = np.zeros((5, numCycle, 2))
    T0 = np.zeros(5)

    for i in range(numCycle):
        for j in range(5):
            v_t[j, i, 0] = (data[2 + 6*i + j].split())[2]
            v_t[j, i, 1] = (data[2 + 6*i + j].split())[3]

    fig, axs = plt.subplots(2, 3, figsize = (12,8))

    # if is reference, recognize the outlier first (use Ar 40)
    if not action_type:
        t = v_t[4, :, 1]
        v = v_t[4, :, 0]
        mask = np.zeros(numCycle)
        linear_model = np.polyfit(t, v, 1)
        linear_model_fn = np.poly1d(linear_model)
        baseline = 2.5*np.std(np.abs(v - linear_model_fn(t))) # std of the error
        for j in range(numCycle):
            if np.abs(v[j] - linear_model_fn(t[j])) > baseline:
                mask[j] = 1 # mark this point as outlier

    # go over Ar 36 to 40
    for i in range(5):
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        
        # first linear regression 
        linear_model = np.polyfit(t, v, 1)
        linear_model_fn = np.poly1d(linear_model)
        T0[i] = linear_model[1]
 
        axs[i//3, i%3].plot(t, v, marker = 'o', label = "experiment data")
        axs[i//3, i%3].plot(t, linear_model_fn(t), linestyle = '--', label = "fitted line")
        axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")

        # remove the outliers
        if action_type:
            valid_indices = np.where(mask[i, :] == 0)[0]
            outlier_indices = np.where(mask[i, :] > 0)[0]
        else:
            valid_indices = np.where(mask == 0)[0]
            outlier_indices = np.where(mask > 0)[0]

        t = v_t[i, valid_indices, 1]
        v = v_t[i, valid_indices, 0]

        if len(valid_indices) > 1:
            # second linear regression 
            linear_model = np.polyfit(t, v, 1)
            linear_model_fn = np.poly1d(linear_model)
            T0[i] = linear_model[1]

            axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
            axs[i//3, i%3].plot(t, linear_model_fn(t), linestyle = '--', label = "fitted line\n(exclude outliers)")
            axs[i//3, i%3].legend()
            axs[i//3, i%3].set_title("Ar {}\n{} = {} ".format(i+36, r'$T_{0}$', T0[i]))

        else:
            axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
            axs[i//3, i%3].legend()
            axs[i//3, i%3].set_title("Ar {}\n{} = {} ".format(i+36, r'$T_{0}$', T0[i]))
    
    axs[1,2].axis('off')
    plt.tight_layout()
    #plt.show()
    plt.savefig(".work/LR.png", dpi = 200)

    return T0



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
    T0 = np.zeros((2, 5))

    for i in range(2):
        f = open(mass_filename if i == 0 else background_filename, 'r')
        data = f.readlines()
        for j in range(5):
            T0[i, j] = float(data[j+1].split(',')[1])
        f.close()

    result = T0[0, :] - T0[1, :] # 36 37 38 39 40

    ratio = np.zeros(5)
    ratio[0] = result[4]/result[0] # 40/36
    ratio[1] = result[1]/result[3] # 37/39
    ratio[2] = result[0]/result[2] # 36/38
    ratio[3] = result[4]/result[2] # 40/38
    ratio[4] = result[4]/result[3] # 40/39

    return [result, ratio]

def getAirRatioStatistics(filelist):
    ratios = np.zeros(len(filelist))

    for i, filename in enumerate(filelist):
        f = open(filename, 'r')
        data = f.readlines()
        ratios[i] = float(data[5].split(',')[3])
        f.close()

    mean, std = np.mean(ratios), np.std(ratios)

    # plot
    fig, ax = plt.subplots(1, 1, figsize = (3,4))
    ax.plot(np.zeros(len(filelist)), ratios, marker = 'x', markersize = 10, linestyle = 'None')
    ax.errorbar(0, mean, yerr = std, color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
    #print(ax.get_data_ratio())
    ax.set_aspect(7/ax.get_data_ratio())
    ax.axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
    ax.set_title("Air Ratio Statistics")

    #plt.show()
    plt.savefig(".work/ARS.png", dpi = 200)

    return [mean, std]


if __name__ == "__main__":
    #getT0Statistics(["./Data/AS20210429a.csv", "./Data/AS20210429b.csv", "./Data/AS20210429c.csv"])
    print(getAirRatioStatistics(["./Data/ratio_a.csv", "./Data/ratio_b.csv", "./Data/ratio_c.csv"]))
    #print(calculateMassRatio("./Data/AS20210429a", "./Data/pb20210429a"))
