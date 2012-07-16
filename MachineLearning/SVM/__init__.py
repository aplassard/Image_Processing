#!/usr/bin/env python
from sklearn import svm, datasets,neighbors

def buildSVM(traininglabels,trainingfeatures,testlabels,testfeatures):
    percent=0
    model=None
    params=None
    testmodel = svm.LinearSVC(C=0.1)
    print traininglabels.shape,trainingfeatures.shape
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=0.1)'''
    testmodel = svm.LinearSVC(C=1.0)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=1.0)'''
    testmodel = svm.LinearSVC(C=5)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=5)'''
    testmodel = svm.LinearSVC(C=10)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=10)'''
    testmodel = svm.LinearSVC(C=20)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=20)'''
    testmodel = svm.LinearSVC(C=30)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=30)'''
    testmodel = svm.LinearSVC(C=40)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.LinearSVC(C=40)'''
    testmodel = svm.SVC(C=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1)'''
    testmodel = svm.SVC(C=1.0)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0)'''
    testmodel = svm.SVC(C=5)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5)'''
    testmodel = svm.SVC(C=10)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10)'''
    testmodel = svm.SVC(C=20)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20)'''
    testmodel = svm.SVC(C=30)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30)'''
    testmodel = svm.SVC(C=40)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40)'''
    testmodel = svm.SVC(C=0.1,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.0001)'''
    testmodel = svm.SVC(C=1.0,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.0001)'''
    testmodel = svm.SVC(C=5,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.0001)'''
    testmodel = svm.SVC(C=10,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.0001)'''
    testmodel = svm.SVC(C=20,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.0001)'''
    testmodel = svm.SVC(C=30,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.0001)'''
    testmodel = svm.SVC(C=40,gamma=0.0001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.0001)'''
    testmodel = svm.SVC(C=0.1,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.001)'''
    testmodel = svm.SVC(C=1.0,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.001)'''
    testmodel = svm.SVC(C=5,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.001)'''
    testmodel = svm.SVC(C=10,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.001)'''
    testmodel = svm.SVC(C=20,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.001)'''
    testmodel = svm.SVC(C=30,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.001)'''
    testmodel = svm.SVC(C=40,gamma=0.001)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.001)'''
    testmodel = svm.SVC(C=0.1,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.01)'''
    testmodel = svm.SVC(C=1.0,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.01)'''
    testmodel = svm.SVC(C=5,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.01)'''
    testmodel = svm.SVC(C=10,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.01)'''
    testmodel = svm.SVC(C=20,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.01)'''
    testmodel = svm.SVC(C=30,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.01)'''
    testmodel = svm.SVC(C=40,gamma=0.01)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.01)'''
        
    testmodel = svm.SVC(C=0.1,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,gamma=0.1)'''
    testmodel = svm.SVC(C=1.0,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,gamma=0.1)'''
    testmodel = svm.SVC(C=5,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,gamma=0.1)'''
    testmodel = svm.SVC(C=10,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,gamma=0.1)'''
    testmodel = svm.SVC(C=20,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,gamma=0.1)'''
    testmodel = svm.SVC(C=30,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,gamma=0.1)'''
    testmodel = svm.SVC(C=40,gamma=0.1)
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,gamma=0.1)'''
    
    testmodel = svm.SVC(C=0.1,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=0.1,kernel='linear')'''
    testmodel = svm.SVC(C=1.0,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=1.0,kernel='linear')'''
    testmodel = svm.SVC(C=5,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=5,kernel='linear')'''
    testmodel = svm.SVC(C=10,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=10,kernel='linear')'''
    testmodel = svm.SVC(C=20,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=20,kernel='linear')'''
    testmodel = svm.SVC(C=30,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=30,kernel='linear')'''
    testmodel = svm.SVC(C=40,kernel='linear')
    testmodel.fit(trainingfeatures,traininglabels)
    p=calculateSVMerror(testmodel,testfeatures,testlabels)

    if p>percent:
        model=testmodel
        percent=p
        params='''testmodel = svm.SVC(C=40,kernel='linear')'''
    print '\nThe best model had ' + str(percent*100) + '% success and used the parameters:\n' + params+'\n'
    return model


def calculateSVMerror(model,testfeatures,testlabels):
    n=0
    for i in xrange(testfeatures.shape[0]):
        a=model.predict(testfeatures[i,:])[0]
        if a==testlabels[i]:
            n+=1
    return float(n)/testfeatures.shape[0]