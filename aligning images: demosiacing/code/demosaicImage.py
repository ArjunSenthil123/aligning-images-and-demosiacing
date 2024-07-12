# This code is part of:
#
#   CMPSCI 370: Computer Vision, Spring 2023
#   University of Massachusetts, Amherst
#   Instructor: Subhransu Maji
#
#   Homework 2

import numpy as np


def demosaicImage(image, method):
    ''' Demosaics image.

    Args:
        img: np.array of size NxM.
        method: demosaicing method (baseline or nn).

    Returns:
        Color image of size NxMx3 computed using method.
    '''

    if method.lower() == "baseline":
        return demosaicBaseline(image.copy())
    elif method.lower() == 'nn':
        return demosaicNN(image.copy()) # Implement this
    else:
        raise ValueError("method {} unkown.".format(method))


def demosaicBaseline(img):
    '''Baseline demosaicing.
    
    Replaces missing values with the mean of each color channel.
    
    Args:
        img: np.array of size NxM.

    Returns:
        Color image of sieze NxMx3 demosaiced using the baseline 
        algorithm.
    '''
    mos_img = np.tile(img[:, :, np.newaxis], [1, 1, 3])
    image_height, image_width = img.shape

    red_values = img[0:image_height:2, 0:image_width:2]
    mean_value = red_values.mean()
    mos_img[:, :, 0] = mean_value
    mos_img[0:image_height:2, 0:image_width:2, 0] = img[0:image_height:2, 0:image_width:2]

    blue_values = img[1:image_height:2, 1:image_width:2]
    mean_value = blue_values.mean()
    mos_img[:, :, 2] = mean_value
    mos_img[1:image_height:2, 1:image_width:2, 2] = img[1:image_height:2, 1:image_width:2]

    mask = np.ones((image_height, image_width))
    mask[0:image_height:2, 0:image_width:2] = -1
    mask[1:image_height:2, 1:image_width:2] = -1
    green_values = mos_img[mask > 0]
    mean_value = green_values.mean()

    green_channel = img
    green_channel[mask < 0] = mean_value
    mos_img[:, :, 1] = green_channel

    return mos_img


def demosaicNN(img):
    '''Nearest neighbor demosaicing.
    
    Args:
        img: np.array of size NxM.

    Returns:
        Color image of size NxMx3 demosaiced using the nearest neighbor 
        algorithm.
    '''

    nnimg = np.tile(img[:, :, np.newaxis], [1, 1, 3])

    h = img.shape[0]
    w = img.shape[1]
    for y in range(h):
        for x in range(w):
            if((y%2==0) and (x%2==0)): #even y, even x, keep red
                if(y==0):
                    nnimg[y,x,1] = img[y+1,x] #when at top take green from below
                    if(x==0):
                        nnimg[y,x,2] = img[y+1,x+1] #when at top left take blue from bottom right
                    if(x==(w-1)):
                        nnimg[y,x,2] = img[y+1,x-1] #when at top right take blue from bottom left
                else:
                    nnimg[y,x,1] = img[y-1,x] #take green from above
                    nnimg[y,x,2] = img[y-1,x-1] #take blue from above and left

            if((y%2==0) and (x%1==1)): #even y, odd x, keep green
                if(y==0):
                    nnimg[y,x,2] = img[y+1,x] #when at top take blue from below
                else:
                    nnimg[y,x,0] = img[y,x-1] #take red from left
                    nnimg[y,x,2] = img[y-1,x] #take blue from above

            if((y%2==1) and (x%2==0)): #odd y, even x, keep green
                if(x==0):
                    nnimg[y,x,2] = img[y,x+1] #when at leftmost, take blue from right
                else:
                    nnimg[y,x,0] = img[y-1,x] #take red from above
                    nnimg[y,x,2] = img[y,x-1] #take blue from left

            if((y%2==1) and (x%2==1)): #odd y, odd x, keep blue
                nnimg[y,x,0] = img[y-1,x-1] #take red from up 1, left 1
                nnimg[y,x,1] = img[y-1,x] #take green from above
            
            
    return nnimg
    #raise NotImplementedError("You should implement this.")

