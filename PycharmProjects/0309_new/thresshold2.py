from skimage.io import imread, imshow, imsave
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import cv2
import thresshold
image3 = thresshold.image3
import matplotlib.pyplot as plt
plt.hist(image3.ravel())
plt.show()
print('幾種不同範圍的切割')
image3_segmented = image3 > 0.11
imshow(image3_segmented)
plt.show()
image3_segmented = image3 > 0.2
imshow(image3_segmented)
plt.show()
image3_segmented = image3 > 0.3
imshow(image3_segmented)
plt.show()