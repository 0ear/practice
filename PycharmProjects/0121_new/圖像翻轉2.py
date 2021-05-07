from  PIL import  Image
import  matplotlib.pyplot as plt
import  numpy as np
image=Image.open("../img/sample01a.jpg").convert('1')
image2=np.transpose(image)
plt.imshow(image2)
plt.axis('off')
plt.show()
plt.imshow(image2,cmap='gray') #灰階影像要加cmap='gray'
plt.axis('off')
plt.show()
