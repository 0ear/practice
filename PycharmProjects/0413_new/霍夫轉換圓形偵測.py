import numpy as np
import cv2, math
#img1 = cv2.imread('../img/Cans.bmp')
img1 = cv2.imread('../img/coins.png')
img2 = img1.copy()
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150, 200, 50
                           #, minRadius = 120, maxRadius = 200)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 70, 20, 10
                           , minRadius = 50, maxRadius = 80)
print(circles)
circles = np.uint16(np.around(circles))
print(circles) #取整數出來
for i in circles[0, :]:
    print(i)
    cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 20) #畫外圍的圓形
    cv2.circle(img2, (i[0], i[1]), 2, (0, 0, 255), 3) #畫圓心
cv2.imshow('Original', img1)
cv2.imshow('Circle', img2)
cv2.waitKey()