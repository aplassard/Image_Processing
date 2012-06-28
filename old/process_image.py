'''

Created on Jun 20, 2012

@Author: Andrew Plassard

'''
import sys
import scipy as sp
import numpy as np
from numpy import *
import Image 
import PIL.Image as PILImage
import PIL.BmpImagePlugin
import PIL.DcxImagePlugin
import PIL.EpsImagePlugin
import PIL.GifImagePlugin
import PIL.JpegImagePlugin
import PIL.PngImagePlugin
import PIL.TiffImagePlugin as TIFF
from scipy.misc import imread
from scipy.misc import imsave
from scipy import signal
import math
import random

BLUE=0
GREEN=1
RED=2
ALPHA=3

def getImageAsArray(path):
	return np.array(imread(path).astype(float))

def arrayToImage(arr):
	return Image.fromarray(np.uint8(arr))

def getGradient(arr):
	r=arr.shape[0]
	c=arr.shape[1]
	o=np.zeros((r,c))
	for i in xrange(1,r-1):
		for j in xrange(1,c-1):
                        val1=(arr[i-1][j]-arr[i+1][j])**2
                        val2=(arr[i][j-1]-arr[i][j+1])**2
			o[i][j]=sqrt(val1+val2)
	return o

def makeGrayScale(arr,method='average'):
	if method=='average':
		return (arr[:,:,RED] + arr[:,:,GREEN] + arr[:,:,BLUE])/3
	elif method=='luminosity':
		return (0.21*arr[:,:,RED] + 0.71*arr[:,:,GREEN] + 0.07*arr[:,:,BLUE])/3
	elif method=='lightness':
		o = np.zeros((arr.shape[0],arr.shape[1]))
		for r in xrange(arr.shape[0]):
			for c in xrange(arr.shape[1]):
				vals = [arr[r][c][RED],arr[r][c][GREEN],arr[r][c][BLUE]]
				o[r][c]=(max(vals)+min(vals))/2
		return o

def makeGrayScaleRGB(arr,r,g,b):
        return (r*arr[:,:,RED] + g*arr[:,:,GREEN] + b*arr[:,:,BLUE])/3

def threshold(arr,t):
        r=arr.shape[0]
        c=arr.shape[1]
        o = np.zeros((r,c))
        for i in xrange(r):
                for j in xrange(c):
                        if arr[i][j]>t:
                                o[i][j]=255
                        else:
                                o[i][j]=0
        return o


def subtractBackground(arr):
        s=arr.shape
        if len(s)==2:
                m=arr.mean()
                for i in xrange(s[0]):
                        for j in xrange(s[1]):
                                arr[i][j]=max([(arr[i][j]-m),0])
        else:
                for k in range(s[2]):
                        m=arr[:,:,k].mean()
                        for i in xrange(s[0]):
                                for j in xrange(s[1]):
                                        arr[i][j][k]=max([(arr[i][j][k]-m),0])
        return arr

def getHistNorm(arr):
        maxVal=arr.max()
        minVal=arr.min()
        for r in xrange(arr.shape[0]):
            for c in xrange(arr.shape[1]):
                arr[r][c]=(arr[r][c]-minVal)
		arr[r][c]*=(255/(maxVal-minVal))
        return arr
