import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io
print('載入圖像方式有兩種')
img = io.imread('../img/lights.jpg')
print('opencv顏色會不對')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img2)
cv2.waitKey()
plt.imshow(img)
plt.show()
for k in range(0, 200):
    img2[:,:] = np.where(img2[:, :]* 1.03 <255, #設定的條件
                        (img2[:, :]*1.03).astype(np.uint8), #條件成立時做的事
                         img2[:, :]) #條件不成立做的事
    #cv2.imshow('Update'+str(k)+':', img2) #開啟兩百張
    cv2.imshow('Update:', img2) #開啟兩百張只是會覆蓋上去
    cv2.waitKey(50) #等50/1000秒 再依序關閉
