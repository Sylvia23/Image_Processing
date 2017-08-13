'''
    Copyright 2017 by Satya Mallick ( Big Vision LLC )
    http://www.learnopencv.com
'''

import cv2
import numpy as np


def fillHoles(mask):
    '''
        This hole filling algorithm is decribed in this post
        https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
    '''
    maskFloodfill = mask.copy()
    h, w = maskFloodfill.shape[:2]
    maskTemp = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(maskFloodfill, maskTemp, (0, 0), 255)
    mask2 = cv2.bitwise_not(maskFloodfill)
    return mask2 | mask

if __name__ == '__main__' :

    # Read image
    img = cv2.imread("11.jpg", cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Output image
    imgOut = img.copy()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load HAAR cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    eyesCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    
    # Detect eyes
    eyes = eyesCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10))

    # Detect face
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(50, 50))

    # For every detected face
    for (x, y, w, h) in faces:
        # draw rectangle
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 96), 2, lineType=8, shift=0)
    
    # For every detected eye
    for (x, y, w, h) in eyes:
        # draw rectangle
        cv2.rectangle(img, (x,y), (x+w, y+h), (123, 200, 96), 2, lineType=8, shift=0)

    # Display Result
    
    print img.shape
    print img.size
    print img.dtype

    cv2.namedWindow('Before', cv2.WINDOW_NORMAL)
    cv2.namedWindow('After Detection', cv2.WINDOW_NORMAL)
    cv2.imshow('Before', imgOut)
    cv2.imshow('After Detection', img)
    cv2.waitKey(0)

    #cv2.destroyAllWindows()
