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
print('在Rectangle上用opencv產生一多邊形')
Rectangle2 = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2RGB)
print('先規劃頂點座標')
pts =np.array([[170,55],[65,175],[220,180],[20,80],[300,260]],np.int32)
print(pts)
#pts.reshape((-1, 1, 2))
#print(pts)
print('繪製多邊形')
cv2.polylines(Rectangle, [pts], True, 100, 20)#True跟False影響圖形封閉與否
cv2.imshow('ellipse', Rectangle)
Rectangle = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2RGB)
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
added = cv2.subtract(Rectangle, image1) #減法是前面的圖減掉後面的
added2 = cv2.subtract(image1, Rectangle)
cv2.imshow('rect2',added)
cv2.imshow('rect3',added2)
cv2.waitKey(0)