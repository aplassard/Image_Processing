#!/usr/bin/env python

import numpy as np
from string import *
from pybrain.structure import LinearLayer, SigmoidLayer, TanhLayer, SoftmaxLayer
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader
import numpy as np


def initialize(trainingfeatures,traininglabels,p=0.7):
    alldata = ClassificationDataSet(trainingfeatures.shape[1], 1, nb_classes=len(set(traininglabels)))
    for i in xrange(traininglabels[0]):
       	alldata.appendLinked(trainingfeatures[i] , traininglabels[i])
    trndata, tstdata = alldata.splitWithProportion( p )
    trndata._convertToOneOfMany(bounds=[0, 1])
    tstdata._convertToOneOfMany(bounds=[0, 1])
    model, accuracy, params = buildANN(trndata, tstdata)
    print '\nThe best model had '+str(accuracy)+'% accuracy and used the parameters:\n'+params+'\n'
    return model


def buildANN(trndata, tstdata):
    
    accuracy=0
    model = None
    params = None
    
    ann = buildNetwork( trndata.indim, (trndata.indim + trndata.outdim)/2, trndata.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)

    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Feedforward[Hidden Layer = TanhLayer; Hidden Layer Units= (Input+Output)Units/2; Output Layer = SoftmaxLayer]\n"    
    ann = buildNetwork( trndata.indim, trndata.indim, trndata.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)


    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Feedforward[Hidden Layer = TanhLayer; Hidden Layer Units = Input Units; Output Layer = SoftmaxLayer]\n"
    ann = buildNetwork( trndata.indim, (trndata.indim + trndata.outdim)/2, trndata.outdim, hiddenclass=TanhLayer, outclass=SigmoidLayer, bias='true' )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)


    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Feedforward[Hidden Layer = TanhLayer; Hidden Layer Units = (Input+Output)Units/2; Output Layer = SigmoidLayer]\n"
    ann = buildNetwork( trndata.indim, (trndata.indim + trndata.outdim)/2, trndata.outdim, hiddenclass=TanhLayer, outclass=SigmoidLayer, bias='true' )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)
    
    
    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Feedforward[Hidden Layer = TanhLayer; Hidden Layer Units = Input Units; Output Layer = SigmoidLayer]\n"
    ann = buildNetwork( trndata.indim, (trndata.indim + trndata.outdim)/2, (trndata.indim + trndata.outdim)/2, trndata.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)
    
    
    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Feedforward[TWO (2) Hidden Layers = TanhLayer; Hidden Layer Units = (Input+Output)Units/2; Output Layer = SoftmaxLayer]\n"
    ann = buildNetwork( trndata.indim, trndata.indim, trndata.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true', recurrent=True )
    trainer = BackpropTrainer(ann, dataset=trndata, momentum=0.1, verbose=False, weightdecay=0.01, learningrate=0.01)
    a=calculateANNaccuracy(ann, trndata, tstdata, trainer)
    
    if a>accuracy:
        model=ann
        accuracy=a
        params="network = Recurrent[Hidden Layer = TanhLayer; Hidden Layer Units = Input Units; Output Layer = SoftmaxLayer]\n"
        
    return model, accuracy, params

def calculateANNaccuracy(model, trndata, tstdata, trainer,iterations=20,maxEpochs=10):
    
    trn_sum=0
    tst_sum=0
    trnfinal=[]
    tstfinal=[]
           
    for i in range(iterations):

            trainer.trainUntilConvergence(maxEpochs=maxEpochs, continueEpochs=1)
            trnresult = percentError( trainer.testOnClassData(),
                              trndata['class'] )
            tstresult = percentError( trainer.testOnClassData(
           dataset=tstdata ), tstdata['class'] )
            trnres=100-trnresult
            tstres=100-tstresult
            trn_sum=trn_sum+trnres
            tst_sum=tst_sum+tstres
            trnfinal.append(trnres)
            tstfinal.append(tstres)
            
    trn_avg=trn_sum/(i+1)
    tst_avg=tst_sum/(i+1)
    print "Train average accuracy: %5.2f%%" % trn_avg
    print "Test average accuracy: %5.2f%%" % tst_avg

    print "Train SD = ", np.std(trnfinal)
    print "Test SD = ", np.std(tstfinal)
    print "\n"
    return tst_avg
    


def OutputClass(features):

    net = NetworkReader.readFrom('best_model.xml') # Reading the best model/network from the file it was saved
    output = net.activate(features)
    return output
 