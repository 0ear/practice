import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):
    pass
cv2.namedWindow('colorbars')
hh = 'MaX'
hl = 'Min'
wnd = 'Colorbars'
cv2.createTrackbar('MaX', 'colorbars', 0, 255, nothing)
cv2.createTrackbar('Min', 'colorbars', 0, 255, nothing)
img = cv2.imread('../img/2a.jpg')
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)


while True:
    hul = cv2.getTrackbarPos('MaX', 'colorbars')
    huh = cv2.getTrackbarPos('Min', 'colorbars')
    ret, thresh1 = cv2.threshold(img, hul, huh, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, hul, huh, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, hul, huh, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, hul, huh, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, hul, huh, cv2.THRESH_TOZERO_INV)
    cv2.imshow('thresh1', thresh1)
    cv2.imshow('thresh2', thresh2)
    cv2.imshow('thresh3', thresh3)
    cv2.imshow('thresh4', thresh4)
    cv2.imshow('thresh5', thresh5)
    k = cv2.waitKey()
    if k == 27:
        break