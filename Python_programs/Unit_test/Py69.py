"""
Write a Python function is_palindrome(s) that returns True if the string s is a palindrome and False otherwise.
Write unit tests using unittest to check that 'madam' returns True and 'hello' returns False
"""


import unittest

def is_palindrome(s):
    return s == s[::-1]

class TestClass(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(is_palindrome("radar"))
    def test_is_false(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()