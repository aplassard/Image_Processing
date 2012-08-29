import numpy

def loadData(fileName):
    f= open(fileName, 'r')
    data=[]
    values={}
    counter=0
    for line in f:
        line=line.replace("\n","")
        temp=line.split("\t")
        data.append(temp)
        for v in temp:
            v=int(v)
            if(not(set([v]).issubset(values))):
                values[v]=counter
                counter+=1
    data=numpy.array(data).astype(int)
    return data, values

def getMatrix(data, dValues):
    mat=numpy.zeros([len(dValues), len(dValues)])
    for r in xrange(data.shape[0]):
        for c in xrange(data.shape[1]):
            updateMat(data, mat, r, c, 1, 1, dValues)
    return mat


def updateMat(M, coMat, r, c, stepR, stepC, vals):
    minR=max(0, r-stepR)
    maxR=min(M.shape[0], r+stepR+1)
    
    minC=max(0, c-stepC)
    maxC=min(M.shape[1], c+stepC+1)
    base=M[r,c];
    for x in xrange(minR, maxR):
        row=vals[base]
        for y in xrange(minC, maxC):
            if(x==r and y==c):
                continue
            else:
                col=vals[M[x,y]]
                coMat[row,col]+=1
    
