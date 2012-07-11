#!/usr/bin/env python
'''
    Code to process test image
'''
import numpy as np
import ImageTransforms
from commmon import *

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

def runWalk():
    pass