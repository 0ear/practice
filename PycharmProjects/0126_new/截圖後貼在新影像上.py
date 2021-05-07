from PIL import  Image
from PIL import  ImageDraw
import matplotlib.pyplot as plt
im=Image.open('../img/cat.jpg').convert('RGB')
box=(240,195,760,700)
image_crop=im.crop(box)
image_crop.save('cat1.jpg')
im3 = Image.new('RGB', (700, 700))
im1 = image_crop.rotate(45) #非90或180時有邊角的調整而90度時畫面則為正常的四邊形
im3.paste(im1,(50,50))
plt.imshow(im3)
plt.show()
im3.save('cat2.jpg')

im=Image.open('../img/sample02.jpg').convert('RGB')
box=(240,195,760,700)
Image_crop = im.crop(box)
img4 = Image.new('RGB',(600, 600))
im1a = Image_crop.rotate(45)
img4.paste(im1a,(0,0))
plt.imshow(img4)
plt.show()