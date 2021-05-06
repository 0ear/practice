from PIL import Image
im = Image.open('../img/sample02.jpg').convert('RGB')
box = (240, 195, 760, 700)
image_crop = im.crop(box)
im3 = Image.new('RGBA', (800, 800), (125, 125, 125, 0))
im3.paste(image_crop, (100, 50))
im3.save('sample02new.png')