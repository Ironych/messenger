__author__ = 'Cафин Алексей'
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))

from mess_server import process_client_message
from comm.var import *
import unittest


# в сервере только 1 функция для тестирования
class TestServer(unittest.TestCase):
    err_dict = {
        RESP: 400,
        ERR: 'Bad Request'
    }
    ok_dict = {RESP: 200}

    # ошибка если нет действия
    def test_no_action(self):
        self.assertEqual(process_client_message({TIME: 1.1, USER: {ACCOUNT_NAME: 'Гость'}}), self.err_dict)

    # Ошибка если неизвестное действие
    def test_wrong_action(self):
        self.assertEqual(process_client_message({ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: 'Гость'}}),
                         self.err_dict)

    # Ошибка, если  запрос не содержит штампа времени
    def test_no_time(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Гость'}}), self.err_dict)

    # Ошибка - нет пользователя
    def test_no_user(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1}), self.err_dict)

    # # Ошибка - не Guest
    # def test_unknown_user(self):
    #     self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Гость2'}}),
    #                      self.err_dict)

    #  корректный запрос
    def test_ok_check(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Гость'}}),
                         self.ok_dict)


if __name__ == '__main__':
    unittest.main()
