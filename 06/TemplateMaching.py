import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://docs.opencv.org/4.5.2/d4/dc6/tutorial_py_template_matching.html
def main( input_filename, template_filename ):

    img = cv2.imread(input_filename,0)
    template = cv2.imread(template_filename,0)
    w, h = template.shape[::-1]

    # chose a method
    # https://docs.opencv.org/4.5.2/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d
    method = 'TM_SQDIFF'       #SSD
#   method = 'TM_SQDIFF_NORMED'#Normalized SSD
#   method = 'TM_CCORR_NORMED' #NCC
#   method = 'TM_CCOEFF_NORMED'#ZNCC


    # Apply template Matching
    res = cv2.matchTemplate(img,template,eval('cv2.'+method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in ['TM_SQDIFF', 'TM_SQDIFF_NORMED']:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    cv2.imwrite( method+'_img.png', img )

    res = res / np.max(res) * 255
    res = res.clip(0,255).astype('uint8')
    cv2.imwrite( method+'_res.png', res )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname template_filename' )
