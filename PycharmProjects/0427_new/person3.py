import  numpy as np
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
img=cv2.imread('person1.jpg')
#img=cv2.imread('../img/1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)
print(faces)
for x1,y1,w,h in faces:
    x2 = x1+w
    y2 = y1+h
    img=cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
    face1 = y2 - 1
    upface = img[y1:y1+int(1/3*face1), x1:x2]
    downface = img[y1+int(1/3*face1):y2, x1:x2]
    cv2.imshow('upface', upface)
    cv2.imshow('downface', downface)
    cv2.waitKey(0)
    #roi_gray=gray[y:y+h,x:x+w]
    #roi_color=img[y:y+h,x:x+w]
    #eyes=eye_cascade.detectMultiScale(roi_gray)
    #for ex, ey, ew, eh in eyes:
        #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255, 0), 2)
cv2.imshow('img',img)
cv2.waitKey(0)