from common import *
import fSel, numpy, random
from sklearn import svm
from sklearn.svm import LinearSVC
from MachineLearning.SVM import *
from MachineLearning.mlFunctions import *
import readFile, sys

reload(fSel)

def testData(data, labels, perc=0.7, K=None):
    '''
    Inputs: features, labels, percent for training
    output: trains an SVM on the data provided and on data after feature selection by
    4 methods and prints the error for each case    
    '''
    
    #without feature selection
    testX,testY, trainX, trainY=splitTrainingTesting(data, labels, perc)
    print "Testing without feature selection: "
    #buildSVM(trainY, trainX, testY, testX)    

    #Tree based
    print "\nTesting feature selection, TreeBased: "
    data_new=fSel.getTreeFeatures(data,labels)
    #testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)
    if K==None:
        newK=data_new.shape[1]
    else:
        newK=K
    #newK=17
    print "new K ", newK
    #buildSVM(trainY, trainX, testY, testX)    
    
    #with feature selection
    #univariate, chiSq, k=100
    print "\nTesting feature selection, chiSq, k=", newK
    data_new=fSel.getBestK(data,labels, 'chi2', newK)
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)
    #buildSVM(trainY, trainX, testY, testX)    

    #univariate, f_classif, k=100
    print "\nTesting feature selection, f_classif, k=", newK
    data_new=fSel.getBestK(data,labels, 'f_classif', newK)   
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)    
    buildSVM(trainY, trainX, testY, testX)    

    print "\nTesting feature selection, LinearSVC with L1 penalty: "
    data_new = LinearSVC(C=0.01, penalty="l1", dual=False).fit_transform(data, labels)
    print "reduced to: ", data_new.shape
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)
    buildSVM(trainY, trainX, testY, testX)    
    
def start(fName, K=None):
    '''
    inputFile, number of features to be selected, default is none
    '''
    X,y= readFile.loadFile(fName)
    testData(X, y, 0.7, K)

if __name__ == '__main__':
    '''
    inputFile, number of features to be selected, default is blank
    '''
    start(sys.argv[1], sys.argv[2])