import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

def SubImg( x, y ):
    dif = x - y
    dif = np.sqrt( np.sum( dif * dif, axis=2 ) )
    msk = ( dif > 10 ).astype(np.uint8)*255

    kernel = np.ones((3,3),np.uint8)

    # opening
    msk = cv2.erode(msk, kernel,iterations = 1)
    msk = cv2.dilate(msk, kernel,iterations = 1)

    # closing
    msk = cv2.dilate(msk, kernel,iterations = 2)
    msk = cv2.erode(msk, kernel,iterations = 2)

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
