from keras.applications.vgg16 import VGG16
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
import vgg16
print('第二個檔案進行規劃')
print('規劃vgg16物件')
model_vgg16_conv = VGG16(weights = 'imagenet', include_top = False)
print(model_vgg16_conv.summary())
print('規劃即將輸入到模型內的各項資訊')
img_width = vgg16.img_width #圖像寬度
img_height = vgg16.img_height #圖像高度
num_classes = vgg16.num_classes #分類的數量
train_data_dir = vgg16.train_data_dir #訓練的資料夾
validation_data_dir = vgg16.validation_data_dir #驗證的資料夾
print('每一次訓練與驗證抽查的樣本數量')
nb_train_samples = vgg16.nb_train_samples
nb_validation_samples = vgg16.nb_validation_samples
print('訓練時的次數與每次執行的數量')
epochs = vgg16.epochs
batch_size = vgg16.batch_size
input_shape = vgg16.input_shape
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
