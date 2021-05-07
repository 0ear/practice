import cv2
import numpy as np
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        print('refPt[0]:', refPt[0])
        print('refPt[1]:', refPt[1])
        print('len(refPt):', len(refPt))
        cv2.rectangle(image, refPt[0], refPt[1], (0,255,0), 2)
        cv2.imshow('image', image)
image = cv2.imread('../img/messi5.jpg')
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', click_and_crop)
while True:
    cv2.imshow('image', image)
    key = cv2.waitKey(1)&0xFF
    if key==ord('r'):
        image = clone.copy()
    elif key==ord('c'):
        break
if len(refPt) == 2: #按下c跳出上面迴圈進行判斷
    print('refPt[0][1]:', refPt[0][1])
    print('refPt[1][1]:', refPt[1][1])
    print('refPt[0][0]:', refPt[0][0])
    print('refPt[1][0]:', refPt[1][0])
    roi = clone[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
    cv2.imshow('ROI', roi)
    cv2.waitKey(0)