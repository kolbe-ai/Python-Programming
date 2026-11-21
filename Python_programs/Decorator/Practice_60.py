"""
60. Write a method decorator that checks that the arguments passed are positive numbers, and apply it to deposit(amount) in a BankAccount class.
"""


def decorator(func):
    def wrapper(*args,**kwargs):
        for i in args:
            if (i <0):
                print("Negative amount cannot be deposited")
                return 0
        result = func(*args,**kwargs)
        return result
    return wrapper

@decorator
def deposit(amount):
    print("Deposit amount: ",amount)

deposit(-1000)
deposit(1000)