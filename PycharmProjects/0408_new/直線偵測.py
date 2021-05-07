import numpy as np
import cv2,os
from skimage import io
import math
img1 = cv2.imread('../img/Traffic_Lanes.bmp')
img2 = img1.copy()
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200)
edges2 = cv2.Canny(img1, 50, 200)
lines = cv2.HoughLines(edges, 1, math.pi/180.0, 220)
#cv2.imshow('Original Image', img1)
#cv2.imshow('Canny1 Image', edges)
#cv2.imshow('Canny2 Image', edges2)
#print(lines)
#print(lines.__class__)
print('lines指示空間座標資訊,得做轉換處理')
if lines is not None:
    a, b, c=lines.shape
    for i in range(a):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0, y0 = a*rho, b*rho
        pt1 = (int(x0+1000*(-b)), int(y0+1000*(a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        print('依之前計算的座標pt1到pt2繪製直線')
        cv2.line(img2, pt1, pt2, (255, 0, 0), 1, cv2.LINE_AA)
cv2.imshow('Lines Image', img2)
cv2.waitKey()