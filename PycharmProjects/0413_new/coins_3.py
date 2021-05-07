import cv2,coins_2
gray = coins_2.gray
image = coins_2.image
blurred = coins_2.blurred
edged = coins_2.edged
print('輪廓偵測')
contours, hierarchy = cv2.findContours(
    edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
print('count:', len(contours))
print('contours:', contours)
print('hierarchy:', hierarchy)
coins = image.copy()
cv2.drawContours(coins, contours, -1, (0,255,0),2) #輪廓繪製
cv2.imshow('contours', coins)
cv2.imwrite('coins_3.contours.png', coins)
cv2.waitKey()