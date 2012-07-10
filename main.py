#!/usr/bin/env python

from loader import getimagelists
import processtrainingimage
from common import *
import sys
import ml
import numpy as np
import ProcessTest

def run(filename):
    print "Reading File"
    training,test=getimagelists(filename)
    features=[]
    labels=[]
    d={}
    for line in training:
        print "Processing file: " + line.split(tab)[0]
        l,f,d=processtrainingimage.process(line,d)
        for i in range(len(f)):
            features.append(f[i])
        for i in range(len(l)):
            labels.append(l[i])
    o=open('output.txt','w')
    print "outputting"
    for i in xrange(len(labels)):
        output = labels[i]
        for j in xrange(len(features[i])):
            output+=tab+str(features[i][j])
        o.write(output+'\n')
    print "Converting nested list to array"
    features=np.array(features)
    print "Building Machine Learning Models"
    model,ldict,m,s=ml.buildLearners(labels,features)
    print "Starting Testing Images!"
    for line in test:
        print "Processing file: " + line.split(tab)[0]
        for key in d.keys():
            ProcessTest.runtrainingimage(line,80,model,ldict,m,s)
            
if __name__ == '__main__':
    run(sys.argv[1])