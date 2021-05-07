from PIL import Image
import matplotlib.pyplot as plt
image = Image.open('../img/sample02.jpg').convert('RGB')
plt.imshow(image)
plt.axhline(200, 0, 1, c='blue')
plt.axvline(350, 0, 1, c='yellow')
plt.grid()
plt.show()
print(image.size)
print(image.mode)
image2 = image.convert('RGBA')
print(image2.size)
print(image2.mode)
newimage = []
for i in image2.getdata():
    if i[0] >= 211 and i[0] <= 238:
         newimage.append((255,255,255,0)) #代表透明背景
    else:
        newimage.append(i)
image2.putdata(newimage)
plt.imshow(image2)
plt.show()