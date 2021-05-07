import cv2
import numpy as np
def mouseevent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('按下滑鼠左鍵')
    if event == cv2.EVENT_LBUTTONUP:
        print('放開滑鼠左鍵')
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('按下滑鼠左鍵兩次')
    if event == cv2.EVENT_FLAG_LBUTTON:
        print('拖拉滑鼠左鍵')

    if event == cv2.EVENT_RBUTTONDOWN:
        print('按下滑鼠右鍵')
    if event == cv2.EVENT_RBUTTONUP:
        print('放開滑鼠右鍵')
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print('按下滑鼠右鍵兩次')
    if event == cv2.EVENT_FLAG_RBUTTON:
        print('拖拉滑鼠右鍵')

    if event == cv2.EVENT_MOUSEHWHEEL:
        if flags > 0:
            print('向前滾動')
        else:
            print('向後滾動')
    if event == cv2.EVENT_MOUSEHWHEEL:
        print('鍵盤需同時按下ALT')
        if flags > 0:
            print('向左滾動')
        else:
            print('向右滾動')

img = np.zeros((440, 440, 3), np.uint8)
img[:] = 255
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouseevent)
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey()
    if k == 113: #小寫q 27為 esc
        break