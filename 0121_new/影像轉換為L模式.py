from PIL import  Image
import  numpy as np
im=Image.open('../img/b_to_w.jpg')#.convert('1') #可改1或L兩種模式
print(im.size,im.mode)
print('顯示1,1位置上顏色資訊:',im.getpixel((1,1)))
if im.mode=='RGB':
    print(np.array(im.getchannel(0))) #代表R
    print('-'*70)
    print(np.array(im.getchannel(1))) #代表G
    print('-'*70)
    print(np.array(im.getchannel(2))) #代表B
    print('-'*70)
elif im.mode=='1' or im.mode=='L':
    print(np.array(im.getchannel(0)))
    print('-' * 70)
