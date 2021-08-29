import sys
import os

import cv2 # it is necessary to use cv2 library
import numpy as np

# https://techacademy.jp/magazine/22808
import urllib.request
def wget( url, filename ):
    with urllib.request.urlopen(url) as u:
      with open(filename, 'bw') as o:
        o.write(u.read())

# https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
# https://docs.opencv.org/4.5.1/db/d28/tutorial_cascade_classifier.html
def main( input_filename, output_filename ):

    # obtain model file
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/'

    face_model = 'haarcascade_frontalface_default.xml'
#   face_model = 'haarcascade_frontalface_alt.xml'
    if( not os.path.isfile( face_model ) ):
        wget( url+face_model, face_model )

    eyes_model = 'haarcascade_eye_tree_eyeglasses.xml'
    if( not os.path.isfile( eyes_model ) ):
        wget( url+eyes_model, eyes_model )

    face_cascade = cv2.CascadeClassifier(face_model)
    eyes_cascade = cv2.CascadeClassifier(eyes_model)

    # Read the input image
    img = cv2.imread(input_filename)
    # Convert into grayscale
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    threshold = 4 # threshold should be integer
    faces = face_cascade.detectMultiScale(gry, 1.1, threshold)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        faceROI = gry[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(img, eye_center, radius, (255, 0, 255), 2)

    cv2.imwrite( output_filename, img )

if( __name__ == '__main__' ):
    if( len(sys.argv) >= 3 ):
        main( sys.argv[1], sys.argv[2] )
    else:
        print( 'usage: python '+sys.argv[0]+' input_filenname output_filename' )
