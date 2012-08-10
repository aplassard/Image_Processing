#!/usr/bin/env python

import numpy as np
from scipy import ndimage
import mahotas
import pymorph
import matplotlib
from math import sqrt

'''
makeMarkers:

input: array for watershed and distance apart in pixels for initialized markers
output: binary array of markers for starting points of watershed algorithm

'''

def makeMarkers(arr,dist):
    s=arr.shape
    o=np.zeros((s[0],s[1])).astype('bool')
    dist=int(dist)
    for r in xrange(s[0]/dist):
        for c in xrange(s[1]/dist):
            o[r*dist][c*dist]=True
    return o


def runWatershed(arr,seeds):
    return pymorph.cwatershed(arr,seeds)
    
def HaralickFeatures(arr):
    if len(arr.shape)==2:
        return mahotas.features.texture.haralick(arr,compute_th_feature=True)
    else: print "Error image must be grayscale"
    return


def getGradient(arr):
    sqrt(0)
    arr=arr.astype(float)
    r=arr.shape[0]
    c=arr.shape[1]
    o=np.zeros((r,c),dtype=float)
    for i in xrange(1,r-1):
        for j in xrange(1,c-1):
            val1=(arr[i-1][j]-arr[i+1][j])**2
            val2=(arr[i][j-1]-arr[i][j+1])**2
            o[i][j]=sqrt(val1+val2)
    return o
