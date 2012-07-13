import sklearn
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import f_classif, SelectKBest, chi2

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

def getBestK(X, y, mode='chi2', K=10):
    '''
    Input: dataset, list of labels, mode of feature selection (chi2 or f_classif), and K
    Outout: Data in 2d numpy array format with top K features selected using the specified
    univariate feature selection method
    '''
    if K>X.shape[0]:
	K=X.shape[0]/2
	
    if mode=='chi2':
	Selector=SelectKBest(chi2, K)
	X_new=Selector.fit_transform(X, y)
    elif mode=='f_classif':
	Selector= SelectKBest(f_classif, K)
	X_new= Selector.fit_transform(X, y)    
    return X_new