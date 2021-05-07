import matplotlib1
import matplotlib.pyplot as plt
image = matplotlib1.image
img_g = image[:, :, 1]
plt.imshow(img_g)
plt.axis('off')
#plt.show()
plt.imshow(img_g, cmap= 'Greys_r')
#plt.show()
print('儲存')
plt.savefig('./graph/3.png')
plt.savefig('./graph/3.jpg')
plt.show() #須放在savefig後 不然存的圖片會變空白
plt.imsave('./graph/3a.jpg', img_g)