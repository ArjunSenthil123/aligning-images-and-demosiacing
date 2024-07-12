# This code is part of:
#
#   CMPSCI 370: Computer Vision, Spring 2023
#   University of Massachusetts, Amherst
#   Instructor: Subhransu Maji
#
#   Homework 2

import numpy as np
import matplotlib.pyplot as plt 

def mosaicImage(img):
    ''' Computes the mosaic of an image.

    mosaicImage computes the response of the image under a Bayer filter.

    Args:
        img: NxMx3 numpy array (image).

    Returns:
        NxM image where R, G, B channels are sampled according to RGRG in the
        top left.
    '''

    image_height, image_width, num_channels = img.shape
    assert(num_channels == 3) #Checks if it is a color image



    mosim = img[:, :, 1]
    
   
    h = img.shape[0]
    w = img.shape[1]
    for y in range(h):
        for x in range(w):
            if((y%2==0) and (x%2==0)):
                mosim[y,x] = img[y,x,0]
            if((y%2==1) and (x%2==1)):
                mosim[y,x] = img[y,x,2]
            
    return mosim

