import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train.to_html('train.html')
test.to_html('test.html')

#針對訓練與測試的資料進行整理
y_train = train['label']
X_train = train.drop(train.columns[[0]], axis = 1)
X_test = test
#先忽略產生樣本進行查看的步驟
#產生訓練與測試的圖像資料 1代表一個通道,代表灰階
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_train.shape[0], 28, 28, 1)
print('於資料外面上下左右各加入2 pixels的空間,避免之後捲積層處理遺漏邊線')
X_train = np.pad(X_train, ((0, 0), (2, 2), (2, 2), (0, 0)), 'constant')
X_test = np.pad(X_test, ((0, 0), (2, 2), (2, 2), (0, 0)), 'constant')

print('進行標準化')
mean_px = X_train.mean().astype(np.float32)
std_px = X_train.std().astype(np.float32)
X_train = (X_train - mean_px)/(std_px)
print('訓練的資料目標,訓練的資料標籤得進行編碼encoding')
print('編碼後沒有大小差別')
from keras.utils.np_utils import to_categorical
y_train = to_categorical(y_train)

print('以下為模型的準備')


print('執行模型訓練')

print('預估與結果儲存')