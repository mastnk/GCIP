import sys

import cv2 # it is necessary to use cv2 library


def main( input_filename, output_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    print( img.shape )

    (H0, W0, C) = img.shape

    if( H0 < W0 ):
        W1 = 640
        H1 = int( H0 * W1 / W0 )
    else:
        H1 = 640
        W1 = int( W1 * H1 / H0 )

    img = cv2.resize( img, (W1, H1) ) # note that order of size should be (WIDTH, HEIGHT)

    cv2.imwrite( output_filename, img ) # save image to output_filename
    print( img.shape )


if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
