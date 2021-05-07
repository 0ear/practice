from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import cv2, os
print('文字部分必須載入pil')
from PIL import ImageFont, ImageDraw, Image
image1 = io.imread('../img/Flower.bmp')
print('依據flower的影像的尺寸產生矩形')
Rectangle = np.zeros(image1.shape, np.uint8)
print(Rectangle)
print('--'*70)
Rectangle = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2GRAY)
print(Rectangle) #會看到三維轉成二維
print((Rectangle.__class__))
print('在Rectangle上用opencv產生一文字')
text1 = '三月甚好'
fontpath = 'NotoSerifCJKtc-Medium.otf' #挑選字型,otf表open font,為google
                                       #與adobe推出的免費字型可用於python環境
font1 = ImageFont.truetype(fontpath, 50) #載入字型
print('由於字型於PIL轉換為影像，所以Rectangle也得轉換為影像')
image1 = Image.fromarray(Rectangle)
print('於圖片上加入文字')
draw1 = ImageDraw.Draw(image1)
draw1.text((30, 30), text1, font=font1)
print('繪製完成後再將PIL影像轉換為numpy')
Rectangle = np.array(image1)
cv2.imshow('font1', Rectangle)
#Rectangle = cv2.cvtColor(Rectangle, cv2.COLOR_BGR2RGB)
#image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
#added = cv2.subtract(Rectangle, image1) #減法是前面的圖減掉後面的
#added2 = cv2.subtract(image1, Rectangle)
#cv2.imshow('rect2',added)
#cv2.imshow('rect3',added2)
cv2.waitKey(0)