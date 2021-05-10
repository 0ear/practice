from skimage import data, exposure, img_as_float, io
import matplotlib.pyplot as plt
image = data.camera()
print(image)
arr = img.flatten()
n, bins, patches = plt.hist(arr, bins = 256, edgecolor = 'None',
                            facecolor = 'red')

