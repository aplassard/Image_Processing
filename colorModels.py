import numpy, colormath, colormath.color_objects
from common import *

'''

takes imageArray, returns imageArray in specified color model
def rgbToXXX(RGBimageArray, mode='lab'):
	make array of zeros of the same size as the input image array -> retImageArray
	for each row
		for each column
			get RGB tuple at location x,y in imageArray
			make RGB ColorObject
			retImageArray[x,y,:]= RGB tuple converted into XXX tuple
	return retImage

will convert to:
'lab'
'xyz'
'xyy'
'rgb'
'cmy'
'hsv'
'hsl'

take imageArray, returns array with mean [L, a, b] for it.
def getModel(RGBimageArray, mode='lab'):
	make array of zeros of the same size as the input image array -> tempImageArray
	for each row
		for each column
			get RGB tuple at location x,y in imageArray
			make RGB ColorObject
			tempImageArray[x,y,:]= RGB tuple converted into XXX tuple
	calculate mean of each dimension -> model
	return model

takes mean [l,a,b] values for modelX(neuron, astrocyte...) and a test imageArray and returns the 
delta e distance
def getDeltaE(modelX, test):
	magic

'''

def rgbTo(imageArray, mode='lab'):
	#print("model",mode)
	retImage=numpy.zeros(imageArray.shape)
	for x in xrange(imageArray.shape[0]):
		#print("Row: ", x)
		for y in xrange(imageArray.shape[1]):
			imageTuple=imageArray[x,y,:]
			imageTuple=colormath.color_objects.RGBColor(*imageTuple)
			retImage[x,y,:]=imageTuple.convert_to(mode).get_value_tuple()
	return retImage

def getDeltaE(model, test, mode='cie2000'):
	return model.delta_e(test, mode, debug=false)
	
def getModelFor(imageArray, mode='lab'):
	tempImage=numpy.zeros(imageArray.shape)
	for x in xrange(imageArray.shape[0]):
		#print("Row: ",x)
		for y in xrange(imageArray.shape[1]):
			imageTuple=imageArray[x,y,:]
			imageTuple=colormath.color_objects.RGBColor(*imageTuple)
			tempImage[x,y,:]=imageTuple.convert_to(mode).get_value_tuple()
	model=makeModelOf(tempImage)
	return model

def makeModelOf(array):
	model=[]
	model.append(array[:,:,0].mean())
	model.append(array[:,:,0].std())
	model.append(array[:,:,1].mean())
	model.append(array[:,:,1].std())
	model.append(array[:,:,2].mean())
	model.append(array[:,:,2].std())
	return model

def getModelFeatures(imageArrDict):
	features=[]
	rgb=imageArrDict[RGB]
	gray=imageArrDict[grayscale]
	features.extend(getModelFor(rgb,'lab'))
	features.extend(getModelFor(rgb,'hsv'))
	features.extend(getModelFor(rgb,'hsl'))
	features.extend(getModelFor(rgb,'xyz'))
	features.extend(getModelFor(rgb,'xyy'))
	features.extend(getModelFor(rgb,'cmy'))
	'''
	features.extend(getModelFor(gray,'lab'))
	features.extend(getModelFor(gray,'hsv'))
	features.extend(getModelFor(gray,'hsl'))
	features.extend(getModelFor(gray,'xyz'))
	features.extend(getModelFor(gray,'xyy'))
	features.extend(getModelFor(gray,'cmy'))
	'''
	features=numpy.array(features);
	return features
