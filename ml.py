#!/usr/bin/env python

import milk
import numpy as np
from sklearn import neighbors,svm
from common import *
from pybrain.datasets import supervised
import random

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
    m=[]
    s=[]
    for i in xrange(arr.shape[1]):
        v,a,b=getZScore(arr[:,i])
        for j in xrange(arr[:,i].shape[0]):
            arr[j,i]=v[j]
        m.append(b)
        s.append(a)
    return arr,m,s

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
        return (vector-m)/s,s,m
    else: return vector,s,m
    
def buildKNN(labels,features):
    knn = neighbors.KNeighborsClassifier()
    knn.fit(features, labels)
    return knn

def getK(KNN,vector,n=5):
    return KNN.predict(vector)
    
def buildSVM(labels,features):
    pass

def buildNeural(labels,features):
    pass
    
    
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
    models={}
    models[KNN]=buildKNN(labels,features)
    models[Neural]=buildNeural(labels,features)
    models[SVM]=buildSVM(labels,features)
    return models,d

def getZ(vector,means,stds):
    for i in xrange(len(vector)):
        vector[i]=(vector[i]-means[i])/stds[i]
    return vector


def splitTrainingTesting(arr,labels,percent=0.7):
    l=set(labels)
    l=list(l)
    traininglabels=[]
    testlabels=[]
    trainingfeatures=[]
    testfeatures=[]
    for i in xrange(len(l)):
        la=l[i]
        n=0
        templabels=[]
        tempfeatures=[]
        for j in xrange(len(labels)):
            if labels[j]==la:
                templabels.append(la)
                tempfeatures.append(list(arr[j,:]))
        g=random.sample(range(len(templabels)),int(percent*float(len(templabels))))
        for j in range(len(templabels)):
            if g.count(j)>0:
                trainingfeatures.append(tempfeatures[i])
                traininglabels.append(templabels[i])
            else:
                testfeatures.append(tempfeatures[i])
                testlabels.append(templabels[i])
    return np.array(testfeatures),testlabels,np.array(trainingfeatures),traininglabels
