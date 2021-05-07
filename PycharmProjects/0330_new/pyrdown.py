import cv2
from skimage import io
img = io.imread('../img/graph3.png')
def pyramid(img):
    level = 3
    temp = img.copy()
    pyramidid_img = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        print(dst.size)
        print(dst.__class__)
        print('-'*70)
        pyramidid_img.append(dst)
        cv2.imshow('pyramid'+str(i), dst)
        temp = dst.copy()
pyramid(img)
cv2.waitKey()