import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( input_filename, output_filename ):

    ker = np.array( [ [-1,-2,-1],
                      [ 0, 0, 0],
                      [+1,+2,+1]], dtype=np.float32 )

    src = cv2.imread( input_filename )  # load image from input_filename
    src = src.astype(np.float32)/255    # cast to float32

    dst = cv2.filter2D( src, -1, ker, borderType=cv2.BORDER_REPLICATE )

    val_max = np.max( np.abs( dst ) )
    dst = dst/val_max * 127 + 127
    dst = dst.clip(0,255).astype( np.uint8 ) # cast to uint8, note that the clip is required before cast

    cv2.imwrite( output_filename, dst ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
