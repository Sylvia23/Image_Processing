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
    img = cv2.imread("3.jpg", cv2.IMREAD_COLOR)
    
    # Output image
    imgOut = img.copy()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load HAAR cascade
    eyesCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    
    # Detect eyes
    eyes = eyesCascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(10, 10))
    
    # For every detected eye
    for (x, y, w, h) in eyes:

        # Extract eye from the image
        eye = img[y:y+h, x:x+w]

        # Split eye image into 3 channels
        b = eye[:, :, 0]
        g = eye[:, :, 1]
        r = eye[:, :, 2]
        
        # Add the green and blue channels.
        bg = cv2.add(b, g)

        # Simple red eye detector.
        mask = (r > 150) &  (r > bg)
        
        # Convert the mask to uint8 format.
        mask = mask.astype(np.uint8)*255

        # Clean mask -- 1) File holes 2) Dilate (expand) mask.
        mask = fillHoles(mask)
        mask = cv2.dilate(mask, None, anchor=(-1, -1), iterations=3, borderType=1, borderValue=1)

        # Calculate the mean channel by averaging
        # the green and blue channels
        mean = bg / 2
        mask = mask.astype(np.bool)[:, :, np.newaxis]
        mean = mean[:, :, np.newaxis]

        # Copy the eye from the original image.
        eyeOut = eye.copy()

        # Copy the mean image to the output image.
        #np.copyto(eyeOut, mean, where=mask)
        eyeOut = np.where(mask, mean, eyeOut)

        # Copy the fixed eye to the output image.
        imgOut[y:y+h, x:x+w, :] = eyeOut

        # put font on image
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, 'Eyes_Sylvia', (200,100), font, 4, (0, 0, 0), 4, cv2.LINE_8)

        # draw rectangle
        cv2.rectangle(img, (x,y), (x+w, y+h), (123, 200, 96), 10, lineType=8, shift=0)

        # draw circle
        color = (255, 0, 255)
        cv2.circle(img, (350, 350), 100, color)

        #save image in a different format
        #img = cv2.imwrite('diff.png', img)

    # Display Result
    b,g,r = cv2.split(img)
    img1 = cv2.merge((b,g,r))
    b1 = img[:,:,0]
    print img.shape
    print img.size
    print img.dtype
    cv2.namedWindow('Red Eyes', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Red Eyes Removed', cv2.WINDOW_NORMAL)
    cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
    cv2.namedWindow('blue', cv2.WINDOW_NORMAL)
    cv2.namedWindow('green', cv2.WINDOW_NORMAL)
    cv2.namedWindow('red', cv2.WINDOW_NORMAL)
    cv2.namedWindow('merged', cv2.WINDOW_NORMAL)
    cv2.namedWindow('nored', cv2.WINDOW_NORMAL)
    cv2.imshow('nored', b1)
    cv2.imshow('merged', img1)
    cv2.imshow('red', r)
    cv2.imshow('green', g)
    cv2.imshow('blue', b)
    cv2.imshow('Red Eyes', img)
    cv2.imshow('Red Eyes Removed', imgOut)
    cv2.imshow('gray', gray_image)
    cv2.waitKey(0)

    #cv2.destroyAllWindows()
