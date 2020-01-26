import random
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb


class Examp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        our_pict = "flowers.jpg"
        our_pict = Image.open(our_pict)

        our_pict = our_pict.crop((0, 0, 150, 150)) # left, top, right, bottom

        our_pict = ImageQt(our_pict.convert('RGBA'))

        hbox = QHBoxLayout(self)
        our_pict = QPixmap.fromImage(our_pict)

        lbl = QLabel(self)
        lbl.setPixmap(our_pict)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example of crop')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Examp()
    sys.exit(app.exec_())
