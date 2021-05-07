import skimage.morphology as sm
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import cv2
#img = cv2.imread('../img/mor2.png')
img = cv2.imread('close1.png')
print(img)
print('shape:', img.shape)
cv2.imshow('img0', img)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
img1 = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)
cv2.imshow('img1', img1)
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
img2 = cv2.morphologyEx(img,cv2.MORPH_OPEN, kernel)
cv2.imshow('img2', img2)
cv2.waitKey(0)
