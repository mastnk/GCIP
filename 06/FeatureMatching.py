import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://docs.opencv.org/4.5.2/dc/dc3/tutorial_py_matcher.html
def main( input_filename, query_filename, output_filename ):

    query = cv2.imread(query_filename, cv2.IMREAD_GRAYSCALE)
    input = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)


    # Initiate SIFT detector
    sift = cv2.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp_q, ds_q = sift.detectAndCompute(query,None)
    kp_i, ds_i = sift.detectAndCompute(input,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(ds_q,ds_i,k=2)

    # Apply ratio test
    k = 0.75 # threshold
    good = []
    for m,n in matches:
        if m.distance < k*n.distance:
            good.append([m])

    # cv.drawMatchesKnn expects list of lists as matches.
    result = cv2.drawMatchesKnn(query,kp_q, input,kp_i,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imwrite( output_filename, result )


if( __name__ == '__main__' ):
    if( len(sys.argv) >= 4 ):
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname query_filename output_filename' )
