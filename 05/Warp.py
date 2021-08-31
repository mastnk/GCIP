import sys

import cv2 # it is necessary to use cv2 library
import numpy as np
import math

def main( input_filename, output_filename ):
    src = cv2.imread( input_filename )  # load image from input_filename
    src = src.astype('float32')/255.0   # single [0,1]


    ############ Edit here ############
    dst_width = 640
    dst_height = 640


    xsrc1 = 153; ysrc1 = 274;
    xdst1 =   0; ydst1 =   0;

    xsrc2 = 733; ysrc2 = 228;
    xdst2 = 640; ydst2 =   0;

    xsrc3 = 940; ysrc3 = 767;
    xdst3 = 640; ydst3 = 640;

    xsrc4 = 189; ysrc4 = 897;
    xdst4 =   0; ydst4 = 640;

    A = np.zeros( (8,8), dtype=np.single )
    b = np.zeros( (8,1), dtype=np.single )

    xs = [xsrc1, xsrc2, xsrc3, xsrc4]
    ys = [ysrc1, ysrc2, ysrc3, ysrc4]
    xd = [xdst1, xdst2, xdst3, xdst4]
    yd = [ydst1, ydst2, ydst3, ydst4]

    for i in range(4):
        A[2*i,0] = xs[i]; A[2*i,1] = ys[i]; A[2*i,2] = 1;
        A[2*i,6] = -xd[i]*xs[i]; A[2*i,7] = -xd[i]*ys[i];
        b[2*i] = xd[i]

        A[2*i+1,3] = xs[i]; A[2*i+1,4] = ys[i]; A[2*i+1,5] = 1;
        A[2*i+1,6] = -yd[i]*xs[i]; A[2*i+1,7] = -yd[i]*ys[i];
        b[2*i+1] = yd[i]

    h = np.dot( np.linalg.inv( np.dot(A.transpose(),A) ), np.dot( A.transpose(), b ) )
    H = np.zeros( (3,3), dtype = np.single )

    H[0,0] = h[0]
    H[0,1] = h[1]
    H[0,2] = h[2]

    H[1,0] = h[3]
    H[1,1] = h[4]
    H[1,2] = h[5]

    H[2,0] = h[6]
    H[2,1] = h[7]
    H[2,2] = 1

    print( H )

    ############ Edit here ############

    dst = cv2.warpPerspective(src, H, (dst_width,dst_height) )

    dst = (dst * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, dst ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
