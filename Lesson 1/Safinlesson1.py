#!/usr/bin/python3
# -*- coding: utf-8 -*-


#Написать программу, которая будет загружать изображения с компьютера и добавлять к ним эффекты.

import sys
from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QLabel, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon

from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt



class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel(self)

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Файл')
        fileMenu.addAction(openFile)

        # а тут мы добавим перекраску
        # self.t_editor = QTextEdit()
        # self.setCentralWidget(self.t_editor)

        our_bw = QAction(QIcon('b.jpg'), 'BW', self)
        our_bw.triggered.connect(self.actionBW)

        our_gray = QAction(QIcon('i.jpg'), 'Серый', self)
        our_gray.triggered.connect(self.actionGray)

        our_sepia = QAction(QIcon('u.jpg'), 'Сепия', self)
        our_sepia.triggered.connect(self.actionSepia)

        tool_b = self.addToolBar('Перекраска')
        tool_b.addAction(our_bw)
        tool_b.addAction(our_gray)
        tool_b.addAction(our_sepia)

        self.setGeometry(300, 200, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


    def actionBW(self):
        image = Image.open(fname)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        factor = 50
        for i in range(width):
            for j in range(height):
                 a = pix[i, j][0]
                 b = pix[i, j][1]
                 c = pix[i, j][2]
                 S = a + b + c
                 if (S > (((255 + factor) // 2) * 3)):
                     a, b, c = 255, 255, 255
                 else:
                     a, b, c = 0, 0, 0
                 draw.point((i, j), (a, b, c))

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Black and White')
        self.show()

    def actionGray(self):
        image = Image.open(fname)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        for i in range(width):
            for j in range(height):
                 a = pix[i, j][0]
                 b = pix[i, j][1]
                 c = pix[i, j][2]
                 S = (a + b + c) // 3
                 draw.point((i, j), (S, S, S))

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Gray')
        self.show()

    def actionSepia(fname):
        image = Image.open(fname)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()

        depth = 30
        for i in range(width):
            for j in range(height):
                 a = pix[i, j][0]
                 b = pix[i, j][1]
                 c = pix[i, j][2]
                 S = (a + b + c)
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

        img_tmp = ImageQt(image.convert('RGBA'))

        hbox = QHBoxLayout(self)
        pixmap = QPixmap.fromImage(img_tmp)

        lbl = QLabel()
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        #self.move(300, 200)
        self.setWindowTitle('Sepia')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(300,300)
        self.lbl.setPixmap(pixmap)
        print(fname)
        #print(pixmap)

       # lbl.setPixmap(pixmap)


if __name__ == '__main__':
    fname = "image.jpg"
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
