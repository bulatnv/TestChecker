from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys
import os
import core

class Ui_MainWindow(object):
    def __init__(self):
        self.jpg_files = []
        self.file_ico = os.path.abspath('Icons_for_main\\Icon_for_button.png') 
    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(500, 246)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
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

        self.pushButton.setGeometry(QtCore.QRect(320, 40, 75, 23))
        self.pushButton_2.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.pushButton_3.setGeometry(QtCore.QRect(70, 170, 75, 23))
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 241, 20))
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 241, 20))
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.setObjectName("pushButton")
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit.setText("C:\\")
        self.lineEdit_2.setText("C:\\")

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton_3.clicked.connect(self.connect_for_pushButton_debug1)
        self.pushButton.clicked.connect(self.connect_for_pushButton_debug)
        self.pushButton_5.clicked.connect(self.openFileNamesDialog)
        self.pushButton_4.clicked.connect(self.openFileNameDialog1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестировщик работ"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить путь"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить работы"))
        self.label.setText(_translate("MainWindow", "Путь к работам учасников"))
        self.label_2.setText(_translate("MainWindow", "Путь куда будут сохранены ответы учасников"))
        self.pushButton_4.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_4.setIconSize(QtCore.QSize(20,20))
        self.pushButton_5.setIcon(QtGui.QIcon(self.file_ico))
        self.pushButton_5.setIconSize(QtCore.QSize(20,20))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить путь"))
        self.pushButton_3.move(40, 170)

        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton_2.resize(self.pushButton_2.sizeHint())
        self.pushButton_3.resize(self.pushButton_3.sizeHint())
        self.pushButton_4.resize(self.pushButton_4.sizeHint())
        self.pushButton_5.resize(self.pushButton_5.sizeHint())

        self.MainWindow.show()

    def connect_for_pushButton_debug(self, MainWindow):  # Not Finish. Надо обрабоать ошибки1
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

    def connect_for_pushButton_debug1(self, MainWindow):  # Not Finish. Надо обрабоать ошибки
        for i in self.jpg_files:
            print(f"{self.file_path}/{i}")
            core.core(f"{self.file_path}/{i}")

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
                self.pushButton.click()
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
            self.lineEdit.setText(dir_name)
            self.pushButton.click()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.__init__()
    ui.setupUi()
    sys.exit(app.exec_())
