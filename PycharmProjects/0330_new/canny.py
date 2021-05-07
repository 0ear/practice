import numpy as np
import cv2,os
from skimage import io
def diplayIMG(img, windowName):
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, 400, 300)
    cv2.imshow(windowName, img)
image = cv2.imread('../img/houses.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', image)
for i in range(0,255,50):
    canny = cv2.Canny(image, i ,255)
    displayIMG(canny, 'canny'+str(i))
cv2.waitKey()