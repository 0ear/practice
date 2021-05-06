from PIL import Image
im = Image.open('../img/sample02.jpg').convert('RGB')
box = (240,195,760,700)
image_crop = im.crop(box)
print('左上角顏色資訊:', image_crop.getpixel((1,1)))
import matplotlib.pyplot as plt
im3=Image.new('RGBA',(800,800),(255,255,255,0))
im3.paste(image_crop,(100,50))
plt.imshow(im3)
plt.show()
im3.save('sample02_d.png')