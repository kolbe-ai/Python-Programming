"""
(Unit Testing: unittest) [PDF Q69] Write is_even(n) and a unittest class with 3 tests (even, odd, zero). Show how to run it.
"""

import unittest

class TestCase(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(10))
    def test_odd(self):
        self.assertFalse(is_even(11))
    def test_zero(self):
        self.assertTrue(is_even(0))

def is_even(n):
    return n%2 == 0

if __name__ == "__main__":
    unittest.main()