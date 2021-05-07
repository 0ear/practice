from skimage import io,data
import numpy as np
img = data.chelsea()
R = img[:, :, 0]
io.imshow(R)
io.show()
rows, cols, dims = img.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255
io.imshow(img)
io.show()