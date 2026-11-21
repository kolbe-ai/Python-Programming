"""
13. Write a Python function is_palindrome(s) that returns True if the
string s is a palindrome and False otherwise. Write unit tests using
unittest to check that 'madam' returns True and 'hello' returns False
"""

import unittest

def is_palindrom(s):
    return s == s[::-1]

class Unit(unittest.TestCase):
    def test_madam(self):
        self.assertTrue(is_palindrom("madam"))
    def test_hello(self):
        self.assertFalse(is_palindrom("hello"))
