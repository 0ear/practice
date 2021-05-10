import numpy as np
import cv2
def image_negative(f):
    g = 255-f
    return g
img1 = cv2.imread('Lenna.bmp')
img2 = image_negative(img1)
cv2.imshow('Original', img1)
cv2.imshow('Negative', img2)
cv2.waitKey(0)