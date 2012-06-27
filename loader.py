#!/usr/bin/env python

import common

def getimagelists(filename):
    f = open(filename,'r')
    training=[]
    test=[]
    for line in f:
        if line:
            if len(line.split(tab))==2:
                test.append(line)
            else:
                training.append(line)
                
    return training,test

