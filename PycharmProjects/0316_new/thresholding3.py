from skimage.io import imshow, imread, imsave
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import cv2
def image_show(image, nrows = 1, ncols = 1, cmap = 'gray'):
    fig, ax = plt.subplots(nrows = nrows, ncols=ncols, figsize = (6,6))
    ax.imshow(image, cmap = 'gray')
    ax.axis('off')
    plt.show()
    return fig, ax
#image1 = imread('../img/cat.jpg', as_gray = True)
image1 = imread('../img/threshold.png', as_gray = True)
thresh1 = filters.threshold_otsu(image1)
thresh2 = filters.threshold_yen(image1)
thresh3 = filters.threshold_mean(image1)
thresh4 = filters.threshold_minimum(image1)
print(thresh1*255)
print(thresh2*255)
print(thresh3*255)
print(thresh4*255)
plt.hist(image1.ravel()*255, range(0, 255)) #資料經filter計算後是介於0跟1間因此*255回歸到正常值
plt.axvline(x = thresh1*255, c = 'r', label = 'otsu')
plt.axvline(x = thresh2*255, c = 'k', label = 'yen')
plt.axvline(x = thresh3*255, c = 'b', label = 'mean')
plt.axvline(x = thresh4*255, c = 'g', label = 'minimum')
plt.legend()
plt.show()
