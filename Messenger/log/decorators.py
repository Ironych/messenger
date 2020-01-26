__author__ = 'Cафин Алексей'

import sys
sys.path.append('../')
import logging
import logging.handlers
import log.config_server_log
import log.config_client_log

from functools import wraps
import traceback


# 1. Продолжая задачу логирования, реализовать декоратор @log, фиксирующий обращение к декорируемой функции. Он сохраняет ее имя и аргументы.
# 2. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная. Если имеется такой код:
# @log
# def func_z():
#  pass
#
# def main():
#  func_z()
# ...в логе должна быть отражена информация:
# "<дата-время> Функция func_z() вызвана из функции main"

mod = sys.argv[0]
if mod.find('mess_client.py') == -1:
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')


def log(func_2_log):

    def decor(*args, **kwargs):
        logger.debug(f'Была вызвана функция {func_2_log.__name__} c параметрами: \n {args}, {kwargs} \n'
                     f'Вызов из модуля {func_2_log.__module__} \n'
                     f'Вызов из файл {mod} ')

        res = func_2_log(*args, **kwargs)
        return res

    return decor
