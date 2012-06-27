#!/usr/bin/env python

import numpy as np
from scipy import ndimage
import mahotas
import pymorph
import matplotlib

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
