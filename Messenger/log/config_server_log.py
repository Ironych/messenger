__author__ = 'Cафин Алексей'

# В каждом модуле выполнить настройку соответствующего логгера по следующему алгоритму:
# Создание именованного логгера;
# Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
# Журналирование должно производиться в лог-файл;
# На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.


import sys
sys.path.append('../')
import logging
import logging.handlers
import os
from comm.var import LOGGING_LEVEL, ENCODING

# создаём формировщик логов (formatter):
frm = '%(asctime)s [%(levelname)-8s] %(filename)s ' \
      '%(message)s'
server_formatter = logging.Formatter(frm)
# Подготовка имени файла для логирования
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server.log')

# создаём потоки вывода логов
steam = logging.StreamHandler(sys.stderr)
steam.setFormatter(server_formatter)
steam.setLevel(logging.ERROR)
# ежедневная ротация
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding=ENCODING, interval=1, when='D')
log_file.setFormatter(server_formatter)

# создаём регистратор и настраиваем его
logger = logging.getLogger('server')
logger.addHandler(steam)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error event')
    logger.warning('Test warning event')
    logger.debug('Test debug event')
    logger.info('Test info event')
