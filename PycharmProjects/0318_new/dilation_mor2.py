import numpy as np
import cv2
#img = cv2.imread('../img/mor2.png')
img = cv2.imread('../img/cat.jpg')
print(img)
print('shape:', img.shape)
cv2.imshow('img0', img)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
img1 = cv2.dilate(img, kernel)
cv2.imshow('img1', img1)
cv2.waitKey(0)
