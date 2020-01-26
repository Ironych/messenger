import sys
import os
sys.path.append('../')
import logging
from comm.var import LOGGING_LEVEL, ENCODING

frm = '%(asctime)s [%(levelname)-8s] %(filename)s ' \
      '%(message)s'

# создаём формировщик логов (formatter):
client_formatter = logging.Formatter(frm)

# Подготовка имени файла для логирования
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'client.log')

# создаём потоки вывода логов
steam = logging.StreamHandler(sys.stderr)
steam.setFormatter(client_formatter)
steam.setLevel(logging.ERROR)
log_file = logging.FileHandler(path, encoding=ENCODING)
log_file.setFormatter(client_formatter)

# создаём регистратор и настраиваем его
logger = logging.getLogger('client')
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
