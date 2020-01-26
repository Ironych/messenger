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

        imageFile = "flowers.jpg"
        our_pict = Image.open(imageFile)

        width = 900
        height = 647

        our_pict = our_pict.resize((width, height), Image.NEAREST) # change size

        our_pict = ImageQt(our_pict.convert('RGBA'))

        hbox = QHBoxLayout(self)
        our_pict = QPixmap.fromImage(our_pict)

        label = QLabel(self)
        label.setPixmap(our_pict)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Example of resize')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Examp()
    sys.exit(app.exec_())


'''
"Nearest neighbor". Быстрейший и худший метод, поскольку используется попросту значение
 бижайшей точки исходной картинки. По сути, часть точек отбрасывается (при уменьшении)
 либо дуплицируется (при увеличении).

"Bilinear". В обоих направлениях проводится линейная интерполяция (используется 2х2 матрица,
 то есть 4 ближайших точки). Быстрый и неплохой метод, слегка сглаживающий картинку, однако
 при больших увеличениях начинает проявляться блочная структура.

"Bicubuc". В обоих направлениях проводится кубическая интерполяция
 (по матрице 4х4, то есть используется 16 ближайших точек), дает более резкую картинку.
 При увеличении дает значительно лучший результат, чем билинейный метод.
 Поскольку детали прорисовываются четче, усиливаются и шумы, то есть картинки
 с шумами нужно увеличивать очень осторожно. Значительно медленнее, чем билинейный фильтр.
'''
