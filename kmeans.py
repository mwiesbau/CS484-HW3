import random
from sklearn.neighbors import DistanceMetric
from scipy.spatial import distance
import numpy as np
import pandas as pd
'''
class Centroid():
    
    dimensions = {}
    
    def __init__(self, dimensions):
        for i in range(0, dimensions):
            self.dimensions[i] = 0
            
    def centroidDistance(self, centroid):
'''


class K_Means():
    centroids = {}

    def __init__(self, dataFrame, clusterLabels):
        self.dataFrame = dataFrame
        self.clusterLabels = clusterLabels
        self.__computeCentroids__() # INITIALIZE CENTROIDS

    def __computeCentroids__(self):
        for label in self.clusterLabels:
            filtered = self.dataFrame.loc[self.dataFrame['cluster'] == label]
            self.centroids[label] = filtered.mean()

    def __centroidsAsDataFrame__(self):
        centroids = pd.DataFrame.from_dict(self.centroids, orient='index')

        return centroids.loc[:, 'sepal_length':'petal_width']



    def distanceBetweenRows(self, row1, row2):
        return None

    def findClusters(self):
        reassignedClusterPoints = 0

        v = np.cov(self.dataFrame.iloc[:, :-1])
        #print(v)
        #print(self.__centroidsAsDataFrame__())
        #distance_metric = DistanceMetric.get_metric('euclidean')
        #dist = distance_metric.pairwise(self.dataFrame.loc[:, :'petal_width'], self.__centroidsAsDataFrame__())
        #print(dist)
        for index, row in self.dataFrame.iterrows():
            currentCluster = row['cluster']

            nearestCluster = {'name': "",
                              'distance': None}


            for cluster in self.clusterLabels:
                distance_metric = DistanceMetric.get_metric('chebyshev')
                dist = distance_metric.pairwise([row.iloc[:-1]], [self.centroids[cluster]])
                #print(dist)
                #dist = (row[0] - self.centroids[cluster][0])**2 +\
                #(row[1] - self.centroids[cluster][1])**2 +\
                #(row[2] - self.centroids[cluster][2])**2 +\
                #(row[3] - self.centroids[cluster][3])**2

                if not nearestCluster['distance'] or dist < nearestCluster['distance']:
                    nearestCluster['name'] = cluster
                    nearestCluster['distance'] = dist

            self.dataFrame.at[index, 'cluster'] = nearestCluster['name']

            if currentCluster != nearestCluster['name']:
                reassignedClusterPoints += 1
                #print("cluster assignment for row {} changed from {} to {}".format(index, currentCluster, nearestCluster['name']))

        self.__computeCentroids__() # UPDATE CENTROIDS AFTER REASSIGNMENT OF CLUSTER LABELS
        return reassignedClusterPoints


    def getDataFrame(self):
        return self.dataFrame
