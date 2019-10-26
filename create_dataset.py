import cv2
import numpy as np

# number of letters in image
width = 10
hight = 33
resolution = 50


def split_image(frame):
    cs = []
    rows = np.vsplit(frame, hight)
    for row in rows:
        row_cs = np.hsplit(row, width)
        for c in row_cs:
            cs.append(c)
    return cs


def process_frame(frame):
    image = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (width * resolution, hight * resolution))
    return np.array(split_image(image), dtype=np.float32)


def prepare_test_data(frame):
    test = cv2.imread(frame, cv2.IMREAD_GRAYSCALE)
    test = cv2.resize(test, (1 * 50, 33 * 50))
    test_letters = np.vsplit(test, 33)
    test_cells = []
    for d in test_letters:
        # d = d.flatten()
        test_cells.append(d)
    return np.array(test_cells, dtype=np.float32)


def save_dataset(dataset, labels):
    if len(dataset) == len(labels):
        dataset.save('dataset.dat')
        labels.save('labels.dat')
        # f = open("dataset/labels.txt", "w+")
        # f.write(str(len(labels)) + "\n")
        # for i in range(len(labels)):
        #     f.write(str(i) + " " + str(labels[i]) + '\n')
        #     cv2.imwrite("dataset/" + str(i) + ".png", dataset[i])
        # f.close()

    else:
        print("Error in saving dataset, images and labels are not equal")


def load_dataset():
    dataset = np.fromfile('dataset.dat', dtype='>f8')
    labels = np.fromfile('labels.dat', dtype=int)
    # labels = []
    # dataset = []
    # f = open("dataset/labels.txt", "r")
    # quantity = int(f.readline())
    # for i in range(quantity):
    #     name, label = map(int, f.readline().split())
    #     c = cv2.imread("dataset/" + str(name) + ".png", cv2.IMREAD_GRAYSCALE)
    #     labels.append(label)
    #     dataset.append(c)
    # f.close()
    return dataset, labels


def test_dataset(cells, labels, number):
    print(labels[number])
    cv2.imshow("example", cv2.UMat(cells[number]))
    cv2.waitKey()


def create_new_dataset():
    filePath = "dataset_raw/processed"
    fileType = ".bmp"
    cells = process_frame(filePath + str(0) + fileType)

    k = range(33)
    label = np.repeat(k, width)
    labels = label

    for i in range(1, 77):
        cells1 = process_frame(filePath + str(i) + fileType)
        cells = np.concatenate((cells, cells1), axis=0)
        labels = np.concatenate((labels, label), axis=None)

    # Saving new dataset
    save_dataset(cells, labels)


k_labels = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
            'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ы', 'Ъ', 'Э', 'Ю', 'Я']

# example command to procces new images and create new dataset
create_new_dataset()

# example how to load dataset
# dataset, labels = load_dataset()
# test_dataset(dataset, labels, 0)
