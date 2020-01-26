#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton,  QFrame,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon, QColor, qRgb, QImage
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.fname = 'image.jpg'
        self.setWindowIcon(QIcon('roller_brush_48px.png'))
        self.image = Image.open(self.fname)
        self.lbl = QLabel(self)

        openFile = QAction(QIcon('opened_folder_48px.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(openFile)

        # Начнем делать кнопки
        #self.col = QColor(0, 0, 0)

        wb = QPushButton('Черно Белое', self)
        wb.setCheckable(True)
        wb.move(10, 30)

        wb.clicked[bool].connect(self.setColor)

        sepia = QPushButton('Сепия', self)
        sepia.setCheckable(True)
        sepia.move(10, 80)

        sepia.clicked[bool].connect(self.setColor)

        gray = QPushButton('Серый', self)
        gray.setCheckable(True)
        gray.move(10, 130)

        gray.clicked[bool].connect(self.setColor)

        negativ = QPushButton('Негатив', self)
        negativ.setCheckable(True)
        negativ.move(10, 180)

        negativ.clicked[bool].connect(self.setColor)


        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Перекраска')
        self.show()


    def setColor(self, pressed):
        self.image = Image.open(self.fname)
        if pressed:
            val = 1
        else:
            val = 0

        source = self.sender()

        image = self.image
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        if source.text() == "Черно Белое":
            factor = 50
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = a + b + c
                    if val == 1:
                        if (S > (((255 + factor) // 2) * 3)):
                            a, b, c = 255, 255, 255
                        else:
                            a, b, c = 0, 0, 0

                    draw.point((i, j), (a, b, c))
        elif source.text() == "Сепия":
            depth = 30
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = (a + b + c)
                    if val == 1:
                        a = S + depth * 2
                        b = S + depth
                        c = S
                        if (a > 255):
                            a = 255
                        if (b > 255):
                            b = 255
                        if (c > 255):
                            c = 255
                    draw.point((i, j), (a, b, c))

        elif source.text() == 'Серый':
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    S = (a + b + c) // 3
                    if val == 1:
                        a, b, c = S, S, S
                    draw.point((i, j), (a, b, c))

        elif source.text() == 'Негатив':
            depth = 30
            for i in range(width):
                for j in range(height):
                    a = pix[i, j][0]
                    b = pix[i, j][1]
                    c = pix[i, j][2]
                    if val == 1:
                        draw.point((i, j), (255 - a, 255 - b, 255 - c))
                    else:
                        draw.point((i, j), (a, b, c))
        #Рисуем
        img_tmp = ImageQt(image.convert('RGBA'))
        pixmap = QPixmap.fromImage(img_tmp)
        self.lbl.setPixmap(pixmap)
        self.lbl.resize(300, 300)
        self.lbl.move(150, 30)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(300, 300)
        self.lbl.move(150, 30)
        self.lbl.setPixmap(pixmap)
        self.fname = fname
        self.image = Image.open(fname)
        print(self.fname)
        #print(pixmap)

       # lbl.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())