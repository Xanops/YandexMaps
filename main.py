import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from interface import Ui_MainWindow
from picture import create_picture


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        create_picture()
        self.img = QLabel(self)
        self.img.move(0, 0)
        self.img.resize(450, 450)
        self.img.setPixmap(create_picture())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
