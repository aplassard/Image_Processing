import featureSelection, numpy, colorModels

class mask(object):
	def __init__(self):
		pass

	def loadTrainData(self,colorFeatures, labels):
		'''
		Input: Color model features, and labels
		Objective: Compute best feature for thresholding and threshold range for each label
		'''
		bestFeatureData, mask=featureSelection.getMask(colorFeatures, labels, 1)
		for i in xrange(0,len(mask)):
			if mask[i]==True:
				break
		self.bestFeatureIndex=i
		self.labelRanges=self.makeRanges(bestFeatureData, labels)

	def thresholdOn(self, imageArray,labelName):
		'''
		Input: image array to be thresholded, and name of label you want to threshold out
		Output: binary image array
		'''
		l,h=self.labelRanges[labelName]
		img=colorModels.convertOnFeature(imageArray, self.bestFeatureIndex)
		mask= (img>h) and (img<l)
		return mask

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
			ranges[k]=[m-s, m+s]

		return ranges
