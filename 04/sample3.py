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

    ############ Edit here ############

    #If you want to use hsv, uncomment the next line
    #hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #If you want to use YCbCr, uncomment the next line
    #ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    sigma = 4
    ksize = int(sigma*3*2+1)
    enhance = 1.25
    smooth = 0.05


    (height, width, channel) = img.shape
    for c in range(channel):
        m1 = img[:,:,c]
        m2 = m1 * m1

        m1 = cv2.GaussianBlur( m1, ksize=(ksize, ksize), sigmaX=sigma, borderType=cv2.BORDER_REPLICATE )
        m2 = cv2.GaussianBlur( m2, ksize=(ksize, ksize), sigmaX=sigma, borderType=cv2.BORDER_REPLICATE )
        va = m2 - m1*m1

        dst = (img[:,:,c] - m1) * va / ( va + smooth*smooth) * enhance + m1
        img[:,:,c] = dst

    #If you want to use hsv, uncomment the next line
    #img = cv2.cvtColor(hsvwithinrange(hsv), cv2.COLOR_HSV2BGR)

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
