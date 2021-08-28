import sys

import cv2 # it is necessary to use cv2 library
import numpy as np

import math

hsv = np.zeros( (641,641,3), dtype = np.single )
hsv[:,:,1] = 0
hsv[:,:,2] = 1

(height, width, channel) = hsv.shape

for h in range(height):
    y = 320-h
    for w in range(width):
        x = w-320

        L = math.sqrt( x*x+y*y )

        if( L > 260 and L < 320 ):
            R = math.atan2( y, x ) * 180 / math.pi

            while( R > 360 ):
                R -= 360
            while( R < 0 ):
                R += 360

            hsv[h,w,0] = R
            hsv[h,w,1] = 1

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
cv2.imwrite( 'ColorWheel.png', img )



hsv = np.zeros( (200,360,3), dtype = np.single )
hsv[:,:,2] = 1

(height, width, channel) = hsv.shape

for h in range(height):
    y = (200-h)/200
    for w in range(width):
        x = w

        hsv[h,w,0] = x
        hsv[h,w,1] = y

img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
img = (img * 255).clip( 0, 255 ).astype('uint8') # uint8 [0,255]
cv2.imwrite( 'HS.png', img )
