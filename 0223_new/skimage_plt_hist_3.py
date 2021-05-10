from skimage import data, exposure, img_as_float, io
import matplotlib.pyplot as plt
image = io.imread('rgb.jpg')
print(image)
arr = img[:, :, 0].flatten()
plt.hist(arr, bins = 256, edgecolor = 'red',facecolor = 'red')
plt.show()
arr = img[:, :, 1].flatten()
plt.hist(arr, bins = 256, edgecolor = 'green',facecolor = 'green')
plt.show()
arr = img[:, :, 2].flatten()
plt.hist(arr, bins = 256, edgecolor = 'blue',facecolor = 'blue')
plt.show()