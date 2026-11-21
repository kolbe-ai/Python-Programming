"""
17. Write a function calculate_average(numbers) that returns the
average of a list of numbers. Create unit tests to verify normal lists, a
single-element list and an empty list.
"""

import unittest
def calculate_average(numbers):
    if(numbers):
        sum1 = sum(numbers)
        length = len(numbers)
        return sum1/length
    return False

class Test_unit(unittest.TestCase):
    def test_list(self):
        self.assertEqual(calculate_average([1,2,3,4,5]),3)
    def test_single(self):
        self.assertEqual(calculate_average([1]), 1)
    def test_empty(self):
        self.assertFalse(calculate_average([]))

if __name__ == "__main__":
    unittest.main()