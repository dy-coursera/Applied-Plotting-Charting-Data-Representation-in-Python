# Use the following data for this assignment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as color

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])



def drawGraph(y):
    # Since we need 95% confidence interval, z-score = 1.96
    # error rate = (z-score * standard_deviation)/(sqrt(number of data))
    error_rate = (1.96 * df.T.std())/(np.sqrt(len(df.T)))
    mean_val = df.T.mean()

    plt.figure()
    plt.xticks(range(len(df.index)), df.index)
    plt.xlabel('Years')
    plt.title('Data collected through 1992 to 1995')
    plt.bar(range(len(df.index)), mean_val, yerr= error_rate)


    # create a line for y-axis value of interest (e.g. 42000)
    plt.axhline(y=y, color = 'orange', linestyle = '--')
    # And add it into a legend
    leg = plt.legend([y])
    leg.get_frame().set_edgecolor('white')


    # Now, we need to set the colormap
    colorlists = color.LinearSegmentedColormap.from_list("colorlists", ["b","w", "r"])

    # Let's compute the positive error rate and negative error rate 
    # error rate = mean +- ((1.96 * std_val)/(np.sqrt(n)))
    error_rate = error_rate.tolist()
    err = []
    for i in range(len(df.index)):
        pos = mean_val.iloc[i] + error_rate[i]
        neg = mean_val.iloc[i] - error_rate[i]
        r = (pos - y)/(pos - neg)
        if r>1:
            r =1
        err.append(r)
    # Let's make ScalarMappable which will choose color based on rates
    pick_color = cm.ScalarMappable(cmap=colorlists)
    pick_color.set_array([])
    # Let's update the bar with new colors
    plt.bar(range(len(df.index)), mean_val, yerr= error_rate, color = pick_color.to_rgba(err))
    # Create the colorbar with range 0~1 into 8 pieces
    plt.colorbar(colorpicks, boundaries = np.linspace(0,1,num =9))
    plt.show()
drawGraph(42000)
