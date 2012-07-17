import pylab
import numpy as np
from string import *
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer, TanhLayer, SoftmaxLayer
from pybrain.structure import FullConnection
from pybrain.datasets.classification import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.supervised.trainers import RPropMinusTrainer
#from pybrain.structure.modules import SoftmaxLayer
from pybrain.datasets.importance import ImportanceDataSet
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
from MachineLearning.mlFunctions import normalizearray
from pybrain.rl.environments.task import Task
import numpy as np
import fSel
from readFile import  loadFile
import sklearn



def start():
    featuresList=[]
    labelsList=[]
    featuresList, labelsList= loadFile("output.txt")

    print 'Normalizing array...'

    normalizearray(featuresList)
   
 
    alldata = ClassificationDataSet( len(featuresList[0]), 1, nb_classes=8, class_labels=['ffi_brainmatter','ffi_neuron','ffi_vacuole','ffi_astrocyte', 'wt_brainmatter', 'wt_neuron', 'wt_vacuole', 'wt_astrocyte'] )
    for i in range(len(labelsList)):
         alldata.appendLinked(featuresList[i], labelsList[i])
          
         
    #print 'All data: ', alldata
    #print 'Statisticcs: ', alldata.calculateStatistics()
    
    newK=fSel.getTreeFeatures(featuresList, labelsList);
    newK=newK.shape[1]
    print "K= ", newK
    reducedFeatures= fSel.getBestK(featuresList,labelsList, 'f_classif', newK)
    reducedData=ClassificationDataSet( len(reducedFeatures[0]), 1, nb_classes=8, class_labels=['ffi_brainmatter','ffi_neuron','ffi_vacuole','ffi_astrocyte', 'wt_brainmatter', 'wt_neuron', 'wt_vacuole', 'wt_astrocyte'] )
    
    #prep reducedData object with reduced feature list
    for i in range(len(labelsList)):
        reducedData.appendLinked(reducedFeatures[i], labelsList[i])
    
    
    print 'Splitting test and training data...'
    tstdata, trndata = alldata.splitWithProportion( 0.30 )
    reducedTestData, reducedTrainData=reducedData.splitWithProportion(0.3)
    
    print 'Number of training and test patterns: ', len(trndata), len(tstdata)
    
    
    trndata._convertToOneOfMany(bounds=[0,1])
    tstdata._convertToOneOfMany(bounds=[0,1])  
    
    reducedTestData._convertToOneOfMany(bounds=[0,1])
    reducedTrainData._convertToOneOfMany(bounds=[0,1])
    
    
    #print "Number of training patterns: ", len(trndata)
    print "Input and output dimensions: ", trndata.indim, trndata.outdim
    #print "Sample (input, target, class):"
    #print trndata['input'][0], trndata['target'][0], trndata['class'][0]
    #print trndata['input'][1], trndata['target'][1], trndata['class'][1]

    
    buildFNN(tstdata, trndata)
    
    print "___________________________________________FEATURE REDUCTION________________________________________________"
    buildFNN(reducedTestData, reducedTrainData)
        
    
def buildFNN(testData, trainData):
    '''
    Input: testing data object, training data object
    Output: Prints details of best FNN
    '''
        
    accuracy=0
    model = None
    params = None
    fnn = buildNetwork( trainData.indim, (trainData.indim + trainData.outdim)/2, trainData.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )    
    trainer = BackpropTrainer(fnn, dataset=trainData, momentum=0.1, verbose=False, weightdecay=0.01)        
    a=calculateANNaccuracy(fnn, trainData, testData, trainer)    
    if a>accuracy:
        model=fnn
        accuracy=a
        params='''network = [Hidden Layer = TanhLayer; Hidden Layer Units= (Input+Output)Units/2; Output Layer = SoftmaxLayer]\n'''
    
    fnn = buildNetwork( trainData.indim, trainData.indim, trainData.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )
    trainer = BackpropTrainer(fnn, dataset=trainData, momentum=0.1, verbose=False, weightdecay=0.01)
    a=calculateANNaccuracy(fnn, trainData, testData, trainer)
    if a>accuracy:
        model=fnn
        accuracy=a
        params='''network = [Hidden Layer = TanhLayer; Hidden Layer Units = Input Units; Output Layer = SoftmaxLayer]\n'''
    
        
    fnn = buildNetwork( trainData.indim, (trainData.indim + trainData.outdim)/2, trainData.outdim, hiddenclass=TanhLayer, outclass=SigmoidLayer, bias='true' )
    trainer = BackpropTrainer(fnn, dataset=trainData, momentum=0.1, verbose=False, weightdecay=0.01)
    a=calculateANNaccuracy(fnn, trainData, testData, trainer)
    if a>accuracy:
        model=fnn
        accuracy=a
        params='''network = [Hidden Layer = TanhLayer; Hidden Layer Units = (Input+Output)Units/2; Output Layer = SigmoidLayer]\n'''
    
        
    fnn = buildNetwork( trainData.indim, (trainData.indim + trainData.outdim)/2, trainData.outdim, hiddenclass=TanhLayer, outclass=SigmoidLayer, bias='true' )
    trainer = BackpropTrainer(fnn, dataset=trainData, momentum=0.1, verbose=False, weightdecay=0.01)
    a=calculateANNaccuracy(fnn, trainData, testData, trainer)
    if a>accuracy:
        model=fnn
        accuracy=a
        params='''network = [Hidden Layer = TanhLayer; Hidden Layer Units = Input Units; Output Layer = SigmoidLayer]\n'''
    
    fnn = buildNetwork( trainData.indim, (trainData.indim + trainData.outdim)/2, (trainData.indim + trainData.outdim)/2, trainData.outdim, hiddenclass=TanhLayer, outclass=SoftmaxLayer, bias='true' )
    trainer = BackpropTrainer(fnn, dataset=trainData, momentum=0.1, verbose=False, weightdecay=0.01)
    a=calculateANNaccuracy(fnn, trainData, testData, trainer)
    if a>accuracy:
        model=fnn
        accuracy=a
        params='''network = [TWO (2) Hidden Layers = TanhLayer; Hidden Layer Units = (Input+Output)Units/2; Output Layer = SoftmaxLayer]\n'''
    
        
    print '\nThe best model had '+str(accuracy)+'% accuracy and used the parameters:\n'+params+'\n'
    
    #trainer = RPropMinusTrainer(fnn, dataset=trndata, etaminus=0.5, etaplus=1.2, deltamin=9.9999999999999995e-07, deltamax=5.0, delta0=0.10000000000000001)
    
    #print fnn.activate(features[1])
    
def calculateANNaccuracy(model, trndata, tstdata, trainer):
    trn_sum=0
    tst_sum=0
    trnfinal=[]
    tstfinal=[]
    for i in range(20):
        trainer.trainUntilConvergence(maxEpochs=10, continueEpochs=3, validationProportion=0.30)
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
    '''
    print "Test average accuracy: %5.2f%%" % tst_avg

    print "Test SD = ", np.std(tstfinal)
    '''
    return tst_avg


