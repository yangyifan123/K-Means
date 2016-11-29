from  numpy import *
import time
import matplotlib.pyplot as plt

def enDistance(victor1,victor2):
    return sqrt(sum(power(victor2-victor1,2)))

def createCentroids(dataSet,k):
    hang ,lie = dataSet.shape
    centroids = zeros((k,lie))
    for i in range(k):
        index = int(random.uniform(0,hang))
        centroids[i,:] = dataSet[index,:]
    return centroids

def kmeans(dataSet,k):
    hang = dataSet.shape[0]
    clusterAssment = mat(zeros((hang,2)))
    clusterChanged = True
    centroids = createCentroids(dataSet,k)

    while clusterChanged:
        clusterChanged = False
        for i in xrange(hang):
            minDist = 10000
            minIndex = 0
            for j in range(k):
                distance = enDistance(centroids[j,:],dataSet[i,:])
                if minDist>distance:
                    minDist = distance
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
                clusterAssment[i,:] = minIndex,pow(minDist,2)
        for j in range(k):
            pointInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j,:] = mean(pointInCluster,axis = 0)
            print nonzero(clusterAssment[:, 0].A == j)[0]
            print centroids[j,:]

        print "finished"
        return centroids ,  clusterAssment

def showCluster(dataSet, k, centroids, clusterAssment):
    numSamples, dim = dataSet.shape
    if dim != 2:
        print "Sorry! I can not draw because the dimension of your data is not 2!"
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print "Sorry! Your k is too large! please contact Zouxy"
        return 1

        # draw all samples
    for i in xrange(numSamples):
        markIndex = int(clusterAssment[i, 0])
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # draw the centroids
    for i in range(k):
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize=12)

    plt.show()



print "step 1: load data..."
dataSet = []
fileIn = open('testSet.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    lineArr2 = lineArr[0].strip().split('   ')
    dataSet.append([float(lineArr2[0].strip()), float(lineArr2[1].strip())])
print "step 2: clustering..."
dataSet = mat(dataSet)
k = 4
centroids, clusterAssment = kmeans(dataSet, k)

print "step 3: show the result..."
showCluster(dataSet, k, centroids, clusterAssment)
