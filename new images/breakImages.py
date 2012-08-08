from scipy.misc import imread, imsave

def start(path):
    dirList=os.listdir(path)
    for fname in dirList:
        if(fname.find(".tif")):
            breakImage(fname)
    
def breakImage(fileName):
    img=imread(fileName)
    w=img.shape[1]
    h=img.shape[0]
    stepW=w/4
    stepH=h/4
    counter=1
    for x in xrange(0, w, stepW):
        for y in xrange(0, h, stepH):
            subImage=img[x:x:stepW, y:y+stepH, :]
            newName=str(counter)+"-"+fileName;
            imsave(newName, subImage)
            

if __name__ == '__main__':
    start(sys.argv[1])