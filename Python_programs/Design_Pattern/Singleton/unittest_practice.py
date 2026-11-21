import unittest
"""
def square(n):
    return n*n

class Test (unittest.TestCase):
    def test_postive(self):
        self.assertEqual(square(10),100)
    def test_failed(self):
        self.assertNotEqual(square(10),10)

if __name__ == "__main__":
    unittest.main()

"""



def odd(n):
    return n%2 == 1

class Test(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(odd(7))
    def test_failed(self):
        self.assertFalse(odd(8))

if __name__ == "__main__":
    unittest.main()