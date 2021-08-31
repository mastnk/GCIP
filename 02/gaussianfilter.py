import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( input_filename, output_filename ):
    src = cv2.imread( input_filename )  # load image from input_filename

    dst = cv2.GaussianBlur( src, ksize=(9, 9), sigmaX=2.0, borderType=cv2.BORDER_REPLICATE )

    cv2.imwrite( output_filename, dst ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
