#!/usr/bin/env python

import milk
import numpy as np
from pybrain.supervised.knn.lsh.nearoptimal import MultiDimHash

def basicrunSVM(traininglabels,trainingfeatures,testfeatures):
    classifier=milk.defaultclassifier()
    model = classifier.train(trainingfeatures,traininglabels)
    labels=[]
    for i in range(testfeatures.shape[0]):
        labels.append(model.apply(testfeatures[i]))
    return labels

def buildSVMmodel(traininglabels,trainingfeatures):
    classifier=milk.defaultclassifier()
    model = classifier.train(trainingfeatures,traininglabels)
    return model

def normalizearray(arr):
    for i in xrange(arr.shape[1]):
        v=getZScore(arr[:,i])
        for j in xrange(arr[:,i].shape[0]):
            arr[j,i]=v[j]
    return arr

def naivenormalizevector(vector):
    m = float(vector.max())
    if m>0:
        for i in xrange(vector.shape[0]):
            vector[i]/=m
    return vector

def getZScore(vector):
    s=vector.std()
    print s
    if s>0:
        m=vector.mean()
        return (vector-m)/s
    else: return vector
    
def buildKNN(labels,features):
    knnmodel=MultiDimHash.__init__(features.shape[1])
    for i in xrange(features.shape[0]):
        knnmodel.insert(features[i,:],labels(i))
    return knnmodel

def getK(KNN,vector,n=5):
    return KNN.knn(vector,n)