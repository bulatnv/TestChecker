from sklearn.metrics import accuracy_score
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2
import tensorflow as tf

# Creating labels
k_labels = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
            'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']

def crop(frame):
    hight, width = frame.shape[:2]
    border_width = 8
    return frame[border_width: hight - border_width, border_width: width - border_width]


model = tf.keras.models.load_model('model_T96_B96.h5')
model.summary()


def proccess_letter_field(frame, size=12):
    frame = crop(frame)
    cv2.imshow("frame", frame)
    cv2.waitKey()
    frame = cv2.resize(frame, (size * 50, 1 * 50), cv2.INTER_CUBIC)
    letters = np.hsplit(frame, size)
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


name = cv2.imread("fathername.jpg", cv2.IMREAD_GRAYSCALE)
proccess_letter_field(name, 20)
