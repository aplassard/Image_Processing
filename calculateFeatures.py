from numpy import *
from common import *
import mahotas
from basicInfo import getColorInfo,analyseGradient
import colorModels
import math
#takes in an image array. color or grayscale. for each channel in the array it 
# calculates the mean and std dev, and returns it in a list
#returns list[]
def getPixelDist(imageArray):
	colorList=[]
	for channel in xrange(imageArray.shape[2]):
		im=image[:,:,channel]
		m=mean(im)
		s=std(im)
		colorList.append(m)
		colorList.append(s)
	return colorList

# takes in an image 3d array. returns ratio of longer axis length/ smaller 
# axis length
#returns float
def getAxisRatios(imageArray):
	x=imageArray.shape[0]
	y=imageArray.shape[1]
	ratio= max(x,y)/min(x,y,1)
	return ratio


def HaralickFeatures(arr):
	if len(arr.shape)==2:
		return mahotas.features.texture.haralick(arr,compute_14th_feature=True)
	else: print "Error image must be grayscale"
	return

def flattenHaralick(arr):
	o=[]
	for i in xrange(arr.shape[0]):
		for j in xrange(arr.shape[1]):
			o.append(arr[i][j])
	return o

def tasfeatures(arr):
	return list(mahotas.features.tas(arr))

def calculatefeatures(dictionary,left=None,right=None,top=None,bottom=None):
	vector=[]
	H=HaralickFeatures(dictionary[grayscale][top:bottom,left:right])
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB][top:bottom,left:right,GREEN])
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB][top:bottom,left:right,RED])
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB][top:bottom,left:right,BLUE])
	H = flattenHaralick(H)
	vector.extend(H)
	del H
	T=tasfeatures(dictionary[grayscale][top:bottom,left:right])
	vector.extend(T)
	T=tasfeatures(dictionary[RGB][top:bottom,left:right,GREEN])
	vector.extend(T)
	T=tasfeatures(dictionary[RGB][top:bottom,left:right,RED])
	vector.extend(T)
	T=tasfeatures(dictionary[RGB][top:bottom,left:right,BLUE])
	vector.extend(T)
	del T
	C=getColorInfo(dictionary[RGB][top:bottom,left:right])
	vector.extend(C)
	C=analyseGradient(dictionary)
	vector.extend(C)
	del C
	
	d={}
	d[RGB]=dictionary[RGB][top:bottom,left:right,:]
	d[grayscale]=dictionary[grayscale][top:bottom,left:right]
	CM=colorModels.getModelFeatures(d)
	vector.extend(CM)
	for i in xrange(len(vector)):
		if math.isnan(vector[i])==True:
			vector[i]=0.0
	return vector
	
