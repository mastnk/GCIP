import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( input_filename, output_filename ):

    src = cv2.imread( input_filename )  # load image from input_filename
    src = src.astype(np.float32)/255    # cast to float32


    blr1 = cv2.GaussianBlur( src, ksize=(13, 13), sigmaX=0.8, borderType=cv2.BORDER_REPLICATE )
    blr2 = cv2.GaussianBlur( src, ksize=(13, 13), sigmaX=3.0, borderType=cv2.BORDER_REPLICATE )

    DoG = blr1 - blr2
    dst = src + 2.0 * DoG

    dst = dst*255
    dst = dst.clip(0,255).astype( np.uint8 ) # cast to uint8, note that the clip is required before cast

    cv2.imwrite( output_filename, dst ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
