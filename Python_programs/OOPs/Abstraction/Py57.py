"""
Define an interface Payment with method pay(amount).
Implement classes CreditCardPayment and UPIPayment that process payments differently.
"""

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self,card_no,amount):
        self.card_no = card_no
        self.amount = amount
    def pay(self,amount):
        print(f"\nCard no: {self.card_no}\nThe balance: {self.amount}")

class UPIPayment(Payment):
    def __init__(self,upi_id,amount):
        self.upi_id = upi_id
        self.amount = amount
    def pay(self,amount):
        print("\nUPI ID: ",self.upi_id,"\nThe balance: ",self.amount)

#initializing
amount = 10000
card = CreditCardPayment(1234567890,amount)
upi = UPIPayment("upi@bank",amount)

#withdraw and display
withdraw = 1000
upi.pay(withdraw)
card.pay(withdraw)
