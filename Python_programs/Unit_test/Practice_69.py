"""
69. Write a function is_palindrome(s) that returns True for palindromes and False otherwise.
Write unittest tests checking that 'madam' returns True and 'hello' returns False.
"""

import unittest

def is_palindrome(s):
    palin = s[::-1]
    return palin == s

class Test(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()














