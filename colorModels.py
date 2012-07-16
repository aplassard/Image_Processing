import numpy, colormath, colormath.color_objects, math
from common import *

def getDeltaE(model, test, mode='cie2000'):
	'''
	Magic
	'''
	return model.delta_e(test, mode, debug=false)
	
def getModelFor(imageArray, mode='lab'):
	'''
	Input: imageArray, coloeModel code,
	Output: imageArray in specified color model
	available color models
	'lab'
	'xyz'
	'xyy'
	'rgb'
	'cmy'
	'hsv'
	'hsl'
	'''

	tempImage=numpy.zeros([imageArray.shape[0],imageArray.shape[1],3])
	if(imageArray.ndim==3):
		for x in xrange(imageArray.shape[0]):
			for y in xrange(imageArray.shape[1]):
				imageTuple=imageArray[x,y,:]
				imageTuple=colormath.color_objects.RGBColor(*imageTuple)
				tmp=imageTuple.convert_to(mode).get_value_tuple()
				tempImage[x,y,:]=tmp
		#get model of converted image
	else:
		print"ERROR"
	model=makeModelOf(tempImage)
	return model

def makeModelOf(imgArray):
	'''
	Input: imageArray
	Output: list of mean and median for each channel in imageArray
	'''
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
	'''
	Input: imageArray
	Output: models of image in 6 different color models + originals
	'''
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
	for i in len(features):
		if(math.isnan(features[i])):
			features[i]=0;

	return features
