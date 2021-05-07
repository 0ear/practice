import cv2
import numpy as np
img = cv2.imread('../img/house_input.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2', img2)
a = cv2.Sobel(img, cv2.CV_16S,1,0)
print(a)
print('--'*70)
b = cv2.Sobel(img, cv2.CV_8U,1,0)
print(b)
print()
cv2.imshow('a', a) #不建議當作圖形顯示
cv2.imshow('b', b) #不建議當作圖形顯示
x1 = cv2.convertScaleAbs(a)
cv2.imshow('x1', x1)
x2 = cv2.convertScaleAbs(b)
cv2.imshow('x2', x2)
cv2.waitKey(0)