# Eric Minikel
# 2012-04-04
# a script to make training images
# First, load the image into Paint or something and cover the desired segments with black
# then this will turn the image to BW and turn all the non-black to white.

import sys
import scipy as sp
import numpy as np
from numpy import *
from sys import stdout
#import color # i think not needed
import Image
from scipy.misc import imread
from scipy import signal
import math
import random

BLUE = 0
GREEN = 1
RED = 2
ALPHA = 3

listOfBoxes=[[]]

def getImageAsArray(path):
    return np.array(imread(path).astype(float))

def arrayToImage(arr):
    return Image.fromarray(np.uint8(arr))

def maketraining(path): # whitens non-segment parts
    arr = getImageAsArray(path)
    arr = collapseChannels(arr)
    for r in xrange(arr.shape[0]):
        for c in xrange(arr.shape[1]):
            if(arr[r][c] > 0):
                arr[r][c] = 255
            else:
                addBoxtoList(r, c, arr)
                arr[r][c] = 0
                
    str="";
    for a in listOfBoxes:
        for v in a:
            str=str+repr(v)+"\t"
        str=str+"\n"
        
    f=open(path+"-BlockIndexes.txt",'w')
    f.write(str)
    f.close()
    return arrayToImage(arr)


def collapseChannels(arr): # does not handle images that are already BW
    channels = arr.shape[2]
    if(channels == 4 or channels == 3):
        return (arr[:,:,RED] + arr[:,:,GREEN] + arr[:,:,BLUE])/3 # RGB or RGBA
        

def addBoxtoList(r, c, arr): # get coordinates of top left corner, and array from calling function
    global listOfBoxes
    if(r-1 > 0 ):
        oneUp=arr[r-1][c]
    else:
        oneUp=255  #white
        
    if(c-1>0):
        oneLeft=arr[r][c-1]
    else:
        oneLeft=255;
    
    if(r+5< arr.shape[0]):
        oneDown=arr[r+5][c]
    else:
        oneDown=255
        
    if(c+5 < arr.shape[1]):
        oneRight=arr[r][c+5]
    else:
        oneRight=255
    
    if( oneUp!=0 and oneLeft!=0 and oneDown==0 and oneRight==0):
        brr, brc=getCorners(r, c, arr)
        temp=[]
        temp.append(r)
        temp.append(c)
        temp.append(brr)
        temp.append(brc)
        listOfBoxes.append(temp)
    

def getCorners(r, c, arr):
    posX=0
    for posX in xrange(r, arr.shape[0]):
        if(arr[posX][c]!=0):            
            break                
    
    posX=posX-1
    posY=0
    for posY in xrange(c, arr.shape[1]):
        if(arr[r][posY]!=0):
            break 
               
    posY=posY-1
    return posX, posY
        
# Main program
if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print "Usage: python", sys.argv[0], "<input filepath> <output filepath>"
    else:
        maketraining(sys.argv[1]).save(sys.argv[2])