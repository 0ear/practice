import numpy as np
img = cv2.imread('1.jpg')
cv2.imshow('img1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
rows, cols = img.shpae[:2]
print('img rows:', rows)
print('img cols:', cols)
M = cv2