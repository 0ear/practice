from imutils import paths
import numpy as np
import cv2,os
print('---covid.py開始執行---')
import os
os.environ['KMP_WARNINGS'] = '0'
print('資料夾影像的載入')
imagePaths = list(paths.list_images('./dataset'))
#print(imagePaths)
data = []
labels = []
for imagePath in imagePaths:
    #print(imagePath)
    label = imagePath.split(os.path.sep)[-2]
    #print(os.path.sep)
    #print(label) #分類時的目標,代表是covid or normal
    image = cv2.imread(imagePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224,224))#轉換成相同大小
    data.append(image)
    labels.append(label)
data = np.array(data)/255.0
labels = np.array(labels)
print(labels)
print('執行結束一')
