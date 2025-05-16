#!/usr/bin/python3
"""
Unittests for max_integer() function.
Covers common cases, edge cases, and empty input.
Follows Python's unittest module conventions.
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer(list=[]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_end(self):
        self.assertEqual(max_integer([10, 2, 5, -1, 66]), 66)

    def test_max_integer_start(self):
        self.assertEqual(max_integer([66, 2, 5, -1, 10]), 66)

    def test_max_integer_middle(self):
        self.assertEqual(max_integer([2, 5, 66, -1, 10]), 66)

    def test_max_integer_repeated(self):
        self.assertEqual(max_integer([66, 66, 66, 66, 66]), 66)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -5, -10, -66, -2]), -1)

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([3.14, 1.21, 1.61, 1.41, 2.71]), 3.14)

    def test_max_integer_default(self):
        self.assertEqual(max_integer(), None)

    def test_max_integer_operated(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_max_integer_big(self):
        self.assertEqual(max_integer([20000, 10000, 50000, 40000]), 50000)

    def test_max_integer_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_max_integer_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_max_integer_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_max_integer_string(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_max_integer_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_max_integer_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_max_integer_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_max_integer_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
