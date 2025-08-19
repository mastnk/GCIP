import sys

import cv2 # it is necessary to use cv2 library
import numpy as np
import math

def main( input_filename, output_filename ):
    input = cv2.imread( input_filename )  # load image from input_filename
    input = input.astype('float32')/255.0   # single [0,1]

    ############ Edit here ############
    (h,w,c) = input.shape

    # H1
    H1 = np.zeros( (3,3), dtype=np.single )
    H1[0,0] = 1; H1[0,1] = 0; H1[0,2] = -w/2;
    H1[1,0] = 0; H1[1,1] = 1; H1[1,2] = -h/2;
    H1[2,0] = 0; H1[2,1] = 0; H1[2,2] = 1;

    # H2
    H2 = np.zeros( (3,3), dtype=np.single )
    rad = 45 * math.pi / 180
    H2[0,0] = math.cos(rad); H2[0,1] =-math.sin(rad); H2[0,2] = 0;
    H2[1,0] = math.sin(rad); H2[1,1] = math.cos(rad); H2[1,2] = 0;
    H2[2,0] = 0; H2[2,1] = 0; H2[2,2] = 1;

    # H3
    H3 = np.zeros( (3,3), dtype=np.single )
    H3[0,0] = 1; H3[0,1] = 0; H3[0,2] = w/2;
    H3[1,0] = 0; H3[1,1] = 1; H3[1,2] = h/2;
    H3[2,0] = 0; H3[2,1] = 0; H3[2,2] = 1;
    ############ Edit here ############

    H = np.dot( H2,H1 )
    H = np.dot( H3,H ) # H = H3 * H2 * H1

    print(H)

    output = cv2.warpPerspective(input, H, (w,h) )

    output = (output * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, output ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
