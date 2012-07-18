#!/usr/bin/env python
import numpy as np
import random
    
def normalizeVector(vector,m,s):
    for i in xrange(vector.shape[0]):
        vector[i]=(vector[i]-m[i])/s[i]
    return vector

def normalizearray(arr):
    m=[]
    s=[]
    for i in xrange(arr.shape[1]):
        v,a,b=getZScore(arr[:,i])
        for j in xrange(arr[:,i].shape[0]):
            arr[j,i]=v[j]
        m.append(a)
        s.append(b)
    return arr,m,s

def getZScore(vector):
    s=vector.std()
    m=vector.mean()
    if s>0:
        return (vector-m)/s,m,s
    else: return vector,m,1
    
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
                trainingfeatures.append(tempfeatures[j])
                traininglabels.append(templabels[j])
            else:
                testfeatures.append(tempfeatures[j])
                testlabels.append(templabels[j])
    traininglabels=np.array(traininglabels).astype(float)
    testlabels=np.array(testlabels).astype(float)
    return np.array(testfeatures).astype(float),testlabels,np.array(trainingfeatures).astype(float),traininglabels