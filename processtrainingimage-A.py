#!/usr/bin/env python

from common import *
import Image
import numpy as np
import getcoordinates
import imageTransforms
from calculateFeatures import calculatefeatures
import colorModels
def process(line,d):
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
        c=getcoordinates.getcoordinates(featureimages[j],sample)
        for i in xrange(len(c)):
            featurecoordinates.append(c[i])
        del c
    for j in xrange(len(featurecoordinates)):
        a=d.get(featurecoordinates[j][5],0)
        m=max([a,featurecoordinates[j][2]-featurecoordinates[j][0],featurecoordinates[j][3]-featurecoordinates[j][1]])
        d[featurecoordinates[j][5]]=m
    for j in xrange(len(featurecoordinates)):
        newfeature=runtraininganalysis(images[RGB],featurecoordinates[j])
        if newfeature:
            for i in xrange(len(newfeature)):
                features.append(newfeature[i])
                print("new feature",i)
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
            labels.append(featurecoordinates[j][4]+"_"+featurecoordinates[j][5])
    return labels,features,d
        
def runtraininganalysis(arr,coor):
    left=coor[1]
    right=coor[3]
    top=coor[0]
    bottom=coor[2]
    features=[]
    if bottom-top>4 and right-left>4:
        image=arr[top:bottom,left:right]
        image=arrayToImage(image)
        g=imageTransforms.gaussblur(image)
        gauss={}
        gauss[RGB]=Imagetoarray(g)
        gauss[grayscale]=Imagetoarray(imageTransforms.grayScale(g))
        del g
        #features.append(calculatefeatures(gauss))
	features.append(colorModels.getModelFeatures(gauss))
        s=imageTransforms.smooth(image)
        smooth={}
        smooth[RGB]=Imagetoarray(s)
        smooth[grayscale]=Imagetoarray(imageTransforms.grayScale(s))
        #features.append(calculatefeatures(smooth))
	features.append(colorModels.getModelFeatures(smooth))
        del s
        s=imageTransforms.sharpen(image)
        sharpen={}
        sharpen[RGB]=Imagetoarray(s)
        sharpen[grayscale]=Imagetoarray(imageTransforms.grayScale(s))
        #features.append(calculatefeatures(sharpen))
	features.append(colorModels.getModelFeatures(sharpen))
        normal={}
        normal[RGB]=Imagetoarray(image)
        normal[grayscale]=Imagetoarray(imageTransforms.grayScale(image))
        #features.append(calculatefeatures(normal))
	features.append(colorModels.getModelFeatures(normal))
    if features:
        return features
    else:
        return None
