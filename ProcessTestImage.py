#!/usr/bin/env python
'''
    Code to process test image
'''
import numpy as np
import imageTransforms
from common import *
import Image
from calculateFeatures import calculatefeatures
from scipy.ndimage import watershed_ift
import pylab
from scipy.misc import imsave

__author__='Andrew Plassard'
__version__='1.0'
__email__='andrew.plassard@gmail.com'

def getWalkerParameters(arr,size,factor=1.5):
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


def runWalk(imgline,size,ML):
    '''
    Input:
        The line containing the image
        The window size
        the object of type ml
    Output:
        A series of arrays of the different subtypes of the image
    '''
    fillThreshold=0.1
    line = imgline.strip().split('\t')
    img = line[0]
    img = Image.open(img)
    imgs = imageTransforms.normalizeImage(img)
    x,y,step=getWalkerParameters(imgs[grayscale],size,factor=2)

    arraydict = []
    for key in ML.intdict.keys():
        arraydict.append(np.zeros_like(imgs[grayscale],dtype=int))
        temp=ML.intdict[key]
        f= temp.find('background')
        if f>-1:
            bgIndex=key

    #make binary image mask by thresholding on background
    tempColorImg=imgs['RGB']
    imageMasks=ML.maskGen.getAllMasks(tempColorImg)
    saveImages(imageMasks, ML.intdict)
    '''
    for i in x:
        for j in y:
            print
            print i,i+size,j,j+size,
            subMask=imageMask[j:j+size, i:i+size]
	    subMask=float(subMask.sum())
	    percentFilled=subMask/(size*size)
	    #if subregion has enough 1's in it, the go ahead, else do nothing
	    if(percentFilled>=fillThreshold):
		try:
		    f=np.array(calculatefeatures(imgs,left=i,right=i+size,top=j+size,bottom=j),dtype=float)
		    labels = ML.getLabels(f)
		    for k in xrange(len(labels)):
			print ML.intdict[labels[k]],
			arraydict[labels[k]]=iterRegions(i,j,size,arraydict[labels[k]])
		except ValueError:
                    for i in xrange(len(vector)):
                        print vector[i],
            else:
                print "skipping"
    saveImages(nimages,ML.intdict,threshold=t)

    print 'Finding Local Maxima'
    markers = getSeeds(imageMask)
    print 'Running Watershed'
    watersheded = runWatershed(markers,imageMask)
    print watersheded.shape
    imsave('watersheded_image.tif', watersheded)
    '''

def saveImages(arrdict,keydict,threshold=None):
    print arrdict
    for key in keydict.keys():
	if threshold==None:
	    savearray(arrdict[key],keydict[key]+'.tif')
	else:
	    savearray(arrdict[key],keydict[key]+'.'+str(threshold)+'.tif')

def runWatershed(markers,arr):
    arr=np.logical_not(arr)
    markers=np.array(markers, dtype=(np.int16))
    arr=np.array(arr, dtype=np.uint8)
    res = watershed_ift(arr,markers)
    return res

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


def getSeeds(imageArray):
    Ximage=np.zeros_like(imageArray)
    Yimage=np.zeros_like(imageArray)
    for x in xrange(imageArray.shape[0]):
	lineToggle=False
	for y in xrange(imageArray.shape[1]):
	    if(imageArray[x,y]==1 and lineToggle==False):
		lineToggle=True
		startY=y
	    elif(imageArray[x,y]==0 and lineToggle==True):
		lineToggle=False
		middle=(float(startY+y))/2
		Yimage[x, middle]=1

    for y in xrange(imageArray.shape[1]):
	lineToggle=False
	for x in xrange(imageArray.shape[0]):
	    if(imageArray[x,y]==1 and lineToggle==False):
		lineToggle=True
		startX=x
	    elif(imageArray[x,y]==0 and lineToggle==True):
		lineToggle=False
		middle=(float(startX+x))/2
		Ximage[middle, y]=1
    centers=Ximage*Yimage
    imsave("centers-binary.tiff", centers)
    counter=0
    for y in xrange(imageArray.shape[1]):
	for x in xrange(imageArray.shape[0]):
	    if(centers[x,y]==1):
		centers[x,y]=counter
		counter+=1
    imsave("centers.tiff", centers)

    return centers
