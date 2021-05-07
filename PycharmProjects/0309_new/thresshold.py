from skimage.io import imread, imshow, imsave
import numpy as np
import matplotlib.pyplot as plt
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import cv2
image1 = imread('../img/threshold.png')
imshow(image1) #需搭配plt才能顯示
plt.show()
print(image1.shape)
print('skimage轉換灰階有兩種方式')
image2 = imread('../img/threshold.png', as_gray= True)
imshow(image2)
plt.show()
print(image2.shape)
print('第二種')
image3 = color.rgb2gray(image1)
imshow(image3)
plt.show()
print(image3.shape)