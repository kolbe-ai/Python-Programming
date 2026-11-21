"""
57. Define an interface Payment with a method pay(amount). Implement CreditCardPayment and UPIPayment, each processing payment differently.
"""

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment (Payment):
    def pay(self,amount):
        print(f"Paying ${amount} using Credit Card!")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paying ${amount} using UPI")

card = CreditCardPayment()
card.pay(1000)

upi = UPIPayment()
upi.pay(1200)