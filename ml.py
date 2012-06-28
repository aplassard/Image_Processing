#!/usr/bin/env python

import milk
import numpy as np


def basidrunSVM(traininglabels,trainingfeatures,testfeatures):
    classifier=milk.defaultclassifier()
    model = classifier.train(trainingfeatures,traininglabels)
    labels=[]
    for i in range(testfeatures.shape[0]):
        labels.append(model.apply(testfeatures[i]))
    return labels

def buildSVMmodel(traininglabels,trainingfeatures):
    classifier=milk.defaultclassifier()
    model = classifier.train(trainingfeatures,traininglabels)
    return model

