#!/usr/bin/env python

from loader import getimagelists
import processtrainingimage
from common import *
import sys
from ml import basicrunSVM,normalizearray
import numpy as np

def run(filename):
    print "Reading File"
    training,test=getimagelists(filename)
    features=[]
    labels=[]
    print "Processing files"
    for line in training:
        print "Processing file: " + line.split(tab)[0]
        l,f=processtrainingimage.process(line)
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
if __name__ == '__main__':
    run(sys.argv[1])