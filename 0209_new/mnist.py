from keras.datasets import mnist
import nogpu
nopgu.nopgu()
import warnings
print('處理tensorflow偵測numpy版本的錯誤訊息')
print('以下語法會遮住所有警告訊息')
warnings.filterwarnings('ignore')
print(help(mnist))
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train) #訓練的資料
print('-' *70)
print(y_train)