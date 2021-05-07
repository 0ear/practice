import  numpy as np
import cv2
import matplotlib.pyplot as plt
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
#img=cv2.imread('person1.jpg')
img=cv2.imread('../img/1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)
print(faces)
color = ('r', 'g', 'b')
for x1,y1,w,h in faces:
    x2 = x1+w
    y2 = y1+h
    img=cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
    face1 = y2 - y1
    upface = img[y1:y1+int(1/2*face1), x1:x2]
    downface = img[y1+int(1/2*face1):y2, x1:x2]
    cv2.imshow('upface', upface)
    cv2.imshow('downface', downface)
    cv2.waitKey(0)
    print('接著進行色彩差異統計圖表')
    for i, col in enumerate(color):
        hist1 = cv2.calcHist([upface], [i], None, [256], [0, 256])
        plt.plot(hist1, color = col)
        plt.xlim([0, 256])
    plt.title('upface')
    plt.show()
    for i, col in enumerate(color):
        hist1 = cv2.calcHist([downface], [i], None, [256], [0, 256])
        plt.plot(hist1, color = col)
        plt.xlim([0, 256])
    plt.title('downface')
    plt.show()
    print('進行相似度計算')
    hist1a = cv2.calcHist([upface], [0, 1, 2], None, [64, 64, 64],
                          [0, 256,0 , 256, 0, 256])
    cv2.normalize(hist1a, hist1a, 0, 1.0, cv2.NORM_MINMAX)
    hist1b = cv2.calcHist([downface], [0, 1, 2], None, [64, 64, 64],
                          [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist1b, hist1b, 0, 1.0, cv2.NORM_MINMAX)
    print('比較相關性')
    near1 = cv2.compareHist(hist1a, hist1b, 0)
    print(near1)
    #roi_gray=gray[y:y+h,x:x+w]
    #roi_color=img[y:y+h,x:x+w]
    #eyes=eye_cascade.detectMultiScale(roi_gray)
    #for ex, ey, ew, eh in eyes:
        #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255, 0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)