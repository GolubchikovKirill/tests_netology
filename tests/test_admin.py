import unittest
from unittest import TestCase
from admin import check_auth

class TestAdmin(TestCase):
    def test_coincidence(self):
        login = 'admin'
        password = 'password'
        expected = 'Добро пожаловать'
        result = check_auth(login, password)
        self.assertEqual(result, expected)

    def test_not_coincidence(self):
        login = 'adminn'
        password = 'Password'
        expected = 'Доступ ограничен'
        result = check_auth(login, password)
        self.assertEqual(result, expected)

