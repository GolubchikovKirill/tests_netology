import unittest
from unittest import TestCase
from weight import get_cost

class TestWeight(TestCase):
    def test_params(self):
        expected_higher = 'Стоимость доставки: 500 руб.'
        expected_lower = 'Стоимость доставки: 200 руб.'
        for i, (weight, expected) in enumerate((
                (10, expected_higher),
                (5, expected_lower),
                (15, expected_higher),
                (20, expected_higher),
                (9, expected_lower)
        )):
            with self.subTest(i):
                result = get_cost(weight)
                self.assertEqual(result, expected)
