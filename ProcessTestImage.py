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
    y=xrange(0,s[0]-size,step)
    x=xrange(0,s[1]-size,step)
    return x,y,step
            
def iterRegions(x,y,size,arr):
    for i in xrange(size):
        for j in xrange(size):
            try:
                arr[i+y,j+x]+=1
            except:
                pass
    return arr

def saveImages(arrdict,keydict,threshold=None):
    for key in keydict.keys():
        if threshold==None:
            savearray(arrdict[key],keydict[key]+'.tif')
        else:
            savearray(arrdict[key],keydict[key]+'.'+str(threshold)+'.tif')
        
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
    x,y,step=getWalkerParameters(imgs[grayscale],size,factor=8)
    arraydict = []
    for key in ML.intdict.keys():
        arraydict.append(np.zeros_like(imgs[grayscale],dtype=int))

    for i in x:
        for j in y:
            print
            print i,i+size,j,j+size,
            try:
                f=np.array(calculatefeatures(imgs,left=i,right=i+size,top=j,bottom=j+size),dtype=float)
                labels = ML.getLabels(f)
                for k in xrange(len(labels)):
                    print ML.intdict[labels[k]],
                    arraydict[labels[k]]=iterRegions(i,j,size,arraydict[labels[k]])                            
            except ValueError:
                for i in xrange(len(vector)):
                    print vector[i],
    print
    print 'Saving Images'
    saveImages(arraydict,ML.intdict)
    nimages=[]
    for i in xrange(len(arraydict)):
        t = 20
        nimages.append(thresholdImage(arraydict[i],imgs[RGB],t))
    saveImages(nimages,ML.intdict,threshold=t)

def thresholdImage(vals,arr,threshold):
    for i in xrange(vals.shape[0]):
        for j in xrange(vals.shape[1]):
            if vals[i,j]<=threshold:
                if len(arr.shape)<3:
                    arr[i,j]=0
                else:
                    for k in xrange(arr.shape[2]):
                        arr[i,j,k]=0
    return arr
                    