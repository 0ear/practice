#import nogpu
#nogpu.gu()
print('圖的準備工作')
img_width,img_height = 224, 224
train_data_dir = './sample/train'
validation_data_dir = './sample/valid'
nb_train_samples = 1000
nb_validation_samples = 400
epochs = 150
batch_size = 20
input_shape= (img_width, img_height, 3)
num_classes = 2 #分貓狗兩種
