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
cv2.waitKey(0)