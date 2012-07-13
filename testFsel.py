from common import *
import fSel, numpy, random
from sklearn import svm
from sklearn.svm import LinearSVC
reload(fSel)

def testData(data, labels, perc=0.7):
    '''
    Inputs: features, labels, percent for training
    output: trains an SVM on the data provided and on data after feature selection by
    4 methods and prints the error for each case    
    '''
    #without feature selection
    testX,testY, trainX, trainY=splitTrainingTesting(data, labels, perc)
    print "Testing without feature selection: "
    testThis(trainX, trainY, testX, testY)
    
    #with feature selection
    #univariate, chiSq, k=100
    print "\nTesting feature selection, chiSq, k=100: "
    data_new=fSel.getBestK(data,labels, 'chi2', 100)
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)
    testThis(trainX, trainY, testX, testY)
    #print "Old shape: ", data.shape, "new shape: ", data_new.shape
    #print trainX.shape, trainY.shape, testX.shape, testY.shape
    
    #univariate, f_classif, k=100
    print "\nTesting feature selection, f_classif, k=100: "
    data_new=fSel.getBestK(data,labels, 'f_classif', 100)   
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)    
    testThis(trainX, trainY, testX, testY)
    #print "Old shape: ", data.shape, "new shape: ", data_new.shape
    #print trainX.shape, trainY.shape, testX.shape, testY.shape
    
    #Tree based
    print "\nTesting feature selection, TreeBased: "
    data_new=fSel.getTreeFeatures(data,labels)
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)    
    testThis(trainX, trainY, testX, testY)
    #print "Old shape: ", data.shape, "new shape: ", data_new.shape
    #print trainX.shape, trainY.shape, testX.shape, testY.shape

    print "\nTesting feature selection, LinearSVC with L1 penalty: "
    data_new = LinearSVC(C=0.01, penalty="l1", dual=False).fit_transform(data, labels)
    testX,testY, trainX, trainY=splitTrainingTesting(data_new, labels, perc)
    testThis(trainX, trainY, testX, testY)    
    #print "Old shape: ", data.shape, "new shape: ", data_new.shape
    #print trainX.shape, trainY.shape, testX.shape, testY.shape

def testThis(trainX, trainY, testX, testY):
    '''
    Inputs: training features, training labels, testing features, testing labels
    Output: prints and returns classification accuracy
    '''
    testmodel = svm.SVC(C=10, gamma=0.1)
    testmodel.fit(trainX,trainY)
    p=calculateSVMerror(testmodel,testX,testY)
    print "accuracy: ", p
    return p
    
def calculateSVMerror(model,testfeatures,testlabels):
    n=0
    for i in xrange(testfeatures.shape[0]):
        a=model.predict(testfeatures[i,:])[0]
        if a==testlabels[i]:
            n+=1
    return float(n)/testfeatures.shape[0]
    
def splitTrainingTesting(arr,labels,percent=0.7):
    l=set(labels)
    l=list(l)
    traininglabels=[]
    testlabels=[]
    trainingfeatures=[]
    testfeatures=[]
    for i in xrange(len(l)):
        la=l[i]
        n=0
        templabels=[]
        tempfeatures=[]
        for j in xrange(len(labels)):
            if labels[j]==la:
                templabels.append(la)
                tempfeatures.append(list(arr[j,:]))
        g=random.sample(range(len(templabels)),int(percent*float(len(templabels))))
        for j in range(len(templabels)):
            if g.count(j)>0:
                trainingfeatures.append(tempfeatures[j])
                traininglabels.append(templabels[j])
            else:
                testfeatures.append(tempfeatures[j])
                testlabels.append(templabels[j])
    traininglabels=np.array(traininglabels).astype(float)
    testlabels=np.array(testlabels).astype(float)
    return np.array(testfeatures).astype(float),testlabels,np.array(trainingfeatures).astype(float),traininglabels