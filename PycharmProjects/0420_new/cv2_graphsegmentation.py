import cv2
import numpy as np
im = cv2.imread('../img/simpsons.jpg')
segmentator = cv2.ximgproc.segmentation.createGraphSegmentation(
    sigma = 0.5, k = 300, min_size = 1000
)
segment = segmentator.processImage(im)
mask = segment.reshape(list(segment.shape)+[1]).repeat(3, axis = 2)
masked = np.ma.masked_array(im, fill_value = 0)
for i in range(np.max(segment)):
    masked.mask = mask != i
    y, x = np.where(segment == i)
    top, bottom, left, right = min(y), max(y), min(x), max(x)
    dst = masked.filled()[top:bottom+1, left:right+1]
    cv2.imwrite('./simpsons/' + str(i) + '.png', dst)

