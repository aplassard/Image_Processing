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
		if(set([w[0]]).issubset(d)):
			y.append(d[w[0]])
		else:
			d[w[0]]=classCounter+1
			classCounter=classCounter+1
			y.append(d[w[0]])
	f.close()
	d=invert(d)
	X=numpy.array(X, dtype=float)
	y=numpy.array(y, dtype=float)
	return X,y,d

def invert(d):
	newD={}
	for k in d.keys():
		newD[d[k]]=k
	return newD