#!/usr/bin/env python

import numpy as np
from collections import namedtuple
import ml
from calculateFeatures import calculatefeatures
from common import *
import imageTransforms
import sys

def getWalkerParameters(arr,size,factor=4):
    s=arr.shape
    step=size/factor
    y=xrange(0,s[0],step)
    x=xrange(0,s[1],step)
    return x,y,step
    

def walkimage(params):
    pass

def runtrainingimage(path,size,model,d):
    line = path.strip().split(tab)
    sample=line[1]
    image=line[0]
    img=Image.open(image)
    images=imageTransforms.normalizeImage(img) #Arjun's thing
    x,y,step=getWalkerParameters(images[grayscale],size)
    print "started walking"
    z={}
    for key in d.keys():
        print key,d[key]
        z[key]=np.zeros_like(images[grayscale])
    for i in x:
        for j in y:
            f=calculatefeatures(images,left=i,right=i+size,top=j,bottom=j+size)
            try:
                u=ml.getK(model,f)
                print d[u[0]]," left: ",i," right: ",i+size," top: ",j," bottom: ", j+size
                for q in xrange(size):
                    for w in xrange(size):
                        z[u[0]][q,w]+=10
            except KeyError:
                print "key error!"," left: ",i," right: ",i+size," top: ",j," bottom: ", j+size
    for key in z.keys():
        print d[key],z[key].max()
    
    
def test(featuresfile,img):
    f = open(featuresfile,'r')
    labels=[]
    features=[]
    g = open(img,'r')
    img=g.readline()
    for line in f:
        line=line.strip().split(tab)
        labels.append(line[0])
        features.append(line[1:])
    features=np.array(features).astype('float64')
    model,ldict=ml.buildLearners(labels,features)
    g=flipdict(ldict)
    runtrainingimage(img,80,model[KNN],g)
    

def flipdict(d):
    g={}
    for key in d.keys():
        g[d[key]]=key
    return g

if __name__ == '__main__':
    test(sys.argv[1],sys.argv[2])