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
	if(imageArray.ndim==3):
		for x in xrange(imageArray.shape[0]):
			for y in xrange(imageArray.shape[1]):
				imageTuple=imageArray[x,y,:]
				imageTuple=colormath.color_objects.RGBColor(*imageTuple)
				tempImage[x,y,:]=imageTuple.convert_to(mode).get_value_tuple()
		#get model of converted image
	else:
		print"ERROR"
	model=makeModelOf(tempImage)
	return model

def makeModelOf(imgArray):
	model=[]
	if( imgArray.ndim==2):
		model.append(imgArray.mean())
		model.append(imgArray.std())
	elif(imgArray.ndim==3):
		for i in range(imgArray.shape[2]):
			model.append(imgArray[:,:,i].mean())
			model.append(imgArray[:,:,i].std())
	return model

def getModelFeatures(imageArrDict):
	features=[]
	rgb=imageArrDict[RGB]

	features.extend(getModelFor(rgb,'lab'))
	features.extend(getModelFor(rgb,'hsv'))
	features.extend(getModelFor(rgb,'hsl'))
	features.extend(getModelFor(rgb,'xyz'))
	features.extend(getModelFor(rgb,'xyy'))
	features.extend(getModelFor(rgb,'cmy'))

	#add RGB mean and std
	features.extend(makeModelOf(rgb))

	#grayscale cannot be converted into other models. just get mean and std	
	gray=imageArrDict[grayscale]
	features.extend(makeModelOf(gray))
	
	#return as array
	#features=numpy.array(features);
	return features
