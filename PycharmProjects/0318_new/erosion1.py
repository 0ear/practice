import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = np.zeros((13, 13), dtype=np.uint8)
print(img)
plt.imshow(img, cmap='gray')
plt.show()
img[4:10, 3:9] = 1
print(img)
plt.imshow(img, cmap='gray')
plt.show()
dst4 = sm.erosion(img, sm.square(2))
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)) 
dst4 = cv2.erode(img, kernel)
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()