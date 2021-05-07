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
a1 = np.float32([[76, 50], [100, 154], [50, 133], [123, 89]])
a2 = np.float32([[0, 0], [250, 0], [0, 250], [250, 250]])
M = cv2.getPerspectiveTransform(a1, a2)
print('依原本的圖像使用你設定的矩陣進行圖像的模仿製作')
dst = cv2.warpPerspective(img, M ,(300, 300))
plt.grid()
plt.imshow(img)
plt.show()
cv2.imshow('img1', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()