"""
Write a Python program to create a class BankAccount with a private attribute __balance.
Provide methods to deposit, withdraw, and check balance.
Ensure that the balance cannot be directly modified outside the class.
"""

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def display(self):
        print(f"\nOwner: {self.name}\nBalance: {self.__balance}\n")
    def deposit(self,money):
        self.__balance += money
        print(f"After deposit balance: {self.__balance}")
    def withdraw(self,money):
        self.__balance -= money
        print(f"After withdraw balance: {self.__balance}")
    def check_balance(self):
        print(f"Balance: {self.__balance}")


b1 = BankAccount("Rohit",10000)
#accessing normally
b1.display()
b1.deposit(1004)
b1.withdraw(1001)
b1.check_balance()

#tryign to chnage the balance, name changes but not balance
b1.name = "John"
b1.__balance = 20000
b1.display()