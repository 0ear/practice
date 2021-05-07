import cv2
import numpy as np
drawing = False
mode = True
ix, iy = -1, -1
def nothing(x):
    pass
def draw_circle(event, x, y, flags, param):
    s = 0
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    color = (b, g, r)
    if s == 1:
        color(255, 255, 255)
    s = cv2.getTrackbarPos('eraser', 'image')
    thin = cv2.getTrackbarPos('thin', 'image')
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                cv2.circle(img, (x,y), thin, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


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
switch = '0:off \n 1:on'
img = np.zeros((240, 240, 3), np.uint8)
img[:] = 255
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('eraser', 'image', 0, 1, nothing)
cv2.createTrackbar('thin', 'image', 1, 50, nothing)
cv2.setMouseCallback('image', draw_circle) #滑鼠呼叫語法
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey()
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break