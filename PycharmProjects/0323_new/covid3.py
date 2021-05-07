print('針對深度學習vgg16進行模型規劃並沒有帶入資料')
import nogpu
print('---covid3.py開始執行---')
nogpu.nogpu()
from keras.applications import VGG16
from keras.layers import Input, Dropout, Flatten, Dense, AveragePooling2D
from keras.models import Model
baseModel = VGG16(weights = 'imagenet', include_top = False,
                  input_tensor = Input(shape = (224, 224, 3)))
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(4, 4))(headModel)
headModel = Flatten(name = 'flatten')(headModel)
headModel = Dense(64, activation= 'relu')(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(2, activation= 'softmax')(headModel)
model = Model(inputs = baseModel.input, outputs = headModel)
for layer in baseModel.layers:
    layer.trainable = False
