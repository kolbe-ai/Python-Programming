"""
53. Create a BankAccount class with a private __balance and methods to deposit, withdraw and check the balance.
The balance must not be modifiable directly from outside the class.
"""

class BankAccount:
    #__balance = 98765
    def __init__(self,money = 98765):
        self.__balance = money
    def deposit(self,money):
        self.__balance += money
        print("New balance: ",self.__balance)
    def withdraw(self,money):
        if ( self.__balance - money <0):
            print("Insufficient balance!")
            return
        else:
            self.__balance -= money
            print("New balance: ",self.__balance)
    def check_balance(self):
        print("Balance: ",self.__balance)

b = BankAccount()
b.deposit(100)
b.withdraw(10)
