"""
16. Write a function is_prime(n) that determines whether a number is
prime. Develop appropriate unit tests using unittest for prime numbers,
non-prime numbers, zero, one and negative values
"""

import unittest
def is_prime(n):
    if (n == 1):
        return True
    if (n== 2):
        return True
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True

class Test(unittest.TestCase):
    def testPrime(self):
        self.assertTrue(is_prime(7))
    def testComposite(self):
        self.assertFalse(is_prime(8))

if __name__ == "__main__":
    unittest.main()