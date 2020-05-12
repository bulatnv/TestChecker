from sklearn.metrics import accuracy_score
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2
import tensorflow as tf

# Creating labels
l_labels = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
            'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']
d_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def crop(frame):
    hight, width = frame.shape[:2]
    border_width = 8
    return frame[border_width: hight - border_width, border_width: width - border_width]


# model_T96_B96.h5
# model_0_9633_.h5
# model_0_9646_.h5
letter_model = tf.keras.models.load_model('model_0_9646_.h5')
# letter_model.summary()


digit_model = tf.keras.models.load_model('digitsFF_0_9868.h5')


def process_letter_field(frame, size):
    frame = crop(frame)
    # cv2.imshow('frame', frame)
    # cv2.waitKey()
    frame = cv2.resize(frame, (size * 50, 1 * 50), cv2.INTER_CUBIC)
    letters = np.hsplit(frame, size)
    cells = []
    for l in letters:
        count_white_pixels = cv2.countNonZero(l)
        if count_white_pixels > 275:
            cells.append(l)
    cells = np.array(cells, dtype=np.float32)
    if len(cells) == 0:
        return None
    cells = cells[:, :, :, None]

    # Normalization
    cells = cells / 255.0
    # print(cells.shape)

    result = letter_model.predict(cells)
    result = np.argmax(result, axis=1)
    return ''.join(map(lambda i: l_labels[i], result))


def process_digit_field(frame, size):
    frame = crop(frame)
    # cv2.imshow('frame', frame)
    # cv2.waitKey()
    frame = cv2.resize(frame, (size * 50, 1 * 50), cv2.INTER_CUBIC)
    letters = np.hsplit(frame, size)
    cells = []
    for l in letters:
        count_white_pixels = cv2.countNonZero(l)
        if count_white_pixels > 200:
            cells.append(l)
    cells = np.array(cells, dtype=np.float32)
    if len(cells) == 0:
        return None
    cells = cells[:, :, :, None]

    # Normalization
    cells = cells / 255.0
    # print(cells.shape)

    result = digit_model.predict(cells)
    result = np.argmax(result, axis=1)
    return ''.join(map(lambda i: d_labels[i], result))


def process_answer_field(frame):
    frame = crop(frame)
    # cv2.imshow('frame', frame)
    # cv2.waitKey()
    frame = cv2.resize(frame, (23 * 50, 30 * 50), cv2.INTER_CUBIC)
    letters = np.hsplit(frame, 23)
    cells = []
    for l in letters:
        count_white_pixels = cv2.countNonZero(l)
        if count_white_pixels > 200:
            cells.append(l)
    cells = np.array(cells, dtype=np.float32)
    if len(cells) == 0:
        return None
    cells = cells[:, :, :, None]

    # Normalization
    cells = cells / 255.0
    # print(cells.shape)

    result = digit_model.predict(cells)
    result = np.argmax(result, axis=1)
    return ''.join(map(lambda i: d_labels[i], result))
