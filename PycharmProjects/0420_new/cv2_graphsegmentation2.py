import cv2
import numpy as np
import random
im = cv2.imread('../img/simpsons.jpg')
segmentator = cv2.ximgproc.segmentation.createGraphSegmentation(
    sigma = 0.7, k = 300, min_size = 10000
)
segment = segmentator.processImage(im)
print('以下為顏色分割影像的擷取與顏色標記')
seg_image = np.zeros(im.shape, np.uint8)
a = 0
for i in range(np.max(segment)):
    y, x = np.where(segment == i)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    a += 1
    for xi, yi in zip(x, y):
        seg_image[yi, xi] = color
print(a)
result = cv2.addWeighted(im, 0.3, seg_image, 0.7, 0)
cv2.imshow('result', result)
cv2.waitKey()


