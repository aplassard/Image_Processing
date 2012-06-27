#!/usr/bin/env python

from common import *
import Image
import numpy as np
import getcoordinates
import imageTransforms
from calculateFeatures import calculatefeatures

def process(line):
    line = line.strip().split(tab)
    sample=line[1]
    image=line[0]
    featureimages=line[2:]
    img=Image.open(image)
    images=imageTransforms.normalizeImage(img) #Arjun's thing
    features=[]
    featurecoordinates=[]
    labels=[]
    for j in xrange(len(featureimages)):
        inf = featureimages[j].split('.')
        c=getcoordinates.getcoordinates(featureimages[j],sample)
        for i in xrange(len(c)):
            featurecoordinates.append(c[i])
        del c
    for j in xrange(len(featurecoordinates)):
        print "Now on " +str(j) + " out of " + str(len(featurecoordinates))
        newfeature=runtraininganalysis(images[RGB],featurecoordinates[j])
        if newfeature:
            for i in xrange(len(newfeature)):
                features.append(newfeature[i])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
    return labels,features
        
def runtraininganalysis(arr,coor):
    left=coor[1]
    right=coor[3]
    top=coor[0]
    bottom=coor[2]
    features=[]
    print top,bottom,left,right
    if bottom-top>4 and right-left>4:
        image=arr[top:bottom,left:right]
        image=arrayToImage(image)
        g=imageTransforms.gaussblur(image)
        gauss={}
        gauss[RGB]=Imagetoarray(g)
        gauss[grayscale]=Imagetoarray(imageTransforms.grayScale(g))
        del g
        features.append(calculatefeatures(gauss))
        s=imageTransforms.smooth(image)
        smooth={}
        smooth[RGB]=Imagetoarray(s)
        smooth[grayscale]=Imagetoarray(imageTransforms.grayScale(s))
        features.append(calculatefeatures(smooth))
        del s
        s=imageTransforms.sharpen(image)
        sharpen={}
        sharpen[RGB]=Imagetoarray(s)
        sharpen[grayscale]=Imagetoarray(imageTransforms.grayScale(s))
        features.append(calculatefeatures(sharpen))
        normal={}
        normal[RGB]=Imagetoarray(image)
        normal[grayscale]=Imagetoarray(imageTransforms.grayScale(image))
        features.append(calculatefeatures(normal))
    if features:
        return features
    else:
        print "returning none"
        return None