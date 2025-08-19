import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

def SubImg( x, y ):
    threshold = 10

    o_kernel_size = 3
    c_kernel_size = 3

    o_iterations = 1
    c_iterations = 2

    o_kernel = np.ones((o_kernel_size,o_kernel_size),np.uint8)
    c_kernel = np.ones((c_kernel_size,c_kernel_size),np.uint8)

    dif = x - y
    dif = np.sqrt( np.sum( dif * dif, axis=2 ) )
    msk = ( dif > threshold ).astype(np.uint8)*255

    # opening
    msk = cv2.erode(msk, o_kernel,iterations = o_iterations)
    msk = cv2.dilate(msk, o_kernel,iterations = o_iterations)

    # closing
    msk = cv2.dilate(msk, c_kernel,iterations = c_iterations)
    msk = cv2.erode(msk, c_kernel,iterations = c_iterations)
    return msk

def main( frame0, frame1, frame2, output_filename ):
    # Read the input image
    f0 = cv2.imread(frame0)
    f1 = cv2.imread(frame1)
    f2 = cv2.imread(frame2)

    s01 = SubImg( f0, f1 ).astype(np.single)/255
    s12 = SubImg( f1, f2 ).astype(np.single)/255

    msk = s01 * s12

    msk = (msk*255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, msk )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 4 ):
        main( sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] )
    else:
        print( 'usage: python '+sys.argv[0]+' frame0 frame1 frame2 output_filename' )
