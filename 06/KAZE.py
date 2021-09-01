import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://docs.opencv.org/4.5.1/da/df5/tutorial_py_sift_intro.html
def main( query_filename, output_filename ):

    img = cv2.imread(query_filename)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Initiate KAZE detector
    kaze = cv2.KAZE_create()

    # find the keypoints and descriptors with SIFT
    kp, ds = kaze.detectAndCompute(gray,None)

#   result = cv2.drawKeypoints(gray, kp, img)
    result=cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imwrite( output_filename, result )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' query_filename output_filename' )
