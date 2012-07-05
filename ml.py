#!/usr/bin/env python

import numpy as np
from sklearn import svm, datasets,neighbors
from sklearn.utils import shuffle
from common import *
from pybrain.datasets import supervised
import random
from sklearn.metrics import roc_curve,auc
import sys

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
    
def buildSVM(labels=None,features=None,traininglabels=None,trainingfeatures=None,testlabels=None,testfeatures=None):
    if labels and features:
        traininglabels=labels
        testlabels=labels
        trainingfeatures=features
        testfeatures=features
    elif traininglabels.any() and trainingfeatures.any() and testlabels.any() and testfeatures.any():
        pass
    else:
        print "Incorrect Usage!  Needs to have features and labels or traininfeatures,traininglabels,testfeatures, and testlabels!"
        return
    percent=0
    model=None
    params=None
    testmodel = svm.LinearSVC(C=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=0.1)'''
    testmodel = svm.LinearSVC(C=1.0)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=1.0)'''
    testmodel = svm.LinearSVC(C=5)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=5)'''
    testmodel = svm.LinearSVC(C=10)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=10)'''
    testmodel = svm.LinearSVC(C=20)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=20)'''
    testmodel = svm.LinearSVC(C=30)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=30)'''
    testmodel = svm.LinearSVC(C=40)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=40)'''
    testmodel = svm.SVC(C=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1)'''
    testmodel = svm.LinearSVC(C=1.0)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0)'''
    testmodel = svm.SVC(C=5)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5)'''
    testmodel = svm.SVC(C=10)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10)'''
    testmodel = svm.SVC(C=20)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20)'''
    testmodel = svm.SVC(C=30)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30)'''
    testmodel = svm.SVC(C=40)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40)'''
    testmodel = svm.SVC(C=0.1,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.0001)'''
    testmodel = svm.SVC(C=1.0,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.0001)'''
    testmodel = svm.SVC(C=5,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.0001)'''
    testmodel = svm.SVC(C=10,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.0001)'''
    testmodel = svm.SVC(C=20,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.0001)'''
    testmodel = svm.SVC(C=30,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.0001)'''
    testmodel = svm.SVC(C=40,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.0001)'''
    testmodel = svm.SVC(C=0.1,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.001)'''
    testmodel = svm.SVC(C=1.0,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.001)'''
    testmodel = svm.SVC(C=5,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.001)'''
    testmodel = svm.SVC(C=10,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.001)'''
    testmodel = svm.SVC(C=20,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.001)'''
    testmodel = svm.SVC(C=30,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.001)'''
    testmodel = svm.SVC(C=40,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.001)'''
    testmodel = svm.SVC(C=0.1,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.01)'''
    testmodel = svm.SVC(C=1.0,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.01)'''
    testmodel = svm.SVC(C=5,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.01)'''
    testmodel = svm.SVC(C=10,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.01)'''
    testmodel = svm.SVC(C=20,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.01)'''
    testmodel = svm.SVC(C=30,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.01)'''
    testmodel = svm.SVC(C=40,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.01)'''
        
    testmodel = svm.SVC(C=0.1,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.1)'''
    testmodel = svm.SVC(C=1.0,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.1)'''
    testmodel = svm.SVC(C=5,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.1)'''
    testmodel = svm.SVC(C=10,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.1)'''
    testmodel = svm.SVC(C=20,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.1)'''
    testmodel = svm.SVC(C=30,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.1)'''
    testmodel = svm.SVC(C=40,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.1)'''
    
    testmodel = svm.SVC(C=0.1,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,kernel='linear')'''
    testmodel = svm.SVC(C=1.0,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,kernel='linear')'''
    testmodel = svm.SVC(C=5,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,kernel='linear')'''
    testmodel = svm.SVC(C=10,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,kernel='linear')'''
    testmodel = svm.SVC(C=20,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,kernel='linear')'''
    testmodel = svm.SVC(C=30,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,kernel='linear')'''
    testmodel = svm.SVC(C=40,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)
    print p*100,'%'
    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,kernel='linear')'''
    print '\nThe best model had ' + str(percent*100) + '% success and used the parameters:\n' + params+'\n'
    return model

def calculateSVMerror(model,testfeatures,testlabels):
    n=0
    for i in xrange(testfeatures.shape[0]):
        a=model.predict(testfeatures[i,:])[0]
        if a==testlabels[i]:
            n+=1
    return float(n)/testfeatures.shape[0]

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
                trainingfeatures.append(tempfeatures[j])
                traininglabels.append(templabels[j])
            else:
                testfeatures.append(tempfeatures[j])
                testlabels.append(templabels[j])
    traininglabels=np.array(traininglabels).astype(float)
    testlabels=np.array(testlabels).astype(float)
    return np.array(testfeatures).astype(float),testlabels,np.array(trainingfeatures).astype(float),traininglabels

def test(path):
    f = open(path,'r')
    labels=[]
    features=[]
    for line in f:
        line = line.strip().split(tab)
        labels.append(line[0])
        features.append(line[1:])
    features=np.array(features).astype(float)
    d={}
    n=0
    for i in xrange(len(labels)):
        val=d.get(labels[i])
        if not val:
            val = n
            d[labels[i]]=n
            n+=1
        labels[i]=val
    testfeatures,testlabels,trainingfeatures,traininglabels=splitTrainingTesting(features,labels)
    ntestfeatures,m,s=normalizearray(testfeatures)
    ntrainingfeatures=normalizearray(trainingfeatures)
    SVMmodel=buildSVM(traininglabels=traininglabels,trainingfeatures=ntrainingfeatures,testlabels=testlabels,testfeatures=ntestfeatures)
    KNNmodel=buildKNN(traininglabels,trainingfeatures)
    knncorrect=0
    svmcorrect=0
    bothwrong=0
    for i in xrange(traininglabels.shape[0]):
        a=SVMmodel.predict(ntrainingfeatures[i,:])
        b=getK(KNNmodel,trainingfeatures[i,:])
        a=int(a[0])
        b=int(b[0])
        l=int(traininglabels[i])
        if a==l:
            svmcorrect+=1
        if b==l:
            knncorrect+=1
        if a!=l and b!=l:
            bothwrong+=1
            print "flag",
        if a!=l or b !=l:
            print a,b,l
    print "KNN got",knncorrect*100/traininglabels.shape[0],"% correct."
    print "SVM got",svmcorrect*100/traininglabels.shape[0],"% correct."
    print "There were",bothwrong,"cases where neither model was correct."
    print "This accounted for",bothwrong*100/testlabels.shape[0],"% of the testing data."
    
if __name__ == '__main__':
    test(sys.argv[1])