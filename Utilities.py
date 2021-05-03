import numpy as np 
import matplotlib.pyplot as plt


def calculateT0(filepath, plot):
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

    if plot:
        fig, axs = plt.subplots(2, 3, figsize = (12,8))

    outlier_count = np.zeros(numCycle)

    # go over Ar 36 to 40
    for i in range(5):
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        
        # linear regression 
        linear_model = np.polyfit(t, v, 1)
        linear_model_fn = np.poly1d(linear_model)

        # recognize the outliers
        baseline = np.std(np.abs(v - linear_model_fn(t))) # std of the error
        for j in range(numCycle):
            if np.abs(v[j] - linear_model_fn(t[j])) > baseline:
                outlier_count[j] += 1

        if plot:
            axs[i//3, i%3].plot(t, v, marker = 'o', label = "experiment data")
            axs[i//3, i%3].plot(t, linear_model_fn(t), linestyle = '--', label = "fitted line")
            axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")
            
    # remove outlier
    valid_indices = np.where(outlier_count < 2.5)[0]
    outlier_indices = np.where(outlier_count > 2.5)[0]

    for i in range(5):
        t = v_t[i, valid_indices, 1]
        v = v_t[i, valid_indices, 0]
        
        if len(valid_indices) > 1:
            # linear regression 
            linear_model = np.polyfit(t, v, 1)
            linear_model_fn = np.poly1d(linear_model)
            T0[i] = linear_model[1]

            if plot:
                axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                axs[i//3, i%3].plot(t, linear_model_fn(t), linestyle = '--', label = "fitted line\n(exclude outliers)")
                axs[i//3, i%3].legend()
                axs[i//3, i%3].set_title("Ar {}\n{} = {} ".format(i+36, r'$T_{0}$', linear_model[1]))

        else:
            if plot:
                axs[i//3, i%3].plot(v_t[i, outlier_indices, 1], v_t[i, outlier_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                axs[i//3, i%3].legend()
                axs[i//3, i%3].set_title("Ar {}".format(i+36))



    if plot:
        axs[1,2].axis('off')
        plt.tight_layout()
        #plt.show()
        plt.savefig(".work/LR.png", dpi = 200)

    return T0


def getT0Statistics(filelist):
    result = np.zeros((len(filelist), 5))

    for i, filename in enumerate(filelist):
        result[i, :] = calculateT0(filename, 0)

    statistics = np.zeros((5, 2))

    for i in range(5):
        statistics[i, 0] = np.mean(result[:, i])
        statistics[i, 1] = np.std(result[:, i])

    return statistics


def calculateMassRatio(mass, background):
    result = calculateT0(mass, 0) - calculateT0(background, 0) # 36 37 38 39 40

    ratio = np.zeros(5)
    ratio[0] = result[4]/result[0] # 40/36
    ratio[1] = result[1]/result[3] # 37/39
    ratio[2] = result[0]/result[2] # 36/38
    ratio[3] = result[4]/result[2] # 40/38
    ratio[4] = result[4]/result[3] # 40/39

    return ratio


if __name__ == "__main__":
    print(calculateT0("./Data/AS20210429a", 1))
    #print(calculateMassRatio("./Data/AS20210429a", "./Data/pb20210429a"))
