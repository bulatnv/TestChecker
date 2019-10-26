from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import os
import core
import glob
from pandas import DataFrame
from sys import platform


class Ui_MainWindow(object):
    def __init__(self):
        self.answers_lst = []
        self.jpg_files = []
        self.name = 'Ivan Ivanov'
        self.file_ico = glob.glob("Icons_for_main")
        self.file_ico = f"{os.path.abspath(os.path.dirname(sys.argv[0]))}/Icons_for_main/Icon_for_button.png"
        self.file_path_save_works = ''
        self.answers = dict()

    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(320, 200)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.setMenuBar(self.menubar)
        self.MainWindow.setStatusBar(self.statusbar)

        # self.pushButton.setGeometry(QtCore.QRect(320, 40, 75, 23))
        # self.pushButton_2.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.pushButton_3.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.lineEdit.setGeometry(QtCore.QRect(10, 42, 241, 23))
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 112, 241, 23))
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 16))
        self.label_2.setGeometry(QtCore.QRect(10, 90, 281, 16))
        self.pushButton_4.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.pushButton_5.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))

        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label.setObjectName("label")
        self.label_2.setObjectName("label_2")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5.setObjectName("pushButton_5")
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton.setObjectName("pushButton")
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit.setText("C:/")
        self.lineEdit_2.setText("C:/")

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton_3.clicked.connect(self.work_with_works)
        # self.pushButton.clicked.connect(self.connect_for_file_with_works)
        self.pushButton_5.clicked.connect(self.openFileNamesDialog)
        self.pushButton_4.clicked.connect(self.openFileNameDialog1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестировщик работ"))
        # self.pushButton.setText(_translate("MainWindow", "Сохранить путь"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить работы"))
        self.label.setText(_translate("MainWindow", "Путь к работам учасников"))
        self.label_2.setText(_translate("MainWindow", "Путь куда будут сохранены ответы учасников"))
        self.pushButton_4.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        # self.pushButton_2.setText(_translate("MainWindow", "Сохранить путь"))

        # self.pushButton.resize(self.pushButton.sizeHint())
        # self.pushButton_2.resize(self.pushButton_2.sizeHint())
        self.pushButton_3.resize(self.pushButton_3.sizeHint())
        self.pushButton_4.resize(self.pushButton_4.sizeHint())
        self.pushButton_5.resize(self.pushButton_5.sizeHint())
        if platform == "linux":
            self.label_2.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
            self.label.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
            self.label.resize(self.label.sizeHint())
            self.label_2.resize(self.label_2.sizeHint())
            self.lineEdit.setText("/home/ ")
            self.lineEdit_2.setText("/home/")

        self.MainWindow.show()

    def connect_for_file_with_works(self):  # Not Finish. Надо обрабоать ошибки1
        try:
            self.file_path = self.lineEdit.text()
            files = os.listdir(self.file_path)
        except FileNotFoundError:
            files = []
            self.file_path = ''
        for i in files:
            i = i.split(".")
            try:
                if i[1] == "jpg" or i[1] == "BMP" or i[1] == "png" or i[1] == 'bmp':
                    self.jpg_files.append(f"{i[0]}.jpg")
            except IndexError:
                pass
        print(files)
        files = []
        file_path = ''
        pass

    def connect_for_check_works(self):
        for i in self.jpg_files:
            print(f"{self.file_path}/{i}")
            for j in core.core(f"{self.file_path}/{i}").items():
                self.answers_lst.append(j[1])
            self.answers[self.name] = self.answers_lst
            self.answers_lst = []
            # self.answers = [1,2,3,4,5,6,7]

    def openFileNamesDialog(self):
        dir_name = Qt.QFileDialog.getExistingDirectory(
            None,
            "Open Directory",
            Qt.QDir.currentPath(),
            Qt.QFileDialog.ShowDirsOnly | Qt.QFileDialog.DontResolveSymlinks
        )
        if dir_name == '':
            pass
        else:
            self.lineEdit.setText(dir_name)

    def openFileNameDialog1(self):
        dir_name = Qt.QFileDialog.getExistingDirectory(
            None,
            "Open Directory",
            Qt.QDir.currentPath(),
            Qt.QFileDialog.ShowDirsOnly | Qt.QFileDialog.DontResolveSymlinks
        )
        if dir_name == '':
            pass
        else:
            self.lineEdit_2.setText(dir_name)
            self.file_path_save_works = dir_name

    def work_with_works(self):
        self.file_path = self.lineEdit.text()
        self.file_path_save_works = self.lineEdit_2.text()
        if self.file_path_save_works == '' or self.file_path == '':
            print("Error - \'Путь не указан\'")
        else:
            print(self.file_path_save_works)
            print(self.file_path)
            self.connect_for_file_with_works()
            self.connect_for_check_works()
            print("YES program-checker is work, answers:", self.answers)
            self.jpg_files = []
            print(self.answers)
            df = DataFrame(self.answers)
            print(df)
            df.to_excel(f'{self.file_path_save_works}/answers2.xlsx', sheet_name='sheet1', index=False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.__init__()
    ui.setupUi()
    sys.exit(app.exec_())
