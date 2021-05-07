from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2, os
image1 = io.imread('../img/Flower.bmp')
print('依據flower的影像的尺寸產生矩形')
Rectangle = np.zeros(image1.shape, np.uint8)
print(Rectangle)
print('--'*70)
Rectangle = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2GRAY)
print(Rectangle) #會看到三維轉成二維
print('在Rectangle上用opencv產生一條直線')
Rectangle2 = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2RGB)
cv2.line(Rectangle, (125, 125), (675,675), 255, 25)
cv2.line(Rectangle2, (125, 125), (675,675), (100, 200, 100), 25)
#cv2.circle(Rectangle, (350,350),100,75,10)
cv2.imshow('line1', Rectangle) #原本是全黑加上的是灰色的那塊
cv2.imshow('line2', Rectangle2)
cv2.waitKey(0)
Rectangle = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2RGB)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
added = cv2.subtract(Rectangle, image1) #減法是前面的圖減掉後面的
added2 = cv2.subtract(image1, Rectangle)
cv2.imshow('rect2',added)
cv2.imshow('rect3',added2)
cv2.waitKey(0)