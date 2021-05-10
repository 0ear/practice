import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure,data
from skimage.io import imread, imshow, imsave
from skimage.filters import rank
img = data.camera()
print('原始圖像的顏色分布')
image2 = img.ravel() #平坦化
print(img)
print(image2)
plt.hist(image2, bins = 256)
plt.show()
print('設定濾鏡進行平均')
selem = np.ones((10, 10))
img1 = rank.mean(img, selem = selem)
arr1 = img1.flatten()
plt.imshow(img1, plt.cm.gray)
plt.show()
plt.hist(arr1, bins = 256)
plt.show()