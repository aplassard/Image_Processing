from numpy import *

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
        return mahotas.features.texture.haralick(arr,compute_th_feature=True)
    else: print "Error image must be grayscale"
    return