from PIL import Image
import  matplotlib.pyplot as plt
image = Image.open(('../img/sample01a.jpg'))
plt.imshow(image)
plt.axis('off')
plt.show()