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
    normimg=normalize(img) #Arjun's thing
    features=[]
    featurecoordinates=[]
    for j in range(len(featureimages)):
        inf = featureimages[j].split('.')
        features.append(inf[1])
        c=getcoordinates.getcoordinates(featureimages[j],sample)
        featurecoordinates.append(c)
        del c
    