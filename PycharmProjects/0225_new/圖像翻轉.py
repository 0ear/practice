import numpy as np
import cv2
img = cv2.imread('DOG.jpg')
flip0 = cv2.flip(img, 0) #上下顛倒
flip1 = cv2.flip(img, 1) #左右顛到
flip2 = cv2.flip(img, -1) #上下再左右顛倒
cv2.imshow('img1', img)
cv2.imshow('flip0', flip0)
cv2.imshow('flip1', flip1)
cv2.imshow('flip2', flip2)
cv2.waitKey(0)
cv2.destroyAllWindows()