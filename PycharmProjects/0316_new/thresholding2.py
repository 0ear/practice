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
image1 = imread('../img/cat.jpg', as_gray = True)
#image_show
imshow(image1)
plt.show()
fig, ax = plt.subplots(1, 1)
ax.hist(image1.ravel(), bins = 32, range=[0, 256])
ax.set_xlim(0, 256)
plt.show()

image1=imread('../img/threshold.png',as_gray=True)
imshow(image1)
plt.show()
print(image1)
print()
print(image1.shape)
print(image1.ravel())
print()
print((image1.ravel()).shape)
plt.hist(image1.ravel())
plt.show()
