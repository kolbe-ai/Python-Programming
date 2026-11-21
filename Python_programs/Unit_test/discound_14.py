"""
14. Write a function calculate_discount(amount) that calculates a
discount based on the purchase amount. Use Python's unittest
framework to test different input values and expected outputs.
"""

import unittest
def calculate_discount(amount):
    return amount-(amount*.10)

class Unit(unittest.TestCase):
    def test_high(self):
        self.assertEqual(calculate_discount(1000),900)
    def test_med(self):
        self.assertEqual(calculate_discount(500),450)
    def test_low(self):
        self.assertEqual(calculate_discount(100),90)

