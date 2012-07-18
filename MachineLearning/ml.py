#!/usr/bin/env python
import numpy as np
from common import *
from mlFunctions import *
from SVM import buildSVM
from KNN import buildKNN

class ml(object):
    '''
    Machine Learning Class
    '''
    def __init__(self,trainingfeatures,traininglabels):
        '''
        Input:
            trainingfeatures: numpy array of features with one row per sample
            traininglabels: list of character features with each entry corresping
                            to its corresponding entry in trainingfeatures
        Output:
            object of type ml
            
        Initializes class of type ml.  Builds multiple machine learning modules.
        '''
        self.trainingfeatures,self.means,self.stds=normalizearray(trainingfeatures)
        self.labeldict={}
        self.intdict={}
        self.traininglabels = np.zeros_like(traininglabels,dtype=int)
        n=0
        for i in xrange(len(traininglabels)):
            val= self.labeldict.get(traininglabels[i])
            if val==None:
                val = n
                self.labeldict[traininglabels[i]]=n
                self.intdict[n]=traininglabels[i]
                n+=1
            self.traininglabels[i]=val
        testfeatures,testlabels,tfeatures,tlabels = splitTrainingTesting(self.trainingfeatures,self.traininglabels)
        self.svm = buildSVM(tlabels,tfeatures,testlabels,testfeatures)
        self.knn = buildKNN(self.traininglabels,self.trainingfeatures)
        
    def getKNNClass(self,vector):
        return int(self.knn.predict(vector)[0])
        
    def getSVMClass(self,vector):
        return int(self.svm.predict(vector)[0])
        
    def getLabels(self,vector):
        labels = []
        nvector = (vector-self.means)/self.stds
#        labels.append(self.getKNNClass(nvector))
        labels.append(self.getSVMClass(nvector))
        return labels
    
    
