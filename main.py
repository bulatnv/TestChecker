from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import core


class Ui_MainWindow(object):
    def __init__(self):
        self.jpg_files = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 246)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 170, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 241, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 281, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 170, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.connect_for_pushButton_debug1)
        self.pushButton.clicked.connect(self.connect_for_pushButton_debug)
        self.pushButton_5.clicked.connect(self.connect_for_pushButton_debug1)
        self.pushButton_4.clicked.connect(self.connect_for_pushButton_debug)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестировщик работ"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить путь"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить работы"))
        self.label.setText(_translate("MainWindow", "Путь к работам учасников"))
        self.label_2.setText(_translate("MainWindow", "Путь куда будут сохранены ответы учасников"))
        self.pushButton_4.setText(_translate("MainWindow", "debug"))
        self.pushButton_5.setText(_translate("MainWindow", "debug1"))

        self.pushButton_3.move(40, 170)

        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton_2.resize(self.pushButton_2.sizeHint())
        self.pushButton_3.resize(self.pushButton_3.sizeHint())
        self.pushButton_4.resize(self.pushButton_4.sizeHint())
        self.pushButton_5.resize(self.pushButton_5.sizeHint())

    def connect_for_pushButton_debug(self, MainWindow):

        global files
        try:
            self.file_path = self.lineEdit.text()
            files = os.listdir(self.file_path)
        except FileNotFoundError:
            pass
        for i in files:
            i = i.split(".")
            try:
                if i[1] == "jpg":
                    self.jpg_files.append(f"{i[0]}.jpg")
            except IndexError:
                pass
        print(files)
        files = []
        file_path = ''
        pass

    def connect_for_pushButton_debug1(self, MainWindow):
        for i in self.jpg_files:
            print(f"{self.file_path}/{i}")
            core.core(f"{self.file_path}/{i}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.__init__()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
