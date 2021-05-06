from PIL import  Image
import  numpy as np
#im=Image.open('../img/ABC.bmp').convert('L')
im=Image.open('../img/sample01a.jpg').convert('L')
im.save('change1.png')
imarray1=np.array(im.getchannel(0))
print(imarray1)
imarray2=255-imarray1
print(imarray2)
im2=Image.fromarray(imarray2)
im2.save('change2.png')

