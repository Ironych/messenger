# This Python file uses the following encoding: utf-8

__author__ = 'Cафин Алексей'
import subprocess
import os
import sys
#sys.path.extend(['/mnt/1500/home/alexey/PycharmProjects/Python_lessons_advanced', '/mnt/1500/home/alexey/PycharmProjects/Python_lessons_advanced/Lesson_8'])


process = []
console = [f"gnome-terminal"]
cmd = ["python3"]
dir = os.curdir
print(dir)
path_ser = [os.path.join(dir, 'mess_server.py')]
path_clnt = [os.path.join(dir, 'mess_client.py')]


while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen(console + cmd + path_ser, shell=True))
        process.append(subprocess.Popen(console + cmd + path_clnt, shell=True))
        process.append(subprocess.Popen(console + cmd + path_clnt, shell=True))
        process.append(subprocess.Popen(console + cmd + path_clnt, shell=True))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()