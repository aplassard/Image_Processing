from common import *
import sklearn, readFile, sys
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import f_classif, SelectKBest, chi2
from MachineLearning.mlFunctions import *

def getTreeFeatures(data, labels):
    '''
    Input: The entire dataset and list of labels
    Outout: Data in 2d numpy array format with irrelevant features removed using
    Tree-based feature selection
    '''
    X=data
    y=labels
    clf=ExtraTreesClassifier(compute_importances=True, random_state=0)
    X_new=clf.fit(X,y).transform(X)
    return X_new

def getBestK(X, y, mode='f_classif', K=10):
    '''
    Input: dataset, list of labels, mode of feature selection (chi2 or f_classif), and K
    Outout: Data in 2d numpy array format with top K features selected using the specified
    univariate feature selection method
    '''
    K=int(K)
    if (K>X.shape[1] ):
	K=(X.shape[1]/2)

    if mode=='chi2':
	Selector=SelectKBest(chi2, K)
	X_new=Selector.fit_transform(X, y)
    elif mode=='f_classif':
	Selector= SelectKBest(f_classif, K)
	X_new= Selector.fit_transform(X, y)

    sup=Selector.get_support()
    return sup

def getMask(data, labels, K=None):
    '''
    Inputs: features, labels, number of features desired (optional)
    Output: performs feature selection and returns boolean mask of useful features
    '''
    #Tree based feature selection to get K
    if K==None:
        data_new=getTreeFeatures(data,labels)
        newK=data_new.shape[1]
    else:
        newK=K
    #change f_classif to chi2 
    print "making mask with k=: ", newK
    mask=getBestK(data,labels, 'f_classif', newK)  

    return mask

def start(fName, K=None):
    '''
    inputFile, number of features to be selected, default is none
    '''
    X,y= readFile.loadFile(fName)
    getMask(X, y, K)

if __name__ == '__main__':
    '''
    inputFile, number of features to be selected, default is blank
    '''
    if int(sys.argv[2])==int(0):
        start(sys.argv[1], None)
    else:
        start(sys.argv[1], sys.argv[2])
