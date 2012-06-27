#!/usr/bin/env python

from common import *
import Image
import numpy as np
import getcoordinates

def process(line):
    line = line.strip().split(tab)
    sample=line[1]
    image=line[0]
    featureimages=line[2:]
    img=Image.open(image)
    images=getimagedict(img) #Arjun's thing
    features=[]
    featurecoordinates=[]
    labels=
    for j in xrange(len(featureimages)):
        inf = featureimages[j].split('.')
        features.append(inf[1])
        c=getcoordinates.getcoordinates(featureimages[j],sample)
        featurecoordinates.append(c)
        del c
    for j in xrange(len(featurecoordinates)):
        features.append(runtraininganalysis(images[RGB],featurecoordinates[j]))
        
def runtraininganalysis(arr,coord)