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

models = models.load_model('model_cifar10.h5')

np.random.shuffle(Xtest)

for i in range(50):
    plt.subplot(5, 10, i + 1)
    plt.imshow(Xtest[i])
    pred = models.predict(Xtest[i].reshape((-1, 32, 32, 3)))
    pred = np.argmax(pred)
    plt.title(classes[pred])
    plt.axis('off')

plt.show()
