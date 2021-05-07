import skimage.morphology as sm
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
img = color.rgb2gray(io.imread('../img/mor.png'))
dst = sm.closing(img, sm.disk(13))
plt.imshow(img, cmap ='gray')
plt.show()
plt.imshow(dst, cmap ='gray')
plt.show()