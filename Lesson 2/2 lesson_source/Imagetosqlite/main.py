import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import sys

from sqlalchemy import Column, ForeignKey, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb

Base = declarative_base()

class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    Data = Column(BLOB)

class Examp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        engine = create_engine('sqlite:///images.db')

        engine.echo = True

        session = sessionmaker()
        session.configure(bind=engine)
        Base.metadata.create_all(engine)

        file = open("flowers.jpg", "rb")

        our_pict = file.read()

        file.close()

        s = session()
        images = Image( Data = our_pict )
        s.add(images)
        s.commit()

        self.move(300, 200)
        self.setWindowTitle('Example of inserting image into SQLite')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Examp()
    sys.exit(app.exec_())
