"""
Write a method decorator that checks if arguments passed to a method are positive numbers.
Apply it to a method deposit(amount) of a BankAccount class.
"""

def check_positive(func):
    def wrapper(self,num):
        if(num<0):
            print(f"Positive numbers only accepted")
            return None
        return func(self,num)
    return wrapper

class BankAccount:
    @check_positive
    def deposit(self,amount):
        print(f"The amount deposited of {amount}")


#checking
b = BankAccount()
b.deposit(1000)
b.deposit(-100)