import numpy

def loadFile(fileName):
	X=[]
	y=[]
	d={}
	classCounter=0
	f=open(fileName)
	for line in f:
		w=line.split("\t")
		temp=w[1:]
		X.append(temp)
		y.append(w[0])
	f.close()
	X=numpy.array(X, dtype=float)	
	return X,y
