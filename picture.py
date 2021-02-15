from PyQt5.QtGui import QPixmap

from url import url


def create_picture():
    pixmap = QPixmap()
    pixmap.loadFromData(url())
    return pixmap
