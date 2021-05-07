import cv2
import  numpy as np
img=cv2.imread('houses.jpg')
print('圖像仿製的規劃')
#取出原本圖像的rows與cols
rows,cols=img.shape[:2]
print('img rows:',rows)
print('img cols:',cols)
print('請設定改變的矩陣M')
M=np.float32([[1,0,100],[0,1,50]])
print(M)
N=np.float32([[0.5,0,100],[0,0.5,50]])
print(N)
dst=cv2.warpAffine(img,M,(cols,rows))
dst2=cv2.warpAffine(img,N,(cols,rows))
cv2.imshow('img1',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
