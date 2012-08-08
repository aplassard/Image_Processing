import numpy, colormath, colormath.color_objects, math
from common import *

def getDeltaE(model, test, mode='cie2000'):
	'''
	Magic
	'''
	return model.delta_e(test, mode, debug=false)

def convertTo(imageArray, mode='lab'):
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
	if(mode == 'rgb' ):
		return imageArray
	if(mode == 'grayscale' ):
		retImage=imageArray[:,:,0]+imageArray[:,:,1]+imageArray[:,:,2]
		retImage=retImage/3
		return retImage

	tempImage=numpy.zeros([imageArray.shape[0],imageArray.shape[1],3])
	if(imageArray.ndim==3):
		for x in xrange(imageArray.shape[0]):
			for y in xrange(imageArray.shape[1]):
				imageTuple=imageArray[x,y,:]
				imageTuple=colormath.color_objects.RGBColor(*imageTuple)
				tmp=imageTuple.convert_to(mode).get_value_tuple()
				tempImage[x,y,:]=tmp
	else:
		print"ERROR"
	return tempImage
	
def getModelFor(imageArray, mode='lab'):
	tempImage=convertTo(imageArray, mode)
	model=makeModelOf(tempImage)
	return model

def convertOnFeature(imageArr, fIndex):
	if fIndex>= 0 and fIndex<=2 :
		mode='lab'

	elif fIndex>= 3 and fIndex<=5 :
		mode='hsv'

	elif fIndex>= 6 and fIndex<=8 :
		mode='hsl'

	elif fIndex>= 9 and fIndex<=11 :
		mode='xyz'

	elif fIndex>= 12 and fIndex<=14 :
		mode='xyy'

	elif fIndex>= 15 and fIndex<=17 :
		mode='cmy'

	elif fIndex>= 18 and fIndex<=20 :
		#keep in RGB
		mode='rgb'
		pass

	elif fIndex>= 21 and fIndex<=23 :
		mode='grayscale'
		retImage=toGrayscale(imageArr)

 	channel=fIndex%3
	print "using mode ", mode , "and channel ", channel
	retImage=convertTo(imageArr, mode)
	retImage=retImage[:,:,channel]
	print "returning image of shape:", retImage.shape
	return retImage

def makeModelOf(imgArray):
	'''
	Input: imageArray
	Output: list of mean and median for each channel in imageArray
	'''
	model=[]
	if( imgArray.ndim==2):
		model.append(imgArray.mean())
		#model.append(imgArray.std())
	elif(imgArray.ndim==3):
		for i in range(imgArray.shape[2]):
			model.append(imgArray[:,:,i].mean())
			#model.append(imgArray[:,:,i].std())
	return model

def toGraysale(imageArr):
	for x in xrange(len(imageArr.shape[0])):
		for y in xrange(len(imageArr[1])):
			retImage=numpy.sum(imageArr[x,y,:])/3
	return retImage
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
	for i in xrange(len(features)):
		if(math.isnan(features[i])):
			features[i]=0;

	return features
