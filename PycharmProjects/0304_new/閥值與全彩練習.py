import cv2
import numpy as np
img = cv2.imread('../img/RGB_Chart.bmp')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('Gray', img2)
print('進行高斯模糊')
img3 = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow('GaussianBlur', img3)
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold_binary', thresh1)
et, thresh2 = cv2.threshold(img3, 200, 255, cv2.THRESH_BINARY_INV)#和前面相反
cv2.imshow('threshold_binary_INV', thresh2)

print('tozero低於閥值不改變,超過為0')
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_TOZERO)
cv2.imshow('threshold_binary_tozero', thresh1)
print('低於閥值為0,超過則不改變')
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('threshold_binary_tozero_inv', thresh1)
print('threshold_trunc 低於125不改變,高於125調整為255')
ret, thresh2 = cv2.threshold(img3, 125, 255, cv2.THRESH_TRUNC)
cv2.imshow('threshold_trunc', thresh2)
cv2.waitKey(0)