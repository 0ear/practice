import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('houses.jpg')
print(img.shape)
rows, cols = img.shape[:2] #[:2]代表取出0和1 為寬跟高
M = np.float32([[1, 0, 100], [0, 1, 50]]) #float32代表轉換為所要的數值
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Original', img)
cv2.imshow('change', dst)
cv2.waitKey(0)