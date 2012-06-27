#!/usr/bin/env python

'''
Main wrapper scripts for processing
'''

def calculateFeatures(image):
	'''
	Input:	an image, training or test
	Output:	an array of feature values
	Process:
		Run through all feature analyses
	'''

def runTrainingAnalysis(trainingimage):
	'''
	Input: 	an image from the training data
	Output:	a matrix of features for the different training images
	Process:
		Create different images based on functions
			blur/smooth
			+/- gaussian noise
			contrast enhancement
			etc
		Calculate training data from images
	'''
	pass

def runTestAnalysis(testimage,model):
	'''
	Input:	an image from the test set
			the model for the classifier
	Output:	a label for the image passed in
	Process:
		calculate features from the image
		run model.apply(features)
	'''
	pass

def runAll(trainingpath,traininglabels,testimagepath):
	'''
	Input: 	a path the the images from the training data set and their labels
			the images for testing
	Output:	an array of labels for the test data
			model for the SVM (optional)
	Process:
		For each training image, pass to runTrainingAnalysis
		Train classifier on training data
		iterate through test data and get labels
	'''
	pass