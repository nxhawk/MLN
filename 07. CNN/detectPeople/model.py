import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import tensorflow
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical


TRAIN_DATA = 'datasets/train-data'
TEST_DATA = 'datasets/test-data'

Xtrain = []
ytrain = []

Xtest = []
ytest = []

dict = {'posBThy': [1, 0, 0, 0, 0], 'posNDiep': [0, 1, 0, 0, 0],
        'posNPhuong': [0, 0, 1, 0, 0], 'posTBich': [0, 0, 0, 1, 0],
        'posTHoang': [0, 0, 0, 0, 1],
        'testBThy': [1, 0, 0, 0, 0], 'testNDiep': [0, 1, 0, 0, 0],
        'testNPhuong': [0, 0, 1, 0, 0], 'testTBich': [0, 0, 0, 1, 0],
        'testTHoang': [0, 0, 0, 0, 1]
        }


def getData(dirData, lstData):
    for whatever in os.listdir(dirData):
        whatever_path = os.path.join(dirData, whatever)
        lst_filename_path = []
        for filename in os.listdir(whatever_path):
            filename_path = os.path.join(whatever_path, filename)
            img = np.array(Image.open(filename_path))
            lst_filename_path.append((img, dict[whatever]))

        lstData.extend(lst_filename_path)
    return lstData


Xtrain = getData(TRAIN_DATA, Xtrain)
Xtest = getData(TEST_DATA, Xtest)

model_training_first = models.Sequential([
    layers.Conv2D(32, (3, 3), input_shape=(128, 128, 3),
                  activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.15),  # cat bo bot

    layers.Conv2D(64, (3, 3), activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.2),

    layers.Conv2D(128, (3, 3), activation='relu'),  # 32kernel, kernel size = 3
    layers.MaxPool2D((2, 2)),
    layers.Dropout(0.2),

    layers.Flatten(),  # 32x32(3 layer) phang du lieu
    # 3072(input 32x32x3)->1000 -> 256 -> 10 (output) NN
    layers.Dense(1000, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(5, activation='softmax')
])  # Seqential như chuỗi các ô vuông nối tiếp nhau (flatten)

# model_training_first.summary()

# ---------------------------------------------
model_training_first.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# opti: cập nhật lại , loss: mất mát,

model_training_first.fit(np.array([x[0] for _, x in enumerate(Xtrain)]),
                         np.array([y[0] for _, y in enumerate(Xtrain)]), epochs=10)

model_training_first.save('model_family10.h5')

models = models.load_model('model_family10.h5')

