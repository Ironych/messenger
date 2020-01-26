# This Python file uses the following encoding: utf-8

__author__ = 'Cафин Алексей'
import logging
# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# Порт поумолчанию для сетевого ваимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONN = 5
# Максимальная длина сообщения в байтах
MAX_PACKAGE_LEN = 4048
# Кодировка
ENCODING = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESP = 'response'
ERR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
AUTH = 'authenticate'
MSG = 'msg'
QUIT = 'quit'
PROBE = 'prоbe'
JOIN = 'join'
LEAVE = 'leave'
EXIT = 'exit'

# Словари - ответы:
# 200
RESPONSE_200 = {RESP: 200}
# 400
RESPONSE_400 = {
            RESP: 400,
            ERR: None
        }


if __name__ == '__main__':
    pass