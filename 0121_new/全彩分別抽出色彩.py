from PIL import  Image
import matplotlib.pyplot as plt
import numpy as np
image1 = Image.open('../img/r_to_b.png')
image = np.array(image1)
r = image[:,:,0]
print(r)
g = image[:,:,1]
print(g)
b = image[:,:,2]
print(b)
np.save('r1.npy', r)
np.save('g1.npy', g)
np.save('b1.npy', b)
print('若只有一個通道的影像，進行儲存')
r2 = Image.fromarray(r) #儲存的圖片會以灰階形式呈現
r2.save('r2.jpg')
g2 = Image.fromarray(r)
g2.save('g2.jpg')
b2 = Image.fromarray(r)
b2.save('b2.jpg')