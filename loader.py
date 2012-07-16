#!/usr/bin/env python

from common import *

def getimagelists(filename):
    f = open(filename,'r')
    training=[]
    test=[]
    for line in f:
        if line:
            if len(line.split(tab))==1:
                test.append(line)
            elif len(line.split(tab))>2:
                training.append(line)
            else:
                print "Invalid line:",line
                
    return training,test

