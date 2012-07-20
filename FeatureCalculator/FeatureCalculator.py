#!/usr/bin/env python
from common import *

__author__='Andrew Plassard'
__version__='1.0'
__email__='andrew.plassard@gmail.com'

class FeatureCalculator(object):
    def __init__(self,features=None):
        self.boolfeatures = features
        
            
    def __call__(self,imgdict):
        return self.calculatefeatures(imgdict)
        
    def calcluatefeatures(self,imgdict):
        pass