"""
26. Write a method decorator that checks whether the argument passed
to a method is a positive number. Apply the decorator to a
deposit(amount) method of a BankAccount class. Display an
appropriate message for invalid values
"""

def check_positive(func):
    def wrapper(self,depos):
        if (depos<0):
            print("The deposite cannot be zero")
            return
        return func(self,depos)
    return wrapper



class Bank:
    def __init__(self,amount):
        self.amount = amount

    @check_positive
    def deposit(self,depos):
        self.amount+= depos
        print(f"Amount : {self.amount}")
        print(f"Deposit : {depos}")

b1 = Bank(1000)
b2 = Bank(2000)

b1.deposit(100)
b1.deposit(-100)
b2.deposit(200)

