from PIL import Image
image = Image.open('../img/house_input.png').convert('RGB')
image2 = image.convert('L')
print(image.size)
print(image.mode)
print(image2.size)
print(image2.mode)
image2.save('house3.png')