import numpy as np
x = np.array([1.43, 288.3, -5.6, 512])
print(x)
print(x.dtype)
print('若數值資料想要轉換為圖像,值需要介於0~255間')
y = x.astype('uint8') #會限制值在0~255間,>255的值就-256,<0的就+256
print(y)
print(y.dtype)