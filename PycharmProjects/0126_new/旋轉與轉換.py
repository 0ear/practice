from PIL import Image
image = Image.open('../img/sample02.jpg').convert('RGB')
img4a = image.rotate(45, Image.ANTIALIAS)
img4a.save('rotate4a.png')
img4b = image.rotate(45, Image.BICUBIC)
img4c = image.rotate(45, Image.BILINEAR)
img4d = image.rotate(45, Image.NEAREST)
img4b.save('rotate4b.png')
img4c.save('rotate4c.png')
img4d.save('rotate4d.png')

image1 = Image.open('../img/sample01a.jpg').convert('RGB')
img4e = image1.transpose(Image.ROTATE_90) #長寬均依照新圖像的要求進行調整
img4e.save('transpose4e.png')
img4f = image1.rotate(45, Image.BICUBIC) #依現有影像空間進行調整，可能裁切或出現黑邊
img4f.save('rotate4f.png')