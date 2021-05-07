import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io
img = io.imread('../img/lights.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', img2)
print('進行高斯模糊')
img3 = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow('GaussianBlur', img3)
#cv2.waitKey(0)
print('threshold_binary的操作')
print('低於200為0, 高於200為255的調整(binary最低為0最高為自訂')
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold_binary', thresh1)
ret, thresh2 = cv2.threshold(img3, 200, 255, cv2.THRESH_BINARY_INV)#和前面相反
cv2.imshow('threshold_binary_INV', thresh2)

print('tozero低於閥值不改變,超過為0')
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_TOZERO)
cv2.imshow('threshold_binary_tozero', thresh1)
print('低於閥值為0,超過則不改變')
ret, thresh1 = cv2.threshold(img3, 200, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('threshold_binary_tozero_inv', thresh1)
cv2.waitKey(0)