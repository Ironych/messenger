# This Python file uses the following encoding: utf-8

__author__ = 'Cафин Алексей'
import sys
import os
import argparse
sys.path.append(os.path.join(os.getcwd(), '..'))
import json
from comm.var import *
from log.decorators import *
from errors import IncorrectDataRecivedError, NonDictInputError


# Утилита приёма и декодирования сообщения
# принимает байты выдаёт словарь, если принято что-то другое отдаёт ошибку значения
@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LEN)  #получаем закодированное сообщение
    if isinstance(encoded_response, bytes):  #проверяем что пришли байты
        json_response = encoded_response.decode(ENCODING)  #декодируем
        response = json.loads(json_response)  # превращаем JSON в словарь
        if isinstance(response, dict):  #проверяем что получилмся словарь
            return response  #Возвращаем ответ в виде словаря
        else:
            raise IncorrectDataRecivedError  # если не словарь, то ошибка
    else:
        raise IncorrectDataRecivedError  # если не байты то ощибка


# Утилита кодирования и отправки сообщения
# принимает словарь и отправляет его
@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)  # превращаем сообщение в json
    encoded_message = js_message.encode(ENCODING)  # кодируем
    sock.send(encoded_message)  #Посылаем кодированное сообщение


# Парсер аргументов коммандной строки.
@log
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('-m', default='send', nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    return parser
