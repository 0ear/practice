import cv2
import  numpy as np
img=cv2.imread('Dog.jpg')
print('圖像仿製的規劃')
#取出原本圖像的rows與cols
rows,cols=img.shape[:2]
print('img rows:',rows)
print('img cols:',cols)
print('請設定改變的矩陣M')
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.5) #第一個參數為旋轉的中心點
N = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1.5) #第二為轉的度數 第三為放大縮小的倍數
P = cv2.getRotationMatrix2D((cols/2, rows/2), 100, 0.3)
dst=cv2.warpAffine(img,M,(cols,rows))
dst2=cv2.warpAffine(img,N,(cols,rows))
dst3=cv2.warpAffine(img,P,(cols,rows))
cv2.imshow('img1', img)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows
