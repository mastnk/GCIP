import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://docs.opencv.org/3.4/d4/d7d/tutorial_harris_detector.html
def cornerHarris(src_gray, thresh):
    max_thresh = 255
    # Detector parameters
    blockSize = 2
    apertureSize = 3
    k = 0.04

    # Detecting corners
    dst = cv2.cornerHarris(src_gray, blockSize, apertureSize, k)
    # Normalizing
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    dst_norm_scaled = cv2.convertScaleAbs(dst_norm)
    # Drawing a circle around corners
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i,j]) > thresh:
                cv2.circle(dst_norm_scaled, (j,i), 5, (0), 2)

    return dst_norm_scaled


def main( input_filename, output_filename ):
    src = cv2.imread( input_filename )
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    thresh = 100
    result = cornerHarris( src_gray, thresh )
    cv2.imwrite( output_filename, result )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
