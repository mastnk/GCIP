import sys

import cv2 # it is necessary to use cv2 library
import numpy as np


def main( input_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    print(type(img)) # class of img
    print(img.dtype) # data type of img
    print(img.shape) # (height, width, channel)
    print()

    fimg = img.astype('float32')/255.0
    print(type(fimg)) # class of img
    print(fimg.dtype) # data type of img
    print(fimg.shape) # (height, width, channel)
    print()

    np.save('fimg.npy', fimg)    # save as numpy array (not image format)
    fimg2 = np.load('fimg.npy')  # load numpy array
    print(type(fimg)) # class of img
    print(fimg.dtype) # data type of img
    print(fimg.shape) # (height, width, channel)
    print()

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 2 ):
        main( sys.argv[1] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname' )
