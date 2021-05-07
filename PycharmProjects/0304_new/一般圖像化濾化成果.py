import cv2
import numpy as np
img = cv2.imread('Holloways_beach.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('建立kernel-1, 銳利化')
kernel1 = np.array(([0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]),
                   dtype= 'int')
print('建立kernel-2, 模糊化')
kernel2 = np.array(([0.0625, 0.0125, 0.0625],
                   [0.125, 0.35, 0.125],
                   [0.0625, 0.0125, 0.0625]),
                   np.float32)
img3 = cv2.filter2D(img2, -1, kernel1)
img4 = cv2.filter2D(img2, -1, kernel2)
cv2.imshow('Original', img2)
cv2.imshow('kernel1', img3)
cv2.imshow('kernel2', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('顯示數值資訊:img2')
print(np.array(img2))
print('顯示數值資訊:img3')
print(np.array(img3))
print('顯示數值資訊:img4')
print(np.array(img4))