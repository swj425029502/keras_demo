from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator as img

train_dir="E:\Project\Keras_Demo\\2019\dataset\cats_and_dogs_small\\train"
test_dir="E:\Project\Keras_Demo\\2019\dataset\cats_and_dogs_small\\test"
val_dir="E:\Project\Keras_Demo\\2019\dataset\cats_and_dogs_small\\validation"


model=models.Sequential()
model.add(layers.Conv2D(96,(11,11),strides=4,activation="relu",input_shape=(150,150,3)))
model.add(layers.MaxPooling2D((3, 3),strides=2))
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(256, (5, 5), activation='relu',strides=1,padding="same"))
model.add(layers.MaxPooling2D((3, 3),strides=2))
model.add(layers.BatchNormalization())
model.add(layers.Conv2D(384, (3, 3), activation='relu',strides=1,padding="same"))
model.add(layers.Conv2D(384, (3, 3), activation='relu',strides=1,padding="same"))
model.add(layers.Conv2D(256, (3, 3), activation='relu',strides=1,padding="same"))
model.add(layers.MaxPooling2D((3, 3),strides=2))
model.add(layers.Flatten())
model.add(layers.Dense(4096,activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(4096,activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1,activation='sigmoid'))
model.summary()
model.compile(loss='binary_crossentropy',optimizer=optimizers.RMSprop(lr=1e-4),metrics=['acc'])


train_datagen=img(rescale=1./255)
test_datagen=img(rescale=1./255)

train_generator=train_datagen.flow_from_directory(train_dir,target_size=(150,150),batch_size=20,class_mode='binary')
# test_generator=test_datagen.flow_from_directory(test_dir,target_size=(150,150),batch_size=20,class_mode='binary')
val_generator=test_datagen.flow_from_directory(val_dir,target_size=(150,150),batch_size=20,class_mode='binary')

history = model.fit_generator(
 train_generator,
 steps_per_epoch=100,
 epochs=30,
 validation_data=val_generator,
 validation_steps=50)

model.save('cats_and_dogs_small_1.h5')

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()