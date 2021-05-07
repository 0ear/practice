import cv2
import  numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('Dog.jpg')
print('圖像仿製的規劃')
#取出原本圖像的rows與cols
rows,cols=img.shape[:2]
print('img rows:',rows)
print('img cols:',cols)
print('請設定改變的矩陣M')
a1 = np.float32([[50, 50], [200, 50], [50, 200]])
a2 = np.float32([[10, 50], [200, 50], [100, 250]])
M = cv2.getAffineTransform(a1, a2)
print('依原本的圖像使用你設定的矩陣進行圖像的模仿製作')
dst = cv2.warpAffine(img, M ,(cols, rows))
cv2.imshow('img1', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.scatter(50, 50, color='b')
plt.scatter(200, 50, color='red')
plt.scatter(50, 200, color='g')
plt.scatter(10, 50, color='b')
plt.scatter(200, 50, color='r')
plt.scatter(100, 250, color='g')
plt.show()
