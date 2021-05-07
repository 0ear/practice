from skimage.io import imshow, imread, imsave
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import cv2
image1 = imread('../img/threshold.png', as_gray = True)
imshow(image1)
plt.show()
print(image1.shape)
from skimage.filters import try_all_threshold
fig, ax = try_all_threshold(image1, figsize = (10, 8 ), verbose = False)
plt.show()