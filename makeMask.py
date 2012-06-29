#takes a model of the colored background image from makeBackgroundModel
# and a testing image to be processed
#returns a binary matrix, imageMask, where imageMask(x,y)=0 for background, 1 for foreground
#mainly for reducing search time, also is akind of segmentation

import numpy
import scipy
import calcualteFeatures
import imageTransforms
import Image
import common

def getMask(image, model):
    imageMask=zeros(image.shape)
    threshold=0.9
    xStep=image.shape[0]/100
    yStep=image.shape[1]/100
    for x in range(0, image.shape[0]-xStep, xStep):
        for y in range(0, image.shape[1]-yStep, yStep):
            #get sub-image of next window
            subImage=image[x:x+xStep, y:y+yStep, :]
            graySubImage=imageTransforms.graySubImage(arraytoImage(subImage))
            d={}
            d[RGB] = subImage
            d[grayscale]= graySubImage
            #get feature vector of this window
            fv=calculatefeatures(d)
            
            #get similarity with background model
            sim=getSimilarity(fv, model)
            
            #if not too similar, add it to region that should be explored in the window search
            if(sim<threshold):
                makeOnes(x, x+xStep, y, y+yStep, imageMask)
    return imageMask


def makeOnes(x1,x2,y1,y2,mask):
    for x in range(x1,x2):
        for y in range(y1, y2):
            mask[x,y]=1            

#get normalized euclidian distance
def getSimilarity(x, model):
    dist = numpy.linalg.norm(x-model)
