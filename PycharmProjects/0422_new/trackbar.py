import cv2
import numpy as np
switch = '0:off \n 1:on'
def change_color(x):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    cv2.imshow('image', img)
img = np.zeros((240, 180, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('R', 'image', 0, 255, change_color)
cv2.createTrackbar('G', 'image', 0, 255, change_color)
cv2.createTrackbar('B', 'image', 0, 255, change_color)
cv2.createTrackbar(switch, 'image', 0, 1, change_color)
while True:
    k = cv2.waitKey()
    if k == 27:
        break