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
    layers.Flatten(input_shape=(32, 32, 3)),  # 32x32(3 layer)
    # 3072(input 32x32x3)->3000 -> 1000 -> 10 (output) NN
    layers.Dense(3000, activation='relu'),
    layers.Dense(1000, activation='relu'),
    layers.Dense(10, activation='softmax')
])  # Seqential như chuỗi các ô vuông nối tiếp nhau (flatten)

model_training_first.compile(
    optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])
# opti: cập nhật lại , loss: mất mát,

model_training_first.fit(Xtrain, ytrain, epochs=10)
model_training_first.save('model_cifar10.h5')
