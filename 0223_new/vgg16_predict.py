import numpy as np
from keras.models import Sequential, model_from_json
from keras.models import load_model, Model
import os
import keras
from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.layers import Input, Flatten, Dense, Dropout
from keras.applications.vgg16 import preprocess_input
print('先載入檔案')
with open('myvgg16.config', 'r') as text_file:
    json_string = text_file.read()

print('規劃vgg16物件')
model_vgg16_conv = VGG16(weights = 'imagenet', include_top = False)
print(model_vgg16_conv.summary())
print('規劃即將輸入到模型內的各項資訊')
img_width = 224 #圖像寬度
img_height = 224 #圖像高度
num_classes = 2 #分類的數量
input_shape = (img_height, img_width, 3)

print('規劃輸入層')
input = Input(shape = input_shape, name = 'image_input')

print('卷積層')
output_vgg16_conv = model_vgg16_conv(input)
print('完全連接層，代表即將要進行分類')
x = Flatten(name = 'flatten')(output_vgg16_conv)
x = Dense(4096, activation='relu', name = 'fc1')(x)
x = Dense(256, activation='relu', name = 'fc2')(x)
x = Dense(num_classes, activation='softmax', name = 'predictions')(x)
model = Model(inputs = input, outputs = x)
print(model.summary())
model.summary()
model.load_weights('myvgg16.weight', by_name= False)
print('設定要預測的圖像')
img_path = './sample/train/dogs/dog.1.jpg'
img = image.load_img(img_path, target_size = (224, 224))
x1 = image.img_to_array(img) #圖像轉為矩陣
x1 = np.expand_dims(x1, axis =0)
labels = ['cat', 'dog']
predictions = model.predict(x1)
print('預測的類別:', labels[np.argmax(predictions)])
print('預測的比率:', predictions.ravel())