import cv2 # it is necessary to use cv2 library
from google.colab.patches import cv2_imshow # it is necessary to use cv2_imshow

import sys

def main( input_filename ):
    img = cv2.imread( input_filename )
    cv2_imshow( img )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 2 ):
        main( sys.argv[1] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname' )

