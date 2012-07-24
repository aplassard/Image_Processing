import numpy

def getSimpleModel(X, y, z):
	'''
	Input: features(mean and std), labels
	Output: highRange, lowRange for each feature
	'''
	models={}
	modelCounter={}
	for i in xrange(X.shape[0]):
		label=y[i]
		colorDetails=X[i, :]
		if(set([label]).issubset(models)):
			temp=models[label]
			temp=numpy.vstack((temp,(colorDetails)))
			models[label]=temp
		else:
			models[label]=colorDetails
	processModels(models)
	return models,z

def processModels(m):
	for k in m.keys():
		data=m[k]
		maxData=data.max(0)
		minData=data.min(0)
		data=minData
		data=numpy.hstack((data,maxData))
		m[k]=data
		print "DATA: ", data
	return m
		
