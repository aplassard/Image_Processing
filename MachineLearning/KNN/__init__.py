#!/usr/bin/env python
from sklearn import neighbors

def buildKNN(labels,features):
    knn = neighbors.KNeighborsClassifier()
    knn.fit(features, labels)
    return knn

