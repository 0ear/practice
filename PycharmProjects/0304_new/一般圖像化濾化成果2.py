import cv2
import numpy as np
a = np.zeros((18, 18), dtype = 'uint8')
print('可繪製矩形與圓形,再依這個矩形進行濾化')
cv2.rectangle(a, (5, 5), (15, 15), 155, 2)
print(a)
print('建立kernel-1、銳利化')
kernel1=np.array((
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]),
    dtype='int')
print('建立kernel-2、模糊化')
kernel2=np.array((
    [0.0625,0.0125,0.0625],
    [0.125,0.35,0.125],
    [0.0625, 0.0125, 0.0625]),
    np.float32)
a2=cv2.filter2D(a,-1,kernel1)
a3=cv2.filter2D(a,-1,kernel2)
print(a2)
print()
print(a3)
print()
cv2.imwrite('a1.png', a)
cv2.imwrite('a2.png', a2)
cv2.imwrite('a3.png', a3)