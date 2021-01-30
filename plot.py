import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def main():
    f = open(("data_" + str(10) + "_shuffle.txt"), "r")
    lines = f.readlines()
    data = []

    count = 0
    for line in lines:
        if (count > 999): #count = 1000 is the average time
            break
        count += 1
        string = line.split(" ")
        num = float((string[0]))
        data.append(num)
    
    #gen graph
    x = data

    plt.hist(x, weights=np.ones(len(x)) / len(x), bins=20, color="red")
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    plt.show()

main()
