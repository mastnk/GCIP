import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( background, input_filename, output_filename ):
    # Read the input image
    bak = cv2.imread(background)
    img = cv2.imread(input_filename)

    dif = img - bak
    dif = np.sqrt( np.sum( dif * dif, axis=2 ) )
    msk = ( dif > 10 ).astype(np.uint8)*255

    kernel = np.ones((3,3),np.uint8)

    # opening
    msk = cv2.erode(msk, kernel,iterations = 1)
    msk = cv2.dilate(msk, kernel,iterations = 1)

    # closing
    msk = cv2.dilate(msk, kernel,iterations = 2)
    msk = cv2.erode(msk, kernel,iterations = 2)

    cv2.imwrite( output_filename, msk )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
    else:
        print( 'usage: python '+sys.argv[0]+' background input_filenname output_filename' )
