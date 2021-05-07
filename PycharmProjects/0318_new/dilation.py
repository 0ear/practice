import skimage.morphology as sm
import matplotlib.pyplot as plt
import numpy as np
img = np.zeros((13, 13), dtype=np.int)
print(img)
plt.imshow(img, cmap='gray')
plt.show()
img[4:8, 3:7] = 1
print(img)
plt.imshow(img, cmap='gray')
plt.show()
dst4 = sm.dilation(img, sm.square(2)) #選1沒效果2是左上增加1,3是在在右下加1
#dst4 = sm.dilation(img, sm.star(2))
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()
dst4 = sm.dilation(img, sm.square(3))
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()
dst4 = sm.dilation(img, sm.square(4))
print(dst4)
plt.imshow(dst4, cmap='gray')
plt.show()