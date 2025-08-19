import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

def main( input_filename, output_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    img = img.astype('float32')/255.0   # single [0,1]

    ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    # ycc[:,:,0] : Y
    # ycc[:,:,1] : Cr
    # ycc[:,:,2] : Cb

    Y_gain = 1.2
    Cr_gain = 0.5
    Cb_gain = 1.5

    ycc[:,:,0] = ycc[:,:,0] * Y_gain
    ycc[:,:,1] = ycc[:,:,1] * Cr_gain
    ycc[:,:,2] = ycc[:,:,2] * Cb_gain

    img = cv2.cvtColor(ycc, cv2.COLOR_YCrCb2BGR)

    img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, img ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
