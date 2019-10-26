from sklearn.metrics import accuracy_score
import numpy as np
import cv2
import tensorflow as tf

model = tf.keras.models.load_model('model_T96_B96.h5')
model.summary()


def proccess_letter_field(frame, size=12):
    frame = cv2.resize(frame, (12 * 50, 1 * 50), cv2.INTER_CUBIC)
    letters = np.hsplit(frame, 12)
    cells = []
    for l in letters:
        cells.append(l)
    cells = np.array(cells, dtype=np.float32)
    cells = cells[:, :, :, None]

    # Normalization
    cells = cells / 255.0

    # print(cells.shape)
    result = model.predict(cells)
    result = np.argmax(result, axis=1)
    print(result)


name = cv2.imread("name2.jpg", cv2.IMREAD_GRAYSCALE)
proccess_letter_field(name)



