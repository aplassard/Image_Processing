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
    print "Running Machine Learning"
    l = basicrunSVM(labels,features,features)
    correct=0
    print features[0:3,0:3]
    for i in range(len(l)):
        if l[i]==labels[i]: correct+=1
    print "The number correctly identified was: " + str(correct) +"/" + str(len(l)) + " for a total of " + str(100*float(correct)/float(len(l))) + "% correct before normalization!"
    features=normalizearray(features)
    print "Running Machine Learning with normalized values"
    l = basicrunSVM(labels,features,features)
    correct=0
    for i in range(len(l)):
        if l[i]==labels[i]: correct+=1
    print "The number correctly identified was: " + str(correct) +"/" + str(len(l)) + " for a total of " + str(100*float(correct)/float(len(l))) + "% correct after normalization!"
if __name__ == '__main__':
    run(sys.argv[1])