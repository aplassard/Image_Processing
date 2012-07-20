#!/usr/bin/env python
from sklearn import svm, datasets,neighbors

def buildSVM(traininglabels,trainingfeatures,testlabels,testfeatures):
    percent=0
    model=None
    params=None
    testModel=None
    setC=[0.1,1,5,10,20,30,40]
    for c in setC:
        testmodel = svm.LinearSVC(C=c)        
        testmodel.fit(trainingfeatures,traininglabels)
        p=calculateSVMerror(testmodel,testfeatures,testlabels)
        print "testing LinearSVC with C=", str(c)
        if(p>percent):
            model=testmodel
            percent=p
            params="testModel= LinearSVC with C="+str(c)
    
    for c in setC:
        testmodel = svm.SVC(C=c)        
        testmodel.fit(trainingfeatures,traininglabels)
        p=calculateSVMerror(testmodel,testfeatures,testlabels)
        print "testing SVC with C=", str(c)
        if(p>percent):
            model=testmodel
            percent=p
            params="testModel= SVC with C="+str(c)

    setGamma=[0.0001, 0.001, 0.01, 0.1, 1]
    for c in setC:
        for g in setGamma:
            print "testing SVC with C= ", str(c), " and gamma=", str(g)
            testmodel = svm.SVC(C=c)        
            testmodel.fit(trainingfeatures,traininglabels)
            p=calculateSVMerror(testmodel,testfeatures,testlabels)
            if(p>percent):
                model=testmodel
                percent=p
                params="testModel= SVC with C= "+str(c)+" gamma= "+str(g)
    
    for c in setC:
        testmodel = svm.SVC(C=c, kernel='linear')
        testmodel.fit(trainingfeatures,traininglabels)
        p=calculateSVMerror(testmodel,testfeatures,testlabels)
        print "testing SVC linear kernel with C=", str(c)
        if(p>percent):
            model=testmodel
            percent=p
            params="testModel= SVC with kernel = Linear, C="+str(c)

    print '\nThe best model had ' + str(percent*100) + '% success and used the parameters:\n' + params+'\n'
    return model


def calculateSVMerror(model,testfeatures,testlabels):
    n=0
    for i in xrange(testfeatures.shape[0]):
        a=model.predict(testfeatures[i,:])[0]
        if a==testlabels[i]:
            n+=1
    return float(n)/testfeatures.shape[0]
