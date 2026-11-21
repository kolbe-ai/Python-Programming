#The Function is_valid_password(password)

import unittest

def is_valid_password(passw):
    if(len(passw) >= 8):
        return True
    return False

class TestCase(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(is_valid_password("123455678"))
    def test_is_not_valid(self):
        self.assertFalse(is_valid_password("1234"))

if __name__ == "__main__":
    unittest.main()