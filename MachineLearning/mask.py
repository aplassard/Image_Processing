from FeatureCalculator import featureSelection, colorModels
import numpy, pylab

class mask(object):
	def __init__(self,colorFeatures, labels, labelDict):
		'''
		Input: Color model features, labels, and an integer-label-> character-label dict
		Objective: Compute best feature for thresholding and threshold range for each label
		'''
		mask=featureSelection.getMask(colorFeatures, labels, 1)
		for i in xrange(0,len(mask)):
			if mask[i]==True:
				break
		print mask
		self.bestFeatureIndex=i
		print "Best feature index: ", self.bestFeatureIndex
		print "best data ", colorFeatures[:,i]
		self.labelRanges=self.makeRanges(colorFeatures[:,i], labels)
		print "ranges ", self.labelRanges
		self.labelDict=labelDict
		print "Inverted Dict: ", self.labelDict

	def getMask(self, imageArray, label):
		img = self.convertToModel(imageArray)
		mask = self.getMaskHelper(img, label)
		return mask
		
	def convertToModel(self, imageArray):		
		#get image, convert to best colormodel based on self.bestFeatureIndex
		img=colorModels.convertOnFeature(imageArray, self.bestFeatureIndex)
		return img
		
	def getMaskHelper(self, convertedImg,label):
		
		'''
		Input: image array to be thresholded, and name of label you want to threshold out
		Output: binary image array
		'''
		#find ID of label
		labelID=label

		print "found label: ", labelID

		#get range for ID
		l,h=self.labelRanges[labelID]


		print "using thresholds ", l, h
		t1= (convertedImg<h)
		t2=(convertedImg>l)
		mask=(t1*t2)		
		mask=numpy.array(mask, dtype=int)
		return mask

	def getAllMasks(self, imageArray):		
		img=self.convertToModel(imageArray)
		maskDict={}
		for key in self.labelRanges.keys():
			maskDict[key]=self.getMaskHelper(img, key)			
		return maskDict
	
	def makeRanges(self, bestCol, labelName):
		'''
		Input: single column of values to threshold on, and labels
		Output: A dictionary containing label-> range of values
		'''
		d={}
		distinctLabels = list(set(labelName))
	
		for i in xrange(len(labelName)):
			l=labelName[i];
			temp=[]
			temp.append(bestCol[i])
			if(set([l]).issubset(d)):
				temp.extend(d[l])
			d[l]=temp
		ranges={}
		for k in d.keys():
			x=numpy.array(d[k])
			m=x.mean()
			s=x.std()
			ranges[k]=[m-(4*s), m+(1*s)]
		return ranges
