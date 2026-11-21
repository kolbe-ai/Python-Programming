#is_palindrome(word)

import unittest
def is_palindrome(word):
    return word == word[::-1]

class TestCase(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
    def test_not_palindrom(self):
        self.assertFalse(is_palindrome("Hello"))

if __name__ == "__main__":
    unittest.main()