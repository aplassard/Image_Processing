#!/usr/bin/env python
import Image
import numpy as np
from scipy.misc import imread,imsave
tab='\t'

BLUE = 0
GREEN = 1
RED = 2
ALPHA = 3

def arrayToImage(arr):
    return Image.fromarray(np.uint8(arr))
    
def Imagetoarray(img):
    return np.array(img)
    
def getImageAsArray(path):
    print path
    return np.array(imread(path).astype(float))
    
def savearray(arr,path):
    imsave(path,arr)
    
grayscale='grayscale'
gradient='gradient'
RGB='RGB'
fftimage='fftimage'
KNN='KNN'
Neural='Neural'
SVM='SVM'
originalRGB='originalRGB'
originalgrayscale='originalgrayscale'
numfeatures=502
