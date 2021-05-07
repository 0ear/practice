import cv2
import numpy as np
import random
im = cv2.imread('../img/simpsons.jpg')
segmentator = cv2.ximgproc.segmentation.createGraphSegmentation(
    sigma = 0.7, k = 300, min_size = 10000
)
segment = segmentator.processImage(im)
print('以下為矩形區域劃分')
seg_image = np.zeros(im.shape, np.uint8)
a = 0
mask = segment.reshape(list(segment.shape)+[1]).repeat(3, axis = 2)
masked = np.ma.masked_array(im, fill_value = 0)
for i in range(np.max(segment)):
    masked.mask = mask != i
    y, x =np.where(segment == i)
    top, bottom, left, right = min(y), max(y), min(x), max(x)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    cv2.rectangle(im, (left, bottom), (right, top), (0, 255, 0), 1)
    a += 1
    for xi, yi in zip(x, y):
        seg_image[yi, xi] = color
print(a)
result = cv2.addWeighted(im, 0.3, seg_image, 0.7, 0)
cv2.imshow('result', result)
cv2.waitKey()


