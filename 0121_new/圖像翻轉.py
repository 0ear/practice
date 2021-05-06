from PIL import Image
import  matplotlib.pyplot as plt
import numpy as np
image = Image.open(('../img/sample02.jpg'))
image2 = np.flipud(image) #上下翻轉
image3 = np.fliplr(image) #左右翻轉
plt.imshow(image2)
plt.axis('off')
plt.show()
