import ftplib
import pymysql

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap, QImage, qRgb

class Examp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        host = "f7u.ru"
        ftp_user = "pawelchf7u"
        ftp_password = "Y6h6A2p1"
        our_pict = "flowers.jpg"

        con = ftplib.FTP(host, ftp_user, ftp_password)
        file = open(our_pict, "rb")
        send = con.storbinary("STOR " + our_pict, file)
        con.close
        file.close()

        host = "f7u.ru"
        mysql_db = "python"
        mysql_user = "pawelchf7u"
        mysql_password = "A3k0Q0d1"

        try:
            conn = MySQLdb.connect(host, mysql_user, mysql_password, mysql_db)

        except MySQLdb.Error as err:
            print("Connection error: {}".format(err))
            conn.close()

        sql = "INSERT INTO image(file) VALUES('" + our_pict + "');"

        conn.autocommit(True)

        try:
            cur = conn.cursor()
            cur.execute(sql)

        except MySQLdb.Error as err:
            print("Query error: {}".format(err))

        conn.close()

        self.move(300, 200)
        self.setWindowTitle('Example')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Examp()
    sys.exit(app.exec_())
