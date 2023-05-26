from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical

(Xtrain, ytrain), (Xtest, ytest) = cifar10.load_data()
print(Xtrain.shape)

Xtrain, Xtest = Xtrain/255, Xtest/255
ytrain, ytest = to_categorical(ytrain), to_categorical(ytest)
classes = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


model_training_first = models.Sequential([
    layers.Conv2D(32, (3, 3), input_shape=(32, 32, 3),
                  activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.15),  # cat bo bot

    layers.Conv2D(64, (3, 3), activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.2),

    layers.Conv2D(128, (3, 3), activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.2),

    layers.Flatten(),  # 32x32(3 layer)
    # 3072(input 32x32x3)->1000 -> 256 -> 10 (output) NN
    layers.Dense(1000, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')
])  # Seqential như chuỗi các ô vuông nối tiếp nhau (flatten)

model_training_first.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# opti: cập nhật lại , loss: mất mát,

model_training_first.fit(Xtrain, ytrain, epochs=10)
model_training_first.save('model_cifar10.h5')
