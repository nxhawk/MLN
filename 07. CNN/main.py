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

pred = models.predict(Xtest[105].reshape((-1, 32, 32, 3)))
print(pred)
print(classes[np.argmax(pred)])
plt.imshow(Xtest[105])
plt.show()
