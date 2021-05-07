import cv2,coins_1
gray = coins_1.gray
#resized = coins_1.resized
image = coins_1.image
print('高斯模糊的處理') #過濾雜訊
blurred = cv2.GaussianBlur(gray, (13, 13), 0)
cv2.imshow('blurred', blurred)
cv2.imwrite('coins_GaussianBlur.png', blurred)
print('邊緣偵測不代表輪廓處理')
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow('Canny', edged)
cv2.imwrite('coins_Canny.png', edged)
cv2.waitKey()
