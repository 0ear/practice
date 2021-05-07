import covid
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
print('---covid2.py開始執行---')
lb = LabelBinarizer()
labels = covid.labels
data = covid.data
print('before')
print(labels)
print('-'*60)
print('針對labels進行訓練與轉換')
labels = lb.fit_transform(labels)
print('fit_transform')
print(labels)
print('-'*60)
print('再將轉換為數值資料的labels進行特徵設定')
labels = to_categorical(labels)
print('to_categorical')
print(labels)
print('-'*60)
print('進行訓練與測試資料的切割')
trainX, testX, trainY, testY = train_test_split(
    data, labels, test_size=0.2, stratify=labels,
    random_state=42
)
#print('trainX')
#print(trainX)
#print('-'*60)
#print('trainY')
#print(trainY)
trainAug = ImageDataGenerator(rotation_range=15, fill_mode='nearest')
