import numpy as np
import matplotlib.pyplot as plt 
from utils import *

def histogram(im):
    
   
    h = im.shape[0]
    w = im.shape[1]



    pdf = np.zeros((256))
    cdf = np.zeros((256))


    for y in range(h):
        for x in range(w):
            i = im[y,x]
            pdf[i] = pdf[i] + 1
    
   
    cdf[0] = pdf[0]
    for i in range(1, 256): 
        cdf[i] = cdf[i-1] + pdf[i]
    
   
    return (pdf,cdf)

def contraststretching(img):
    h = img.shape[0]
    w = img.shape[1]
    
    
    
    min = img.min()
    max = img.max()
    
    fimage = np.zeros(img.shape, dtype=int)
    for y in range(h):
        for x in range(w):
            fimage[y,x] = round(((img[y,x]-min)/(max-min))*255.0)

    return (fimage)


def gammacorrection(img,gamma = 2):

    h = img.shape[0]
    w = img.shape[1]
    
    
    
    min = img.min()
    max = img.max()
    
    fimage = np.zeros(img.shape, dtype=int)
    for y in range(h):
        for x in range(w):
            fimage[y,x] = round(((img[y,x]/255.0)**(1.0/(gamma)))*255.0)


    return(fimage)


def equilization(img):
    h = img.shape[0]
    w = img.shape[1]
    n = h*w
    pdf,cdf = histogram(img)
    mincdf = -1
    for i in range(len(cdf)):
        if(cdf[i]!=0):
            mincdf = cdf[i]
            break
    fimage = np.zeros(img.shape, dtype=int)
    for y in range(h):
        for x in range(w):
            fimage[y,x] = round((((cdf[img[y,x]])-mincdf)/(n-mincdf))*255)

    return fimage


imgname = 'forest.png'
data_dir = os.path.join('..', 'data', 'contrast')
imgpath = os.path.join(data_dir, imgname)
gt = imread(imgpath)
gt = (gt * 255).astype("int")


pdf,cdf = histogram(gt)

plt.figure(1)
plt.subplot(121)
plt.bar(np.arange(0,256),pdf)
plt.title('pdf')
plt.xlabel('intensity')
plt.ylabel('count')
plt.subplot(122)
plt.plot(cdf, 'r+')

plt.xlabel('intensity')
plt.ylabel('cumulative count')
plt.title('cdf')
  


plt.figure(2)
gt_stretch = contraststretching(gt)
plt.subplot(121)
plt.title('original')
plt.imshow(gt,cmap = 'gray', vmin = 0, vmax = 255)
plt.subplot(122)
plt.title('contrast stretched')
plt.imshow(gt_stretch, cmap = 'gray',vmin=0, vmax=255)


plt.figure(3)
gt_gamma = gammacorrection(gt,2)
plt.subplot(121)
plt.title('original')
plt.imshow(gt,cmap = 'gray', vmin = 0, vmax = 255)
plt.subplot(122)
plt.title('gamma corrected (2)')
plt.imshow(gt_gamma, cmap = 'gray',vmin=0, vmax=255)

plt.figure(4)
gt_gamma2 = gammacorrection(gt,1/2)
plt.subplot(121)
plt.title('original')
plt.imshow(gt,cmap = 'gray', vmin = 0, vmax = 255)
plt.subplot(122)
plt.title('gamma corrected (1/2)')
plt.imshow(gt_gamma2, cmap = 'gray',vmin=0, vmax=255)

plt.figure(5)
pdf,cdf = histogram(gt_stretch)


plt.subplot(121)
plt.bar(np.arange(0,256),pdf)
plt.title('pdf contrast stretched')
plt.xlabel('intensity')
plt.ylabel('count')
plt.subplot(122)
plt.plot(cdf, 'r+')

plt.xlabel('intensity')
plt.ylabel('cumulative count')
plt.title('cdf contrast stretched')

plt.figure(6)
pdf,cdf = histogram(gt_gamma)

plt.subplot(121)
plt.bar(np.arange(0,256),pdf)
plt.title('pdf gamma corrected(2)')
plt.xlabel('intensity')
plt.ylabel('count')
plt.subplot(122)
plt.plot(cdf, 'r+')

plt.xlabel('intensity')
plt.ylabel('cumulative count')
plt.title('cdf gamma corrected(2)')

plt.figure(7)
pdf,cdf = histogram(gt_gamma2)

plt.subplot(121)
plt.bar(np.arange(0,256),pdf)
plt.title('pdf gamma corrected(1/2)')
plt.xlabel('intensity')
plt.ylabel('count')
plt.subplot(122)
plt.plot(cdf, 'r+')

plt.xlabel('intensity')
plt.ylabel('cumulative count')
plt.title('cdf gamma corrected(1/2)')

plt.figure(8)
gt_equal = equilization(gt)
plt.subplot(121)
plt.title('original')
plt.imshow(gt,cmap = 'gray', vmin = 0, vmax = 255)
plt.subplot(122)
plt.title('equalized')
plt.imshow(gt_equal, cmap = 'gray',vmin=0, vmax=255)

plt.figure(9)
pdf,cdf = histogram(gt_equal)

plt.subplot(121)
plt.bar(np.arange(0,256),pdf)
plt.title('pdf equalized')
plt.xlabel('intensity')
plt.ylabel('count')
plt.subplot(122)
plt.plot(cdf, 'r+')

plt.xlabel('intensity')
plt.ylabel('cumulative count')
plt.title('cdf equalized')

plt.show()