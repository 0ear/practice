from PIL import  Image
im=Image.open('../img/cat.jpg').convert('RGB')
box=(240,195,760,700)
image_crop=im.crop(box)
image_crop.save('cat1.jpg')
im2=Image.open('../img/1.jpg').convert('RGB')
im2.paste(image_crop,(50,100))
im2.save('paste1.jpg')

#顯示影像座標位置
import matplotlib.pyplot as plt
plt.imshow(im)
plt.axhline(300,0 ,1 , c='blue') # y座標,x起始位置比例,x結束位置比例,顏色
plt.axhline(710,0 ,1 , c='blue')
plt.axvline(190,0 ,1 , c='yellow')# x座標,y起始位置比例,y結束位置比例,顏色
plt.axvline(500,0 ,1 , c='yellow')
#plt.grid()
plt.show()

#拼圖
im3 = Image.open('../img/sample02.jpg').convert('RGB')
img_size = im3.size
xx=3 ; yy = 2
x = img_size[0]//xx
y = img_size[1]//yy
for j in range(yy):
    for i in range(xx):
        left = i*x
        up = y*j
        right = left+x
        low = up+y
        region = im3.crop((left, up, right, low))
        print(left, up, right, low)
        temp = str(i)+str(j)
        region.save(temp+'.png')