import numpy as np
import cv2
def gamma_correction(f, gamma = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    c = 255.0/(255.0**gamma)
    table = np.zeros(256) #初始值為0
    for i in range(256):
        table[i] = round(i**gamma*c, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    return g
img = cv2.imread('1.jpg')       #改成('1.jpg, 0)時可將開啟的圖檔轉成黑白圖
                                # 1是全彩 -1是載入具透明背景之圖檔
img1 = gamma_correction(img, 0.1)
img2 = gamma_correction(img, 0.2)
img3 = gamma_correction(img, 0.5)
cv2.imshow('Original', img)
cv2.imshow('Gamma = 0.1', img1)
cv2.imshow('Gamma = 0.2', img2)
cv2.imshow('Gamma = 0.5', img3)
cv2.waitKey(0)
