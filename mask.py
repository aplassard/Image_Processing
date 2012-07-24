import featureSelection

class Mask(object):
	def __init__(self):

	def loadTrainData(colorFeatures, labels):
		'''
		Input: Color model features, and labels
		Objective: Compute best feature for thresholding and threshold range for each label
		'''
		distinctLabels = list(set(labels))
	def thresholdOn(imageArray,labelName):
		'''
		Input: image array to be thresholded, and name of label you want to threshold out
		Output: binary image array
		'''
