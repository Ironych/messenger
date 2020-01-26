#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QPushButton,  QSlider, QHBoxLayout,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QPixmap, QIcon, QColor, qRgb, QImage
import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.
from PIL.ImageQt import ImageQt

from PyQt5.QtCore import Qt

from sqlalchemy import Column, ForeignKey, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Imagedb(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    Data = Column(BLOB)


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

        btn1 = QPushButton("Обрезать", self)
        btn1.move(30, 50)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton("Масштаб", self)
        btn2.move(30, 100)
        btn2.clicked.connect(self.buttonClicked)

        btn3 = QPushButton("В базу", self)
        btn3.move(30, 150)
        btn3.clicked.connect(self.saveImage)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(50, 400, 300, 30)
        sld.valueChanged[int].connect(self.changeValue)


        self.statusBar()

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Аватар')
        self.show()

    def changeValue(self, value):
        our_pict = self.image
        width = value*5
        height = value*5
        #width = our_pict.size[0]*value/50
        #height = our_pict.size[1]*value/50
        our_pict = our_pict.resize((width, height), Image.NEAREST)  # change size
        our_pict = ImageQt(our_pict.convert('RGBA'))
        hbox = QHBoxLayout(self)
        our_pict = QPixmap.fromImage(our_pict)
        self.lbl.setPixmap(our_pict)
        hbox.addWidget(self.lbl)
        self.setLayout(hbox)
        self.move(300, 300)
        self.setWindowTitle('Example of slider')
        #self.statusBar().showMessage(sender.text() + ' was pressed')

    def buttonClicked(self):
        sender = self.sender()
        our_pict = self.image
        if sender.text() == 'Обрезать':
            our_pict = our_pict.crop((0, 0, 150, 150)) # left, top, right, bottom
            our_pict = ImageQt(our_pict.convert('RGBA'))
            hbox = QHBoxLayout(self)
            our_pict = QPixmap.fromImage(our_pict)
            self.lbl.setPixmap(our_pict)
            hbox.addWidget(self.lbl)
            self.setLayout(hbox)
            self.move(300, 300)
            self.setWindowTitle('Example of crop')
            self.statusBar().showMessage(sender.text() + ' was pressed')
        else:
            width = 400
            height = 300
            our_pict = our_pict.resize((width, height), Image.NEAREST)  # change size
            our_pict = ImageQt(our_pict.convert('RGBA'))
            hbox = QHBoxLayout(self)
            our_pict = QPixmap.fromImage(our_pict)
            self.lbl.setPixmap(our_pict)
            hbox.addWidget(self.lbl)
            self.setLayout(hbox)
            self.move(300, 300)
            self.setWindowTitle('Example of resize')
            self.statusBar().showMessage(sender.text() + ' was pressed')
        self.show()


    def saveImage(self):
        engine = create_engine('sqlite:///images.db')

        engine.echo = True

        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)

        file = open(self.fname, "rb")
        our_pict = file.read()
        file.close()

        s = session()
        images = Imagedb( Data = our_pict )
        s.add(images)
        s.commit()


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        pixmap = QPixmap(fname)
        self.lbl.resize(300, 300)
        self.lbl.move(150, 30)
        self.lbl.setPixmap(pixmap)
        self.image = Image.open(fname)
        print(self.fname)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())