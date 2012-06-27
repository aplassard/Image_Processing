#!/usr/bin/env python

from common import *
import Image
import numpy as np
import getcoordinates
import imageTransforms

def process(line):
    line = line.strip().split(tab)
    sample=line[1]
    image=line[0]
    featureimages=line[2:]
    img=Image.open(image)
    images=imageTransfroms.normalizeImage(img) #Arjun's thing
    features=[]
    featurecoordinates=[]
    labels=[]
    for j in xrange(len(featureimages)):
        inf = featureimages[j].split('.')
        features.append(inf[1])
        c=getcoordinates.getcoordinates(featureimages[j],sample)
        featurecoordinates.append(c)
        del c
    for j in xrange(len(featurecoordinates)):
        features.append(runtraininganalysis(images[RGB],featurecoordinates[j]))
        labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
        
def runtraininganalysis(arr,coor):
    left=coor[1]
    right=coor[3]
    top=coor[0]
    bottom=coor[2]
    image=arr[top:bottom][left:right][:]
    image=arrayToImage(image)
    