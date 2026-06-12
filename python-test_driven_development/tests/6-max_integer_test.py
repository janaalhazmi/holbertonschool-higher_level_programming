#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test mixed positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_max_at_beginning(self):
        """Test max value at beginning."""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test max value at end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == "__main__":
    unittest.main()
