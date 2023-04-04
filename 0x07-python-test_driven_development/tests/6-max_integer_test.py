#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """orderd list int test"""
        ordered = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """unorderd list test"""
        unordered = [1, 2, 4, 3]
        self.assertAlmostEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """test with initial max value"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertAlmostEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Empty list test"""
        empty = []
        self.assertAlmostEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """single element test"""
        one_element = [7]
        self.assertAlmostEqual(max_integer(one_element), 7)

    def test_floats(self):
        """floats test"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertAlmostEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """test with int anf float combination"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertAlmostEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """String test"""
        string = "Melaku"
        self.assertAlmostEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """test with multi string"""
        strings = ["Melaku", "Demeke", "is", "amazing"]
        self.assertAlmostEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """empty string test"""
        self.assertAlmostEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
