#ref:
# https://datatofish.com/k-means-clustering-python/
# https://blog.cambridgespark.com/how-to-determine-the-optimal-number-of-clusters-for-k-means-clustering-14f27070048f

from tools import tools
#from collections import Counter
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from sklearn.cluster import KMeans
from config import config
from stringtable import stringTable

def columnFloat(matrix, i, decimal):
    retval=[]
    for row in matrix:
        try:
            retval.append(round(float(row[i]), decimal))
        except:
            print("-")
    return retval

def histogram(data, arrayNum, title, xLabel, yLabel):
    cleandata=columnFloat(data, arrayNum, 2)
    #mu, sigma = 100, 15
    mu, sigma = (np.mean(cleandata), np.std(cleandata))

    # the histogram of the data
    n, bins, patches = plt.hist(cleandata, bins=50, density=0, facecolor='green', alpha=0.75)
    #n, bins, patches = plt.hist([1,1,1,1,2,3,5,6,5,5,5,5,6,3,2,2,2,1], bins=50, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf( bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    #plt.axis([0, 8, 0, 10])
    plt.grid(True)

    plt.show()

def kmean(data, ncluster):
    #df = DataFrame(data,columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n'])
    #df = DataFrame(data,columns=['a','b','c','d','e'])
    df = DataFrame(data)
    #print(df)

    kmeans = KMeans(n_clusters=ncluster).fit(df)
    centroids = kmeans.cluster_centers_
    print("result:")
    print(kmeans.labels_)
    print("centroids:")
    print(centroids)

    #plt.scatter(df['a'], df['b'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    #plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    #plt.show()

def kmean_clusters(data):
    #df = DataFrame(data,columns=['a','b','c','d','e'])
    #df = DataFrame(data,columns=['a','b','c','d','e','f','g'])
    df = DataFrame(data)
    print(df)
    Sum_of_squared_distances = []
    K = range(1, 15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(data)
        Sum_of_squared_distances.append(km.inertia_)

    plt.plot(K, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

#data = tools.read(str(config.parent / "dinner_persen.txt"))
#subdata = {'x': tools.column(data,10),
#               'y': tools.column(data, 11)}

#temp = {'x': [25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
#        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
#       }
#recounted = Counter(column(data,1))
#print(recounted)


#histogram(data, stringTable.RESULT_RATING, "Rating Distribution", "Rating", "Count")
#histogram(data, stringTable.RESULT_COMMENT, "Comment Count Distribution", "Comment Count", "Count")

#kmean_clusters(data)
print("##################################################################################################################")
print("lunch:")
lunch = tools.read(str(config.parent / "lunch_percent.txt"))
#kmean_clusters(lunch)
kmean(lunch,3)
print("##################################################################################################################")
print("dinner:")
dinner = tools.read(str(config.parent / "dinner_percent.txt"))
#kmean_clusters(dinner)
kmean(dinner,6)