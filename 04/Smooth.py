import sys

import cv2 # it is necessary to use cv2 library
import numpy as np



def main( input_filename, output_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    img = img.astype('float32')/255.0   # single [0,1]

    ############ Edit here ############

    sigma = 2.5
    smooth = 0.025
    enhance = 1.1
    iteration = 2

    ############ Edit here ############

    ksize = int(np.ceil(sigma*3))*2+1

    (height, width, channel) = img.shape
    for c in range(channel):
        for i in range(iteration):
            m1 = img[:,:,c]

            Lm1 = cv2.GaussianBlur( m1, ksize=(ksize, ksize), sigmaX=sigma, borderType=cv2.BORDER_REPLICATE )
            m2 = m1 - Lm1
            m2 = m2 * m2;
            Lm2 = cv2.GaussianBlur( m2, ksize=(ksize, ksize), sigmaX=sigma, borderType=cv2.BORDER_REPLICATE )

            img[:,:,c] = (m1 - Lm1) * Lm2 / ( Lm2 + smooth*smooth) * enhance + Lm1

    img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, img ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
