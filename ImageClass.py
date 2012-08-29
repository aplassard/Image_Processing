#!/usr/bin/env python
from common import *
import numpy as np
from scipy.stats import scoreatpercentile
from MachineLearning.mlFunctions import normalizearray

class ImageClass(object):
    def __init__(self):
        self.singlelabelobjects = {}
        self.labels = set()
    
    def addObject(self,key,vector):
        singlelabelobject = SingleLabel(key,vector)
        self.singlelabelobjects[key]=singlelabelobject
        self.labels.add(key)
        
    def addVector(self,key,vector):
        if key in self.labels:
             a = self.singlelabelobjects[key]
             a.addFeatureVector(vector)
             self.singlelabelobjects[key]=a
        else:
            print 'Adding key:',key
            self.addObject(key,vector)
            
    def getPercentiles(self):
        v=[]
        n=[]
        l=[]
        for key in self.singlelabelobjects.keys():
            a = self.singlelabelobjects[key].getPercentileVector()
            v.append(a)
            l.append(key)
            n.append(self.singlelabelobjects[key].n)
        return v,l,n
    
    def toFile(self,oname,normalized=True):
        v,l,n = self.getPercentiles()
        o = open(oname+'.txt','w')
        print
        print 'Writing to file: ' + oname+'.txt'
        for i in xrange(len(l)):
            output = str(l[i])+tab+str(n[i])
            for j in xrange(len(v[i])):
                output += tab+str(v[i][j])
            o.write(output+'\n')
        o.close()
        if normalized:
            print
            print 'Writing to file: '+ oname+'_normalized.txt'
            o = open(oname+'_normalized.txt','w')
            v = normalizearray(np.array(v,dtype=float))[0]
            for i in xrange(len(l)):
                output = str(l[i])+tab+str(n[i])
                for j in xrange(v.shape[1]):
                    output += tab+str(v[i,j])
                o.write(output+'\n')
            o.close()
    
class SingleLabel(object):
    def __init__(self,key,vector):
        self.key = key
        self.features = []
        self.features.append(vector)
        self.n=1
        self.percentilevector = None
        
    def addFeatureVector(self,features):
        self.features.append(features)
        self.n+=1
    
    def getPercentileVector(self):
        if self.percentilevector == None:
            percentilevector = []
            f = np.array(self.features,dtype = float)
            for i in xrange(f.shape[1]):
                percentilevector.extend(self.getPercentileValues(f[:,i]))
            self.percentilevector = np.array(percentilevector,dtype=float)    
        return self.percentilevector
    
    def getPercentileValues(self,vector,percentiles=[20,50,80]):
        p=[]
        for i in range(len(percentiles)):
            p.append(scoreatpercentile(vector,percentiles[i]))
        return p