import sys

import cv2 # it is necessary to use cv2 library
import numpy as np
import math

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

    ############ Edit here ############

    #If you want to use hsv, uncomment the next line
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #If you want to use YCbCr, uncomment the next line
    #ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    (height, width, channel) = img.shape

    r = (height+width)/8
    for h in range(height):
        y = height/2-h
        for w in range(width):
            x = w-width/2

            hsv[h,w,1] = w/width

            #hsv[h,w,1] = (x/(width/2))*(x/(width/2)) + (y/(height/2))*(y/(height/2))

            ##
            ##
            #if( x*x + y*y > r*r ):
            #    a = 1-(x*x+y*y-r*r)/(r*r)
            #    if( a < 0 ):
            #        a = 0
            #    hsv[h,w,1] *= a


    #If you want to use hsv, uncomment the next line
    img = cv2.cvtColor(hsvwithinrange(hsv), cv2.COLOR_HSV2BGR)

    #If you want to use YCbCr, uncomment the next line
    #img = cv2.cvtColor(ycc, cv2.COLOR_YCrCb2BGR)

    ############ Edit here ############

    img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
    cv2.imwrite( output_filename, img ) # save image to output_filename

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
