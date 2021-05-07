import cv2 as cv
src = cv.imread('../img/demo1.png')
h, w = src.shape[:2]
degree = 13.478872030505087
print('角度部分怎麼找?  是透過直線偵測方式取得所有角度的平均值')
RotateMatrix = cv.getRotationMatrix2D((w/2.0, h/2.0), degree, 1)
print('RotateMatrix:', RotateMatrix)
dst = cv.warpAffine(src, RotateMatrix, (w,h), borderValue=(255, 255,255))
cv.imshow('warp', dst)
cv.waitKey()