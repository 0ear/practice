#from PIL import Image
#image = Image.open('../img/sample01.jpg').convert('RGB')
#print(image.size)
#img3 = image.copy()
#img4 = img3.resize((2400,1800)) # 有兩個參數，只是省略第二個
#img4.save('resize.png')
#print(img3.size)
#print(img4.size)

from PIL import Image
image = Image.open('../img/LenaRGB.bmp').convert('RGB')
print(image.size)
img3 = image.copy()
img4 = img3.resize((2400,1800), resample = Image.ANTIALIAS)#四種可選
img5 = img3.resize((2400,1800), resample = Image.BICUBIC)
img6 = img3.resize((2400,1800), resample = Image.BILINEAR)
img7 = img3.resize((2400,1800), resample = Image.NEAREST)
img4.save('resizea.png')
img5.save('resizeb.png')
img6.save('resizec.png')
img7.save('resized.png')
print(img3.size)
print(img4.size)
print(img5.size)
print(img6.size)
print(img7.size)