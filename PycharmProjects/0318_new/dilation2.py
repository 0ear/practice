import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = np.zeros((13, 13), dtype=np.uint8)
print(img)
plt.imshow(img, cmap='gray')
plt.show()
img[4:8, 3:7] = 1
print(img)
plt.imshow(img, cmap='gray')
plt.show()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2)) #opencv要求要uint8
dst4 = cv2.dilate(img, kernel)
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()
dst4 = sm.dilation(img, sm.square(2))
print(dst4)要求要是uint8
plt.imshow(dst4, cmap='gray')
plt.show()
