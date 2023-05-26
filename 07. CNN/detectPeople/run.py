import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

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

models = models.load_model('model_family10.h5')

face_detector = cv2.CascadeClassifier('')

cam = cv2.VideoCapture('review.mp4')

lstResult = ['Bich Thy', 'Ngoc Diep', 'Ngoc Phuong', 'Bich Pham', 'Tan Hoang']

while True:
    OK, frame = cam.read()
    faces = face_detector.detecMutilScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = cv2.resize(frame[y: y+h, x: x+w], (128, 128))
        result = np.argmax(models.predict(roi.reshape((-1, 128, 128, 3))))

        cv2.rectangle(frame, (x, y), (x+w, y+h), (128, 255, 50), 1)
        cv2.putText(frame, lstResult[result], (x+15, y-15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 25, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
