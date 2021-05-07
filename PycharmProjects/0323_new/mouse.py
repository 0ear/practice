import cv2
import numpy as np
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y),20,(255,0,0),-1)
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle) #使opencv能跟影像與滑鼠動作產生連結
while (1):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
