import sys

import cv2 # it is necessary to use cv2 library
import numpy as np
import math

def main( input_filename, output_filename ):
    src = cv2.imread( input_filename )  # load image from input_filename
    src = src.astype('float32')/255.0   # single [0,1]

    H = np.eye( 3, dtype=np.single )

    ############ Edit here ############

    # rotation
    rad = 45 * math.pi / 180
    h11=math.cos(rad);   h12=-math.sin(rad);   h13=10;
    h21=math.sin(rad);   h22= math.cos(rad);   h23=20;
    h31=0;   h32=0;

    _H = np.zeros( (3, 3), dtype=np.single )
    _H[0,0] = h11;   _H[0,1] = h12;   _H[0,2] = h13;
    _H[1,0] = h21;   _H[1,1] = h22;   _H[1,2] = h23;
    _H[2,0] = h31;   _H[2,1] = h32;   _H[2,2] = 1;

    H = np.dot( _H, H )

    # scale
    h11=0.5;   h12=0;   h13=0;
    h21=0;     h22=1;   h23=0;
    h31=0;     h32=0;

    _H = np.zeros( (3, 3), dtype=np.single )
    _H[0,0] = h11;   _H[0,1] = h12;   _H[0,2] = h13;
    _H[1,0] = h21;   _H[1,1] = h22;   _H[1,2] = h23;
    _H[2,0] = h31;   _H[2,1] = h32;   _H[2,2] = 1;

    H = np.dot( _H, H )

    # translation
    h11=1;   h12=0;   h13=320;
    h21=0;   h22=1;   h23=0;
    h31=0;   h32=0;

    _H = np.zeros( (3, 3), dtype=np.single )
    _H[0,0] = h11;   _H[0,1] = h12;   _H[0,2] = h13;
    _H[1,0] = h21;   _H[1,1] = h22;   _H[1,2] = h23;
    _H[2,0] = h31;   _H[2,1] = h32;   _H[2,2] = 1;

    H = np.dot( _H, H )

    ############ Edit here ############

    (h,w,c) = src.shape
    dst = cv2.warpPerspective(src, H, (w,h) )

    dst = (dst * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, dst ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
