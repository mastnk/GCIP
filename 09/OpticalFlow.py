import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://stackoverflow.com/questions/20064818/how-to-draw-optical-flow-images-from-oclpyrlkopticalflowdense
def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
#    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    vis = img.copy()
    cv2.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (x2, y2) in lines:
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis

# https://code-graffiti.com/opencv-dense-optical-flow-in-python/
def main( frame0, frame1, output_filename ):
    # Read the input image
    f0 = cv2.imread(frame0)
    f1 = cv2.imread(frame1)

    gf0 = cv2.cvtColor(f0,cv2.COLOR_BGR2GRAY)
    gf1 = cv2.cvtColor(f1,cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(gf0, gf1, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    img = draw_flow( f0, flow )
    cv2.imwrite( output_filename, img )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2], sys.argv[3] )
    else:
        print( 'usage: python '+sys.argv[0]+' frame0 frame1 output_filename' )
