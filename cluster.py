from tools import tools
#from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


def columnFloat(matrix, i, decimal):
    #return [round(float(row[i]),decimal) for row in matrix]
    retval=[]
    for row in matrix:
        try:
            retval.append(round(float(row[i]), decimal))
        except:
            print("-")
    return retval

def column(matrix, i):
    return [row[i] for row in matrix]

def histogram(data):
    cleandata=columnFloat(data, 4, 2)
    #mu, sigma = 100, 15
    mu, sigma = (np.mean(cleandata), np.std(cleandata))

    # the histogram of the data
    n, bins, patches = plt.hist(cleandata, bins=50, density=0, facecolor='green', alpha=0.75)
    #n, bins, patches = plt.hist([1,1,1,1,2,3,5,6,5,5,5,5,6,3,2,2,2,1], bins=50, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=10)

    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title("Rating Distribution")
    #plt.axis([0, 8, 0, 10])
    plt.grid(True)

    plt.show()


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

data = tools.read("../result.txt")
#recounted = Counter(column(data,1))
#print(recounted)


histogram(data)