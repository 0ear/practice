import covid, covid2, covid4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from  sklearn.metrics import  confusion_matrix
print('---covid5.py開始執行---')
lb=covid2.lb
print('lb:',lb)
model=covid4.model
testX=covid4.testX
testY=covid4.testY
EPOCHS=covid4.EPOCHS
H=covid4.H
BS=covid4.BS
predidexs=model.predict(testX,batch_size=BS)
predidexs=np.argmax(predidexs,axis=1)
print(classification_report(testY.argmax(axis=1),predidexs,target_names=lb.classes_))
cm=confusion_matrix(testY.argmax(axis=1),predidexs)
print(cm)
print('-'*70)
total=sum(sum(cm))
acc=(cm[0,0]+cm[1,1])/total
sensitivity=cm[0,0]/(cm[0,0]+cm[0,1])
specificity=cm[1,1]/(cm[1,0]+cm[1,1])
print('準確率:',acc)
print('sensitivity:',sensitivity)
print('specificity:',specificity)
N=EPOCHS
plt.style.use('ggplot')
plt.figure()
print('以下為H的相關資料')
print(H.history.keys())
plt.plot(np.arange(0,N),H.history['loss'],label='train_loss')
plt.plot(np.arange(0,N),H.history['val_loss'],label='val_loss')
plt.plot(np.arange(0,N),H.history['accuracy'],label='train_accuracy')
plt.plot(np.arange(0,N),H.history['val_accuracy'],label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Loss/Accuracy')
plt.legend(loc='lower left')
plt.savefig('covid.png')
plt.show()
model.save('model.h5')