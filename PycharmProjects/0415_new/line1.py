import cv2 as cv
import numpy as np
def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edge = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edge, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('image-lines', image)
def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edge = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edge, 1, np.pi / 180, 100, minLineLength = 3)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('line_detect_possible_demo', image)
src = cv.imread('../img/Traffic_Lanes.bmp')
#src = cv.imread('../img/Advanced_Sudoku.png')
cv.imshow('input', src)
line_detection(src)
line_detect_possible_demo(src)
cv.waitKey()