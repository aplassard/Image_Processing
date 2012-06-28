from numpy import *
from common import *
import mahotas
from basicinfo import getColorInfo
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

def calculatefeatures(dictionary):
	vector=[]
	H=HaralickFeatures(dictionary[grayscale])
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB](:,:,GREEN))
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB](:,:,RED))
	H = flattenHaralick(H)
	vector.extend(H)
	H=HaralickFeatures(dictionary[RGB](:,:,BLUE))
	H = flattenHaralick(H)
	vector.extend(H)
	del H
	T=tasfeatures(dictionary[grayscale])
	vector.extend(T)
	T=tasfeatures(dictionary[RGB](:,:,GREEN))
	vector.extend(T)
	T=tasfeatures(dictionary[RGB](:,:,RED))
	vector.extend(T)
	T=tasfeatures(dictionary[RGB](:,:,BLUE))
	vector.extend(T)
	del T
	C=getColorInfo(dictionary[RGB])
	vector.extend(C)
	del C
	return vector
	