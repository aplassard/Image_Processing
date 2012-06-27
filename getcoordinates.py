#!/usr/bin/env python

from common import *
from scipy.misc import imread
import numpy as np

def collapseChannels(arr): # does not handle images that are already BW
    channels = arr.shape[2]
    if(channels == 4 or channels == 3):
        return (arr[:,:,RED] + arr[:,:,GREEN] + arr[:,:,BLUE])/3 # RGB or RGBA
        

def getcoordinates(path,sample):
    listOfBoxes=[]
    feature=path.strip().split('.')[1]
    arr=getImageAsArray(path)
    arr=collapseChannels(arr)
    for r in xrange(arr.shape[0]):
        for c in xrange(arr.shape[1]):
            if(arr[r][c] > 0):
                arr[r][c] = 255
            else:
                listOfBoxes.append(addBoxtoList(r, c, arr,sample,feature))
                arr[r][c] = 0
    return ListOfBoxes
                
def addBoxtoList(r, c, arr,sample,feature): # get coordinates of top left corner, and array from calling function
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
        temp.append(sample)
        temp.append(feature)
        return temp
        
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