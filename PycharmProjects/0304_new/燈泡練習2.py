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
print('threshold_trunc 低於125不改變,高於125調整為255')
ret, thresh2 = cv2.threshold(img3, 125, 255, cv2.THRESH_TRUNC)
cv2.imshow('threshold_trunc', thresh2)
cv2.waitKey(0)

