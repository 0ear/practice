import numpy as np
import cv2
from skimage import io
img = io.imread('../img/office.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('三種模糊的矩陣大小設定')
#blurred = np.hstack([cv2.GaussianBlur(img2, (3,3),0),
#                    cv2.GaussianBlur(img2, (15,15),0),
#                     cv2.GaussianBlur(img2, (27,27),0)])
blurred = np.hstack([cv2.GaussianBlur(img2, (7,7),0),
                    cv2.GaussianBlur(img2, (7,7),13),
                     cv2.GaussianBlur(img2, (7,7),25)])

#blurred = cv2.blur(img2, (3,3))
cv2.namedWindow('Averaged', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Averaged', 870,400)
cv2.imshow('Averaged', blurred)
print(img2)
print('-'*70)
print(blurred)
cv2.waitKey(0)