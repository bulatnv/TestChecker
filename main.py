# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import glob
import os
import sys
import core
import csv

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(181, 89)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.label.setText(_translate("self", "Работа звершена"))
        self.pushButton.setText(_translate("self", "OKEY"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 235)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 370, 189))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестер работ"))
        self.label_3.setText(_translate("MainWindow", "Путь к таблице с правильными ответами"))
        self.label.setText(_translate("MainWindow", "Путь куда будет сохраннена таблица с результатами"))
        self.label_2.setText(_translate("MainWindow", "Путь к работам"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить работы"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        self.filePathJpg = []
        super().__init__()
        self.setupUi(self)
        self.aboutProject = QtWidgets.QAction('&About Project', self)
        # self.aboutProject.setShortcut('Ctrl+Q')
        self.aboutProject.setStatusTip('About Project')
        # self.aboutProject.triggered.connect(QtWidgets.qApp.quit)

        self.help = QtWidgets.QAction('&Help', self)
        # self.help.setShortcut('Ctrl+Q')
        self.help.setStatusTip('Help new users')
        # self.help.triggered.connect(QtWidgets.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Menu')
        fileMenu.addAction(self.aboutProject)
        fileMenu.addAction(self.help)

        self.file_ico = glob.glob("Icons_for_main")
        self.file_ico = f"{os.path.abspath(os.path.dirname(sys.argv[0]))}/Icons_for_main/Icon_for_button.png"
        print(self.file_ico)

        self.label_2.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.label.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))
        self.label_3.setFont(QtGui.QFont("Times", 9, QtGui.QFont.Bold))

        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setIconSize(QtCore.QSize(20, 20))

        self.pushButton.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_4.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_2.setIcon(QtGui.QIcon(self.file_ico))

        if 'linux' in sys.platform:
            self.lineEdit.setText('/home/')
            self.lineEdit_2.setText('/home/')
            self.lineEdit_3.setText(('/home/'))
        elif 'windows' in sys.platform:
            self.lineEdit_3.setText('C:/')
            self.lineEdit.setText('C:/')
            self.lineEdit_2.setText('C:/')

        self.pushButton_4.clicked.connect(self.openFileNamesDialog_tree)
        self.pushButton.clicked.connect(self.openFileNamesDialog)
        self.pushButton_2.clicked.connect(self.openFileNamesDialog_two)
        self.pushButton_3.clicked.connect(self.workWithWork)

    def workWithWork(self):
        self.answers = []
        self.name_answer_dct = dict()
        try:
            self.file_path = self.lineEdit.text()
            files = os.listdir(self.file_path)
        except FileNotFoundError:
            print("Путь не найден")
        if files != []:
            for i in files:
                file = i.split('.')
                print(file)
                if file[-1] == 'jpg':
                    self.filePathJpg.append(f"{file[0]}.jpg")
        #print("jpg")
        #print(self.filePathJpg)

        for i in self.filePathJpg:
            #print(f'{self.lineEdit.text()}/{i}')
            a = core.core(f"{self.lineEdit.text()}/{i}")
            #print(a)
            FIO = f"{a[1]} {a[0]} {a[2]}"
            #print(FIO)
            #print(a[3])
            keys = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E'}
            with open(f'{self.lineEdit_3.text()}/answers.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for index, row in enumerate(reader):
                    trueAns = row
                    break

            for i in a[3].items():
                if i[1] != '-1' and len(i[1]) == 1:
                    item = keys[i[1]]
                elif i[1] == '-1':
                    item = 'No answer'
                else:
                    pass
                self.answers.append(item)
            b = trueAns[0].split(",")
            print(b)
            true = 0
            for j in range(len(self.answers) - 1):
                if self.answers[j] == b[j]:
                    true+=1
            print(self.answers)
            print(len(self.answers))
            self.answers.append(f'{true+1}/{len(self.answers)}')
            self.name_answer_dct[FIO] = self.answers

        print(self.name_answer_dct)
        filepath = os.path.join(f'{self.lineEdit_2.text()}', 'answers.csv')
        self.csv_dict_writer(filepath, self.name_answer_dct)
        self.a = Ui_Form()
        self.a.setupUi()
        self.a.show()
        self.a.pushButton.clicked.connect(self.a.close)
    def csv_dict_writer(self, path, data):
        open(path, 'a').close()
        with open(path, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in data.items():
                writer.writerow([key, *value])

    def openFileNamesDialog(self):
        dir_name = Qt.QFileDialog.getExistingDirectory(
            None,
            "Open Directory",
            Qt.QDir.currentPath(),
            Qt.QFileDialog.ShowDirsOnly | Qt.QFileDialog.DontResolveSymlinks
        )
        if dir_name == '':
            print("Пустой путь")
        else:
            self.lineEdit.setText(dir_name)

    def openFileNamesDialog_two(self):
        dir_name = Qt.QFileDialog.getExistingDirectory(
            None,
            "Open Directory",
            Qt.QDir.currentPath(),
            Qt.QFileDialog.ShowDirsOnly | Qt.QFileDialog.DontResolveSymlinks
        )
        if dir_name == '':
            print("Пустой путь")
        else:
            self.lineEdit_2.setText(dir_name)

    def openFileNamesDialog_tree(self):
        dir_name = Qt.QFileDialog.getExistingDirectory(
            None,
            "Open Directory",
            Qt.QDir.currentPath(),
            Qt.QFileDialog.ShowDirsOnly | Qt.QFileDialog.DontResolveSymlinks
        )
        if dir_name == '':
            print("Пустой путь")
        else:
            self.lineEdit_3.setText(dir_name)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
