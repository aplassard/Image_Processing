import numpy

def walkThrough(imageArray, window, models, z):
	w=window
	outputImage=numpy.zeros(imageArray.shape)
	for x in xrange(0,imageArray.shape[0]-w,w):
		for y in xrange(0,imageArray.shape[1]-w,w):
			imageWindow=imageArray[x:x+w, y:y+w]
			outputImage[x:x+w, y:y+w]=getClass(imageWindow, models,z)
			print "looking at ", x, " to ", x+w," and " , y," to ", y+w
	return outputImage


def getClass(imageWindow, models,z):
	hasLabel=False
	label=999
	for k in models.keys():
		m=models[k]
		l1=m[0]
		l2=m[1]
		l3=m[2]
		
		h1=m[3]
		h2=m[4]
		h3=m[5]

		ch1=numpy.mean(imageWindow[:,:,0])
		ch2=numpy.mean(imageWindow[:,:,1])
		ch3=numpy.mean(imageWindow[:,:,2])
		#print "checking if ", ch1, ch2, ch3, " is between ", h1, l1, h2, l2, h3, l3
		if(l1<ch1<h1 and l2<ch2<h2 and l3<ch3<h3):
			if(not hasLabel):
				label=k
				print "got label ", z[k]
				hasLabel=True
			else:
				print "error, relabeling as :", z[k]
				return 999
	if(not hasLabel):
		return 999
	else:
		return label
			
