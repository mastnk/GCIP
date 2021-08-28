import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

def hsvwithinrange( hsv ):
    h = hsv[:,:,0]

    while( np.count_nonzero( h > 360 ) > 0 ):
        h[h>360] -= 360

    while( np.count_nonzero( h < 0 ) > 0 ):
        h[h<0] += 360

    hsv[:,:,0] = h
    return hsv

def main( input_filename, output_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    img = img.astype('float32')/255.0   # single [0,1]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # H: [0,360]
    # S: [0,1]
    # V: [0,1]


    hsv[:,:,0] = hsv[:,:,0] + 60             #H
    hsv[:,:,1] = hsv[:,:,1] * 1.5            #S
    hsv[:,:,2] = np.power( hsv[:,:,2], 1/2 ) #V

    hsv = hsvwithinrange(hsv)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, img ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
