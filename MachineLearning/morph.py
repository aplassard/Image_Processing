import numpy as np
from scipy.misc import imsave
def morph(imageArray, x=3, mode='erode'):
    size=x*x
    mask = np.ones([x,x]);
    mid=x/2
    width=imageArray.shape[1];
    height=imageArray.shape[0];
    imMask=np.zeros([height, width])
    for row in xrange(x, height-x):
        for col in xrange(x, width-x):
            subImage=imageArray[row-mid:row+mid, col-mid:col+mid].astype(float)
            if(mode== 'erode'):
                imMask[row,col]=subImage.min()
            else:
                imMask[row,col]=subImage.max()
    return imMask

def meh(img, l=1):
    '''
    pseudo edge detection
    '''
    mask=np.zeros_like(img)
    for x in xrange(img.shape[0]):
        for y in xrange(img.shape[1]):
            maxx=min(img.shape[0], x+l)
            maxy=min(img.shape[1], y+l)
            minx=max(0, x-l)
            miny=max(0, y-l)
            subImage=img[minx:maxx+1, miny:maxy+1]
            d=(subImage.shape[0]*subImage.shape[1])-1
            m=(subImage.sum()-img[x,y])/(d)
            #m=subImage.max()-1
            if m>img[x,y]:
                mask[x,y]=255
    return mask

def clean(img, l=1):
    mask=np.zeros_like(img)
    for x in xrange(img.shape[0]):
        for y in xrange(img.shape[1]):
            maxx=min(img.shape[0], x+l)
            maxy=min(img.shape[1], y+l)
            minx=max(0, x-l)
            miny=max(0, y-l)
            subImage=img[minx:maxx+1, miny:maxy+1]
            counts = np.bincount(subImage.ravel()).astype(float)
            if(counts.max()/counts.sum()>0.8):
                mask[x,y]=np.argmax(counts)
            else:
                mask[x,y]=img[x,y]
    return mask

def all(img, i):
    im1=meh(img)    
    print "saving base image "
    imsave("base-Edged.png", im1)
    im2=im1
    for p in xrange(0,i):
        im2=clean(im2)
        imsave("cleaned_Ver_"+str(p)+".png", im2)