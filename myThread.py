import threading

class testImageThread (threading.Thread):    
    def __init__(self, threadID, name, imageArray, limits, featureList, window, slide):
        self.imgArr= imageArray
        self.limits=limits
        self.featureList=featureList
        self.window=window
        self.slide=slide
        self.cf= calculateFeatures(featuresList)
        self.result=numpy.zeros([])
    
    def run(self):
        self.walkImage()
        
    def walkImage():
        '''
        input: input image, window size in pixels, slide in pixels
        output: saves calculated features to instance variable "result"
        '''
        for startX in xrange(imgArr.shape[0]):
            endX=startX+self.window
            for startY in xrange(imgArr.shape[1]):
                endY=startY+window
                subImage= imgArr[startX:endX, startY:endY, :]
                result.append(cf.getFeatures(subImage))