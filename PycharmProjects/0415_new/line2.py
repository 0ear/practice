import cv2 as cv
import numpy as np
def DegreeTrans(theta):
    res = theta/np.pi*180
    print('res:', res)
    return res
def rotateimage(src, degree):
    h, w = src.shape[:2]
    RotateMatrix = cv.getRotationMatrix2D((w/2.0, h/2.0), degree, 1)
    print('RotateMatrix:', RotateMatrix)
    rotate = cv.warpAffine(src, RotateMatrix, (w,h), borderValue=(255, 255,255))
    return rotate
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edge = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edge, 1, np.pi/180, 200)
    sum = 0 #new
    for i in range(len(lines)):
        #print(i)
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            sum += theta
            cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1, cv.LINE_AA)
            cv.imshow('image-lines', image)
    print('sum', sum)
    average = sum/len(lines)
    angle = DegreeTrans(average) - 90
    return angle

src = cv.imread('../img/demo1.png')
#src = cv.imread('../img/Advanced_Sudoku.png')
cv.imshow('input', src)
degree = line_detection(src)
print('調整角度', degree)
rotate = rotateimage(src, degree)
cv.imshow('rotate', rotate)
cv.waitKey()