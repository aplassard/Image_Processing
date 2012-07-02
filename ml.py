#!/usr/bin/env python

import milk
import numpy as np
from pybrain.supervised.knn.lsh.nearoptimal import MultiDimHash
from pybrain.supervised.knn.lsh.minhash import MinHash
from sklearn import neighbors


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
    if s>0:
        m=vector.mean()
        return (vector-m)/s
    else: return vector
    
def buildKNN(labels,features):
    knn = neighbors.KNeighborsClassifier()
    knn.fit(features, labels)
    return knn

def getK(KNN,vector,n=5):
    return KNN.predict(vector)
    
    
def buildLearners(labels,features):
    d={}
    n=0
    for i in xrange(len(labels)):
        val=d.get(labels[i])
        if val:
            labels[i]=val
        else:
            d[labels[i]]=n
            n+=1
            labels[i]=val
    KNearest=buildKNN(labels,features)
    models={}
    models[KNN]=KNearest
    models[Neural]=buildNeural(labels,features)
    models[SVM]=buildSVM(labels,features)
    return models,d

