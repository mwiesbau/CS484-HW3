

import seaborn as sns
import pandas as pd
import random
from kmeans import K_Means
from sklearn.neighbors import DistanceMetric





def loadData(clusterLabels):
    '''
    LOADS THE DATA AND RANDOMLY ASSIGNS CLUSTER LABELS
    :return:
    '''
    data = pd.read_csv("../1538576435_7139187_iris_new.data", delim_whitespace=True)

    # RANDOMLY ASSIGN CLUSTER LABELS
    random_data = []
    for i in range(0,150):
        random_data.append(random.choice(clusterLabels))

    rand = pd.DataFrame({'cluster': random_data})
    data = data.join(rand)
    return data


def saveToFile(dataFrame):

    file = open('output.txt', 'w')

    for index, row in dataFrame.iterrows():

        if row['cluster'] == 'one':
           file.write("1\n")
        elif row['cluster'] == 'two':
            file.write("2\n")
        elif row['cluster'] == 'three':
            file.write("3\n")
    file.close()

def makeScatterPlot(data, iteration=None):
    sns.set_style(style='ticks')

    sns_plot = sns.pairplot(data, hue='cluster')

    if not iteration:
        sns_plot.savefig("output.png")
    else:
        sns_plot.savefig("output_{}.png".format(iteration))


if __name__ == "__main__":
    clusterLabels = ["one", "two", "three"]
    data = loadData(clusterLabels)



    makeScatterPlot(data)

    kMeans = K_Means(data, clusterLabels)
    iteration = 1
    i = 1
    while i > 0:
        i = kMeans.findClusters()
        data = kMeans.getDataFrame()
        makeScatterPlot(data)
        print("=" * 100)
        print("Iteration {}, {} reassigned".format(iteration, i))
        iteration += 1

    saveToFile(data)
