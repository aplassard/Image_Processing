#!/usr/bin/env python

from scipy.misc import imread
import process_image
import imagefeature

class genericimage(object):
    def __init__(self):
        self.path=None
        self.forms={}
        
    def loadimage(self,path):
        self.path = path
        self.forms['initial']=imread(path)
        
    