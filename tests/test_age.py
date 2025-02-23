import unittest
from unittest import TestCase

from age import check_age


class TestAge(TestCase):
    def test_age_positive(self):
        age_1 = 18
        expected_1 = 'Доступ разрешён'
        result = check_age(age_1)
        self.assertEqual(expected_1, result)

    def test_age_negative(self):
        age_2 = 14
        expected_2 = 'Доступ запрещён'
        result_2 = check_age(age_2)
        self.assertEqual(expected_2, result_2)

    def test_with_params(self):
        allowed = 'Доступ разрешён'
        forbidden = 'Доступ запрещён'
        for i, (age, expected) in enumerate((
                (10, forbidden),
                (21, allowed),
                (18, allowed),
                (17, forbidden),

        )):
            with self.subTest(i):
                result = check_age(age)
                self.assertEqual(expected, result)
