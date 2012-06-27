#!/usr/bin/env python

tab='\t'

BLUE = 0
GREEN = 1
RED = 2
ALPHA = 3

def arrayToImage(arr):
    return Image.fromarray(np.uint8(arr))
    
def getImageAsArray(path):
    return np.array(imread(path).astype(float))
    
