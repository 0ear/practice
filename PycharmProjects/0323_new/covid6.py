from keras.models import  load_model
from imutils import  paths
import  numpy as np
import  cv2,os
print('1.請先確認模型是否可以載入')
model=load_model('model.h5')
model.summary()
print('---covid1.py開始執行---')
#import  os
#os.environ['KMP_WARNINGS']='0'
print('資料夾影像的載入')
imagePaths=list(paths.list_images('./demoset'))
data=[]
labels=[]
for imagePath in imagePaths:
    image=cv2.imread(imagePath)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=cv2.resize(image,(224,224)) #轉換為相同大小
    data.append(image)
data=np.array(data)/255.0
print(data.shape)
labels.append('covid')
labels.append('normal')
labels=np.array(labels)
print(labels)
print('執行結束1')
from  keras.utils import  to_categorical
from sklearn.preprocessing import  LabelBinarizer
print('---covid2.py開始執行---')
lb=LabelBinarizer()
print('before')
print(labels)
print('-'*60)
print('針對labels進行encode訓練與轉換')
labels=lb.fit_transform(labels)
print('fit_transform')
print(labels)
print('-'*60)
print('再將轉換為數值資料的labels進行特徵設定')
labels=to_categorical(labels)
print('to_categorical')
print(labels)
print('-'*60)
print('執行結束2')
import  numpy as np
print('---covid5.py開始執行---')
predidexs=model.predict(data,batch_size=8)
print("data:\n",data)
print("predidexs:\n",predidexs)
predidexs=np.argmax(predidexs,axis=1)
print("np.argmax:\n",predidexs)
for i in predidexs:
    if i==0:
        print('covid')
    else:
        print('normal')