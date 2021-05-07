import cv2
img=cv2.imread('../img/cat.jpg')
img1 = cv2.pyrDown(img)
img2 = cv2.pyrDown(img1)
img3 = cv2.pyrUp(img2)
img4 = img1-img3
print('img大小:', img.shape)
print('img1大小:', img1.shape)
print('img2大小:', img2.shape)
print('img3大小:', img3.shape)
print('img4大小:', img4.shape)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()