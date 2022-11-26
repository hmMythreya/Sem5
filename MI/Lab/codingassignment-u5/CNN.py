import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, ReLU, Flatten, Dense
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

img_gen = ImageDataGenerator(
    width_shift_range=0.1, height_shift_range=0.1, horizontal_flip=True, rotation_range = 30, rescale = 1./255)
train_gen = img_gen.flow(x_train, y_train, batch_size = 32)
test_gen = img_gen.flow(x_test, y_test)

model = models.Sequential()
model.add(Conv2D(32, kernel_size=(3,3), strides=(1,1),padding='same', activation='relu', input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(ReLU())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(64, kernel_size=(3,3), strides=(1,1),padding='same', activation='relu', input_shape=(16,16,32)))
model.add(BatchNormalization())
model.add(ReLU())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(128, kernel_size=(3,3), strides=(1,1),padding='same', activation='relu', input_shape=(8,8,64)))
model.add(BatchNormalization())
model.add(ReLU())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(256, kernel_size=(3,3), strides=(1,1),padding='same', activation='relu', input_shape=(4,4,128)))
model.add(BatchNormalization())
model.add(ReLU())
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

steps_per_epoch = x_train.shape[0] // 32
r = model.fit(train_gen, steps_per_epoch=steps_per_epoch,
                    validation_data=test_gen, epochs = 20)

model.evaluate(test_gen)
model.summary()

model.save("./PES2UG20CS130.h5")

model_n=tf.keras.models.load_model("./PES2UG20CS130.h5")
model_n.summary()

tf.keras.utils.plot_model(model, to_file="my_model.png", show_shapes=True)

