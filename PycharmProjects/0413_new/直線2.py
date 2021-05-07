import cv2
import numpy as np
im = cv2.imread('../img/street.jpg')
cv2.imshow('Original', im)
im = cv2.GaussianBlur(im, (7,7), 0)
cv2.imshow('blur', im)
edges = cv2.Canny(im, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
cv2.waitKey()
lines = cv2.HoughLines(edges, 1, np.pi/180, 260)
result = im.copy()
for line in lines[0]:
    rho = line[0] #最短距離
    theta = line[1] #角度
    if (theta < (np.pi/4.0)) or (theta > (3.*np.pi/4.0)):
        pt1 = (int(rho/np.cos(theta)), 0)
        pt2 = (int((rho - result.shape[0]*np.sin(theta))/np.cos(theta)), result.shape[0])
        cv2.line(result, pt1, pt2, (0,0,255))
    else:
        pt1 = (0, int(rho / np.sin(theta)))
        pt2 = (result.shape[1],int((rho -result.shape[1] * np.cos(theta)) / np.sin(theta)))
        cv2.line(result, pt1, pt2, (0, 255, 0))
cv2.imshow('Hough', result)
cv2.waitKey()
