import vgg16_3
print('即將進行儲存訓練結果')
model = vgg16_3.model
model.save('myvgg16.h5')
model.save_weights('myvgg16.weight')
from keras.models import model_from_json
json_string = model.to_json()
with open('myvgg16.config', 'w') as text_file:
    text_file.write(json_string)