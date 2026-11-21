"""
15. Create a BankAccount class with deposit() and withdraw() methods.
Write unit tests to verify successful deposits, withdrawals, insufficient
balance and invalid amounts.
"""

import unittest

class BankAccount:
    def __init__(self,money):
        self.money = money
    def deposit(self):
        if(self.money < 0):
            return False
        deposit = 100
        self.money = self.money+100
        return self.money
    def withdraw(self):
        if (self.money < 0):
            return False
        withdraw = 50
        self.money = self.money-50
        return self.money

class Unit(unittest.TestCase):
    def test_deposit(self):
        b = BankAccount(1000)
        self.assertEqual(b.deposit(),1100)
    def test_withdraw(self):
        b = BankAccount(1000)
        self.assertEqual(b.withdraw(),950)

    def insufficient_balance(self):
        b = BankAccount(0)
        self.assertTrue(b.deposit(0))
#unittest.main()