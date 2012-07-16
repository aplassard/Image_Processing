#!/usr/bin/env python
'''
    Code to process test image
'''
import numpy as np
import imageTransforms
from common import *
import Image
from calculateFeatures import calculatefeatures

__author__='Andrew Plassard'
__version__='1.0'
__email__='andrew.plassard@gmail.com'

def getWalkerParameters(arr,size,factor=4):
    '''
    Input: The image in numpy array format
           The size of the window
           The factor by which to divide the window to get step size, default 4
    Output: xrange of x steps
            xrange of y steps
            step size
            
    Example:
    >>> xvals,yvals,step = getWalkerParameters(imagearay,80)
    '''
    s=arr.shape
    step=size/factor
    y=xrange(0,s[0],step)
    x=xrange(0,s[1],step)
    return x,y,step

def runWalk(imgline,size,ML):
    '''
    Input:
        The line containing the image
        The window size
        the object of type ml
    
    Output:
        A series of arrays of the different subtypes of the image
    '''
    line = imgline.strip().split('\t')
    img = line[0]
    img = Image.open(img)
    imgs = imageTransforms.normalizeImage(img)
    x,y,step=getWalkerParameters(imgs[grayscale],size)
    for i in x:
        for j in y:
            print
            print i,i+size,j,j+size,
            f=np.array(calculatefeatures(imgs,left=i,right=i+size,top=j,bottom=j+size),dtype=float)
            labels = ML.getLabels(f)
            for i in xrange(len(labels)):
                print ML.intdict[i],
            