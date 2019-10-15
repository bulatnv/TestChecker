# TestChecker

Проект распознавания ответов участников полиолимпиады ОРБИТА

Основная идея:
Распознать ответы, распознать ФИО участника и др информацию и проверить результаты участия в олимпиаде.

Стек технологий:
Для этого предполагается использование сл стек технологий:
Linux (Ubuntu)
Python, pip, imutils, numpy и т.д.
OpenCV (для определения результатов)
Machine learning or Deep learning (для распознавания ФИО и др)
QT, pyQT ...
To be added

Ответники:
Предполагается что ответники будут сканироваться либо фотографироваться. Изображения требуют первоначальной обработки прежде чем распознаваться.

Как выглядит ответник в ОРБИТЕ:

Также, хорошо бы переработать дизайн ответника.


Image processing pipeline. Процесс обработки изображений.

Предобработка:
Подогнать изображение под приемлемые размеры (изображения должны быть соответствующего размера: не слишком большие)
Выявить лист ответника на изображении (края листа)
Применить трансформацию изображения (perspective transform) для выпрямления и образки листа.

Перевести изображение из цветного в градации серого, затем превратить в бинарный формат (черно-белый).

Автоматическое распознавание ФИО, номера телефона, класса ...
Далее OCR (Optical character recognition) - распознает Фамилию, Имя, Отчество, класс и т.д. Для этого предполагается использовать такие технологии как SVM (Support vector machines), deep learning, Keras, Tensorflow и т.д.

Для распознавания закрашенных кружочков применяем только OpenCV, можно как вариант Deep learning, Intel OpenVINO

https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/
https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/

Распознавание текста:
https://habr.com/ru/post/466565/ 
http://docs.openvinotoolkit.org/2019_R1/_text_recognition_0012_description_text_recognition_0012.html

Распознавание цифр:
https://habr.com/ru/company/ods/blog/335998/


Другие:

https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5
https://cloud.google.com/vision/docs/handwriting#vision-document-text-detection-python


Автоматическое распознавание ответов участников (и возможно проверка и подсчет результатов)

Разбивка ответов на группы

Определение и распознавание кружочков, закрашенного кружочка и определение отмеченного ответа.

https://www.pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/

На данный момент уже имеется ядро системы. 
