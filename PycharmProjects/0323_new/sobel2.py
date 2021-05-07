import cv2
import numpy as np
#img = cv2.imread('../img/house_input.png')
#img = cv2.imread('../img/Flower.bmp')
img = cv2.imread('../img/houses.jpg') #可看出水平跟垂直偵測的差異
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2', img2)
a1 = cv2.Sobel(img, cv2.CV_16S,1,0) #針對x軸方向進行邊緣偵測
b1 = cv2.Sobel(img, cv2.CV_16S,0,1) #針對y軸進行偵測,改成(1,1)及兩軸同時
                                    #會過濾掉只有x or y軸邊緣的資料
x1 = cv2.convertScaleAbs(a1)
cv2.imshow('x1',x1)
x2 = cv2.convertScaleAbs(b1)
cv2.imshow('x2', x2)
#conv1 = cv2.addWeighted(x1, 0.7, x2, 0.4, 0)
#conv2 = cv2.addWeighted(x1, 0.7, x2, 0.4, 100)
#cv2.imshow('conv1', conv1)
#cv2.imshow('conv2', conv2)
cv2.waitKey(0)