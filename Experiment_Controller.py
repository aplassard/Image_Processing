#!/usr/bin/env python
import common

class Experiment_Controller(object):
    def __init__(self):
        self.trainingimages={}
        self.testimages={}
        self.features={}
        self.model=None
    
    def loadimages(filename):
        f = open(filename,'r')
        for line in f:
            line=line.strip().split(common.tab)
            if len(line)>2:
                loadtraining(line)
            else:
                loadtest(line)
                
    def loadtraining(line):
        pass
    
    def loadtest(line):
        pass