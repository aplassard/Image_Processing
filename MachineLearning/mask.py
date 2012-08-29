from FeatureCalculator import featureSelection, colorModels
import numpy, pylab
from morph import morph
from sklearn.lda import LDA

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
		
		self.makeLDA(colorFeatures[:, [i,i]], labels)
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
		
	def getMaskHelper(self, convertedImg,label, mode='LDA'):
		
		'''
		Input: image array to be thresholded, and name of label you want to threshold out, type of thresholding
		Output: binary image array
		'''
		#find ID of label
		labelID=label

		print "found label: ", labelID
		
		if(mode!='LDA'):
			#get range for ID
			l,h=self.labelRanges[labelID]	
			print "using thresholds ", l, h
			t1= (convertedImg<h)
			t2=(convertedImg>l)
			mask=(t1*t2)		
			mask=numpy.array(mask, dtype=int)
		else:
			mask=(convertedImg==labelID).astype(int)
		return mask
	
	def prepLDAMask(self, img):
		'''
		Input: Image array
		Output: mask with pixels labeled with what they are predicted to be by Linear Disctiminant Analysis
		'''
		allMask=numpy.zeros_like(img)
		for x in xrange(img.shape[0]):
			for y in xrange(img.shape[1]):
				allMask[x,y]=self.clf.predict([[img[x,y]]]).astype(int)
		
		return allMask
				
	def getAllMasks(self, imageArray, mode='LDA'):
		img=self.convertToModel(imageArray)
		if mode=='LDA':
			img=self.prepLDAMask(img)
		print img
		maskDict={}
		for key in self.labelRanges.keys():
			tempMask=self.getMaskHelper(img, key, mode)
			#tempMask=morph(tempMask)
			#tempMask=morph(tempMask, 3,'d')
			maskDict[key]=tempMask
		return maskDict
	
	def makeLDA(self,data, labels):
		self.clf=LDA()
		self.clf.fit(data, labels)
		
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
			ranges[k]=[m-(2*s), m+(2*s)]
		return ranges
