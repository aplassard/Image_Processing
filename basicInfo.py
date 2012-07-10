from numpy import *
import analysis_functions
from common import *

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


def analyseGradient(imagedict):
	R=analysis_functions.getGradient(imagedict[RGB][:,:,RED])
	G=analysis_functions.getGradient(imagedict[RGB][:,:,GREEN])
	B=analysis_functions.getGradient(imagedict[RGB][:,:,BLUE])
	GRAY=analysis_functions.getGradient(imagedict[grayscale])
	colorlist=[]
	colorlist.append(mean(R))
	colorlist.append(mean(G))
	colorlist.append(mean(B))
	colorlist.append(mean(GRAY))
	colorlist.append(std(R))
	colorlist.append(std(G))
	colorlist.append(std(B))
	colorlist.append(std(GRAY))
	return colorlist