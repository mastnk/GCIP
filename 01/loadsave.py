import sys
import cv2 # it is necessary to use cv2 library


def main( input_filename, output_filename ):
    img = cv2.imread( input_filename )  # load image from input_filename
    cv2.imwrite( output_filename, img ) # save image to output_filename


if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
