from process_image import *

def iterTreshold(arr):
    for i in range(len(arr)):
        r=arr[i].shape[0]
        c=arr[i].shape[1]
        for j in xrange(255/5):
            o=zeros((r,c))
            for k in xrange(r):
                for l in xrange(c):
                    if arr[i][k][l]>j*5:
                              o[k][l]=255
                    else:
                              o[k][l]=0
            imsave(str(i)+"_"+str(j*5)+".tif",o)
