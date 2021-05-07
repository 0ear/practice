from  keras.applications.vgg16 import  VGG16
from  keras.applications.vgg16 import  preprocess_input
from  keras.preprocessing.image import  load_img
from  keras.preprocessing.image import  img_to_array
from  keras.models import  Model
import  matplotlib.pyplot as plt
from  numpy import  expand_dims
model=VGG16()
model=Model(inputs=model.inputs,outputs=model.layers[1].output)
model.summary()
img=load_img('luffy.jpg',target_size=(224,224)) #summary 預設
img=img_to_array(img)
print(img)
print(img.shape)
img=expand_dims(img,axis=0)
print(img)
print(img.shape)
img=preprocess_input(img)
feature_maps=model.predict(img)
square=8
ix=1
for _ in range(square):
    for _ in range(square):
        ax=plt.subplot(square,square,ix)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.imshow(feature_maps[0,:,:,ix-1],cmap='gray')
        ix+=1
plt.show()