from types import GeneratorType
import unittest

from src.generators.HFWC import even_numbers


class EvenNumbersTest(unittest.TestCase):

    def test_type(self):
        even_generator = even_numbers(0)
        self.assertIsInstance(even_generator, GeneratorType)

    def test_length_0(self):
        even_generator = even_numbers(0)
        self.assertEqual(len(list(even_generator)), 0)

    def test_length_n_equals_8(self):
        even_generator = even_numbers(8)
        self.assertEqual(len(list(even_generator)), 3)

    def test_values_n_equals_8(self):
        even_generator = even_numbers(8)
        self.assertEqual(next(even_generator), 2)
        self.assertEqual(next(even_generator), 4)
        self.assertEqual(next(even_generator), 8)

    def test_length_n_equals_20(self):
        even_generator = even_numbers(20)
        self.assertEqual(len(list(even_generator)), 7)

    def test_values_n_equals_20(self):
        even_generator = even_numbers(20)
        self.assertEqual(next(even_generator), 2)
        self.assertEqual(next(even_generator), 4)
        self.assertEqual(next(even_generator), 8)
        self.assertEqual(next(even_generator), 10)
        self.assertEqual(next(even_generator), 14)
        self.assertEqual(next(even_generator), 16)
        self.assertEqual(next(even_generator), 20)
