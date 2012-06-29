from numpy import *

#takes in an image 3d array. for each channel in the array it calculates
# the mean and std dev, and returns it in a list
def getColorInfo(imageArray):
	colorList=[]
	for channel in xrange(imageArray.shape[2]):
		im=imageArray[:,:,channel]
		m=mean(im)
		s=std(im)
		colorList.append(m)
		colorList.append(s)
	return colorList

# takes in an image 3d array. returns ratio of longer axis length/ smaller 
# axis length
def getAxisRatios(imageArray):
	x=imageArray.shape[0]
	y=imageArray.shape[1]
	ratio= max(x,y)/min(x,y,1)
	return ratio


