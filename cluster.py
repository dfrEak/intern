from tools import tools
#from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def column(matrix, i):
    return [round(float(row[i]),2) for row in matrix]


data = tools.read("../result_avg_dinner.txt")
#recounted = Counter(column(data,1))
#print(recounted)


def histogram():
    mu, sigma = 100, 15

    # the histogram of the data
    n, bins, patches = plt.hist(column(data,1), bins=50, normed=0, facecolor='green', alpha=0.75)
    #n, bins, patches = plt.hist([1,1,1,1,2,3,5,6,5,5,5,5,6,3,2,2,2,1], bins=50, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title("Rating Distribution")
    #plt.axis([0, 8, 0, 10])
    plt.grid(True)

    plt.show()

histogram()