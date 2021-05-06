import matplotlib.pyplot as plt
import cv2,os
from skimage import io
image = plt.imread('../img/tree.jpg')
img2 = cv2.imread('../img/tree..jpg') #opencv通道為bgr其他的是rgb因此跑出來會有色彩差異
plt.imshow(image)
plt.imshow(img2)
plt.axis('off')
plt.show()