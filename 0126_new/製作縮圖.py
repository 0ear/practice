from PIL import Image
im = Image.open('../img/sample01.jpg').convert('RGB')
print(im.size)
im.thumbnail((400,100))
im.save('thumbnail.jpg')
print(im.size)