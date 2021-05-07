from keras.optimizers import Adam
import  covid2,covid3
print('---covid4.py開始執行---')
INI_LR=1e-3
EPOCHS=25
BS=8
model=covid3.model
opt=Adam(lr=INI_LR,decay=INI_LR/EPOCHS)
model.compile(loss='binary_crossentropy',optimizer=opt,metrics=['accuracy'])
trainAug=covid2.trainAug
trainX=covid2.trainX
trainY=covid2.trainY
testX=covid2.testX
testY=covid2.testY
H=model.fit_generator(
    trainAug.flow(trainX,trainY,batch_size=BS),
    steps_per_epoch=len(trainX)//BS,
    validation_data=(testX,testY),
    validation_steps=len(testX)//BS,
    epochs=EPOCHS
)
