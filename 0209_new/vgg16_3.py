from keras.layers import Input, Flatten, Dense, Dropout
from  keras import optimizers
from  keras.preprocessing.image import  ImageDataGenerator
from keras.models import Model
import numpy as np
import vgg16_2
print('第三個檔案進行訓練')
model = vgg16_2.model
model.compile(
              loss='categorical_crossentropy',
              optimizer=optimizers.SGD(momentum=0.9),
              metrics=['accuracy'])
print('規劃即將攜帶到模型內的各項資訊')
img_width=vgg16_2.img_width #圖像的寬度
img_height=vgg16_2.img_height #圖像的高度
num_classes=vgg16_2.num_classes #分類的數量
train_data_dir=vgg16_2.train_data_dir #訓練的資料夾
validation_data_dir=vgg16_2.validation_data_dir #驗證的資料夾
print('每一次訓練與驗證抽查的樣本數量')
nb_train_samples=vgg16_2.nb_train_samples
nb_validation_samples=vgg16_2.nb_validation_samples
print('訓練時的次數與每次執行的數量')
epochs=vgg16_2.epochs
batch_size=vgg16_2.batch_size
input_shape=vgg16_2.input_shape
print('取得訓練的圖檔規劃')
train_datagen = ImageDataGenerator(rotation_range = 0.2, #旋轉
                                   shear_range = 0.2, #裁減
                                   zoom_range = 0.2, #放大縮小
                                   horizontal_flip = False #水平翻轉
                                   )
print('訓練步驟的規劃')
train_generator = train_datagen.flow_from_directory(train_data_dir,
                                                    target_size = (img_width, img_height),
                                                    batch_size = batch_size,
                                                    shuffle = False, #抽樣不放回
                                                    class_mode = 'categorical')
print('模型開始做訓練')
train_history = model.fit_generator(train_generator,
                                    steps_per_epoch = nb_train_samples//batch_size,
                                    epochs = epochs)