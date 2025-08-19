import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( background, input_filename, output_filename ):
    # Read the input image
    bak = cv2.imread(background)
    img = cv2.imread(input_filename)

    threshold = 10

    o_kernel_size = 3
    c_kernel_size = 3

    o_iterations = 1
    c_iterations = 2

    o_kernel = np.ones((o_kernel_size,o_kernel_size),np.uint8)
    c_kernel = np.ones((c_kernel_size,c_kernel_size),np.uint8)

    dif = img - bak
    dif = np.sqrt( np.sum( dif * dif, axis=2 ) )
    msk = ( dif > threshold ).astype(np.uint8)*255

    # opening
    msk = cv2.erode(msk, o_kernel,iterations = o_iterations)
    msk = cv2.dilate(msk, o_kernel,iterations = o_iterations)

    # closing
    msk = cv2.dilate(msk, c_kernel,iterations = c_iterations)
    msk = cv2.erode(msk, c_kernel,iterations = c_iterations)

    cv2.imwrite( output_filename, msk )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
    else:
        print( 'usage: python '+sys.argv[0]+' background input_filenname output_filename' )
