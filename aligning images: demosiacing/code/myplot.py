import numpy as np
import matplotlib.pyplot as plt 
from utils import *

def plotrgbshift1(img,c):
    
    color = 'x+'
    if(c == 'r'):
        color = 'r+'
    if(c == 'g'):
        color = 'g+'
    if(c == 'b'):
        color = 'b+'

    h = img.shape[0]
    w = img.shape[1]
   
    
    a1 = np.array(img)
    a2 = np.array(a1)
    

    for y in range(h):
        for x in range(w):
            if(x%(w-1)==0):
                a2[y,x] = a1[y,x]
            else:
                a2[y,x] = a1[y,x+1]

    a1 = a1.flatten()
    a2 = a2.flatten()
    # Create a line plot of the arrays
    plt.plot(a1, a2, color)
    # Add labels and title to the plot
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Line plot of x and y for ' + c)
    plt.plot(np.unique(a1), np.poly1d(np.polyfit(a1, a2, 1))(np.unique(a1)))

    # Show the plot
    plt.show()

imgname = 'puppy.jpg'
data_dir = os.path.join('..', 'data', 'demosaic')
imgpath = os.path.join(data_dir, imgname)
gt = imread(imgpath)
imageR = gt[:,:,0]
imageG = gt[:,:,0]
imageB = gt[:,:,0]
plotrgbshift1(imageR,'r')
plotrgbshift1(imageG,'g')
plotrgbshift1(imageB,'b')


