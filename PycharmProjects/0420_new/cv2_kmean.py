import cv2
import numpy as np
import matplotlib.pyplot as plt
im = cv2.imread('../img/simpsons.jpg', 0) #0代表灰階
cv2.imshow('im', im)
cv2.waitKey()
print('影像內容想要進行分群,可指定分多少群')
print('影像要先從2D轉成1D')
img1 = im.reshape((im.shape[0]*im.shape[1],1))
print(img1.shape)
print(img1)
img1 = np.float32(img1)
print('圖像挑選的規則建置')
img2 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
print(img2)
print('準備進行分群')
#flags = cv2.KMEANS_RANDOM_CENTERS #分群中心點物件的建立
flags = cv2.KMEANS_PP_CENTERS
compactness, labels, centers = cv2.kmeans(img1, 4, None, img2, 10, flags)
img3 = labels.reshape(im.shape[0], im.shape[1])
plt.imshow(img3, 'gray')
plt.show()
#cv2.imshow('img3', img3)
#cv2.waitKey()
