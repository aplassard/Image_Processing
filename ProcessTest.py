#!/usr/bin/env python

import numpy as np
from collections import namedtuple
import ml
from calculateFeatures import calculatefeatures

def getWalkerParameters(arr,size):
    s=arr.shape
    step=size/4
    y=xrange(0,s[0],step)
    x=xrange(0,s[1],step)
    return x,y,step
    

def walkimage(params):
    pass

def runtrainingimage(path,size,model):
    line = path.strip().split(tab)
    sample=line[1]
    image=line[0]
    img=Image.open(image)
    images=imageTransforms.normalizeImage(img) #Arjun's thing
    x,y,step=getWalkerParameters(arr,size)
    for i in x:
        for j in y:
            f=calculatefeatures(img,left=x,right=x+step,top=y,bottom=y+step)
            print ml.getK(model,f)
    