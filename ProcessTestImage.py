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
import analysis_functions
from scipy.stats import mode
from ImageClass import ImageClass

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
    >>> xvals,yvals,step = getWalkerParameters(imagearray,80)
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

    #make binary image mask by thresholding for each object label (neuron, astrocyte, ...)
    tempColorImg=imgs['RGB']
    imageMasks=ML.maskGen.getAllMasks(tempColorImg, 'LDA')
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
    savearray(imgs['grayscale'],'grayscale.tif')
    gradient = analysis_functions.getGradient(imgs['grayscale'])
    savearray(gradient,'gradient.tif')

    print
    #running watershed on GRADIENT images for all objects/ masks
    segments = {}
    for key in imageMasks.keys():
	x = imageMasks[key]
	gx = gradient*x
	s, sb=getSeeds(x)
	print 'Running Watershed on Gradient'

	rwGradient = runWatershed(s,gx)
	#savearray(sb, ML.intdict[key]+"centersBinary-Grad.tiff")
	#savearray(s, ML.intdict[key]+"centers-Grad.tiff")
	savearray(rwGradient,ML.intdict[key]+'_watershed_on_gradient.tif')
	segments[key]=rwGradient

    #running watershed on GRAYSCALE images for all objects/ masks
    for key in imageMasks.keys():
        x = imageMasks[key]
        gx = imgs['grayscale']*x
        s, sb=getSeeds(x)
        print 'Running Watershed on Grayscale'        
        rwGray = runWatershed(s,gx)
	#savearray(sb, ML.intdict[key]+"centersBinary-GrayScale.tiff")
	#savearray(s, ML.intdict[key]+"centers-GrayScale.tiff")
        savearray(rwGray,ML.intdict[key]+'_watershed_on_grayscale.tif')
        segments[key]=rwGray

    '''
    l = {}
    for key in segments.keys():
        l[key] = getImageClass(segments[key],imgs)
    
    for key in l.keys():
        l[key].toFile(ML.intdict[key]+'_features')
    '''

def saveImages(arrdict,keydict,threshold=None):
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
    Ximage=np.zeros_like(imageArray,dtype=int)
    Yimage=np.zeros_like(imageArray,dtype=int)
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
        if(lineToggle):
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
        if (lineToggle):
            lineToggle=False
            middle=(float(startX+x))/2
            Ximage[middle, y]=1
            
    centers=Ximage*Yimage
    centersBinary=Ximage*Yimage
    counter=0
    for y in xrange(imageArray.shape[1]):
        for x in xrange(imageArray.shape[0]):
            if(centers[x,y]==1):
                centers[x,y]=counter
                counter+=1

    return centers, centersBinary

def removeWatershedJunk(arr,minsize=None):
    arr = arr.astype(int)
    m = arr.max()
    v = m+1

    if minsize==None:
        minsize = (arr.shape[0]*arr.shape[1])/200
    n=m+1
    print 'Removing Junk with size less than: ' + str(minsize)
    print 'There are', n, 'objects in total'
    print
    t = n*.05
    z = t
    num=0
    for i in xrange(0,n):
        if i > t:
            print 'Finished: ' + str(t*100/n) + '% of filtering.  ' + str(num) +' have been Removed out of ' +str(i)+'.'
            t+=z
        c = sum(sum((arr==i).astype(int)))
        if c < minsize:
            num+=1
            tmp = (arr==i).astype(int)*(v)
            arr = arr*(arr!=i).astype(bool)
            arr+=tmp
    
    print
    print 'In total, ' + str(num) + ' objects were removed out of ' + str(m)
    return arr
    
def getImageClass(w,imgs,size=8):
    x,y,step = getWalkerParameters(w,size,factor=1)
    p = .9*size*size
    z=mode(w.ravel())[0][0]
    IC = ImageClass()
    for j in x:
        for i in y:
            try:
                img = w[i:i+step,j:j+step]
                m = mode(img.ravel())
                c=m[1][0]
                m=m[0][0]
                if c > p and m!=z:
                    print i,i+step,j,j+step,m,c,p
                    IC.addVector(int(m),calculatefeatures(imgs,left=j,right=j+step,top=i+step,bottom=i))
                else:
                    print i,i+step,j,j+step,"skipped",m,c,p
            except:
                print i,i+step,j,j+step,"failed"
    return IC
    