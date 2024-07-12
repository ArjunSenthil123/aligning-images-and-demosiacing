import numpy as np

import cv2
from matplotlib import pyplot as plt



def alignChannels(img, max_shift):
    
    imageR = img[:,:,0]
    imageG = img[:,:,1]
    imageB = img[:,:,2]
    
    h = img.shape[0]
    w = img.shape[1]

    nw = w - max_shift[0]*2 -1
    nh = h - max_shift[1]*2 -1

    minangleg = 100000
    minangleb = 100000
    gshiftx = 0
    gshifty = 0
    bshiftx = 0
    bshifty = 0
    imageR_mid = image_extract_region(imageR,15,15,nw,nh)
    for sy in range(-max_shift[0],max_shift[1]+1):
        for sx in range(-max_shift[0],max_shift[1]+1):
            imageG_mid = image_extract_region(imageG,15+sx,15+sy,nw,nh)
            imageB_mid = image_extract_region(imageB,15+sx,15+sy,nw,nh)

            angle_g = angle_between(imageR_mid,imageG_mid)
            if(angle_g<minangleg):
                gshifty = sy
                gshiftx = sx
                minangleg = angle_g

            angle_b = angle_between(imageR_mid,imageB_mid)
            if(angle_b<minangleb):
                bshifty = sy
                bshiftx = sx
                minangleb = angle_b

    fimage = np.zeros(img.shape)
    fimage[:,:,0] = imageR
    fimage[:,:,1] = np.roll(imageG,[-gshifty,-gshiftx],axis=[0,1])
    fimage[:,:,2] = np.roll(imageB,[-bshifty,-bshiftx],axis=[0,1])

    pred_shift = np.array([[gshiftx, gshifty], [bshiftx,bshifty]])
    return fimage, pred_shift



def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    x = v1.flatten()
    y = v2.flatten()
    v1_u = unit_vector(x)
    v2_u = unit_vector(y)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))




def image_extract_region(img,x_offs,y_offs,w,h):
    return img[y_offs:y_offs+h, x_offs:x_offs+w]