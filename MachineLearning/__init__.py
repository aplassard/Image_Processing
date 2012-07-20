#!/usr/bin/env python
from common import *
from ml import *


if __name__ == '__main__':
    f = open('output.txt','r')
    labels = []
    features = []
    for line in f:
        line = line.strip().split(tab)
        labels.append(line[0])
        features.append(line[1:])
        
    features = np.array(features)
    ML=ml(features,labels)
    print ml.getSVMClass(features[1])