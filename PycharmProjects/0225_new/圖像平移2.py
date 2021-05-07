import cv2
import  numpy as np
import  matplotlib.pyplot as plt
img=cv2.imread('houses.jpg')
print('圖像仿製的規劃')
#取出原本圖像的rows與cols
rows,cols=img.shape[:2]
print('img rows:',rows)
print('img cols:',cols)
print('請設定改變的矩陣M')
M=np.float32([[1,0,100],[0,1,50]])
print(M)
N=np.float32([[0.5,0,100],[0,0.75,50]])
print(N)
dst=cv2.warpAffine(img,M,(cols,rows))
dst2=cv2.warpAffine(img,N,(cols,rows))
#plt.imshow(img)
#plt.show()
#plt.imshow(dst)
#plt.show()
#水平移動，位置是100-375 ，在375加入一條垂直線
#垂直部分可於264.5加入水平線
plt.grid()

plt.imshow(dst2)
plt.vlines(350,0,285,colors='yellow')
plt.show()

#plt.show()

