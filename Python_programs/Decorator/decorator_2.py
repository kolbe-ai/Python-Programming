"""
(Decorator: Method Decorator) [PDF Q60] Write a decorator @require_positive that raises ValueError if any argument is negative or zero. Apply it to a deposit(amount) method.
"""


def require_positive(func):
    #can use *args
    def wrapper(self, amount):
        #then amount = args[1]
        if (amount <= 0):
            raise ValueError
        else:
            #then return func(*args)
            return func(self, amount)

    return wrapper


class Bank:
    def __init__(self, balance):
        self.balance = balance
        print("Balance: ", self.balance)

    @require_positive
    def deposit(self, amount):
        self.balance += amount


b = Bank(2000000)
b.deposit(1234)

try:
    b.deposit(0)
except ValueError:
    print("Deposit amount should be atleast 0")


