from PIL import Image
from skimage import io
img1 = Image.open('../img/sample02.jpg')
img2 = io.imread('../img/sample02.jpg')
print(img1.__class__) #出來是pil模式
print(img2.__class__) #出來是ndarray
print(img1.size)
print(img2.size)
print(img2.shape)  #skimage是將圖換成一numpy的ndarray

