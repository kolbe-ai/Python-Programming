"""
Write a Python program to demonstrate the concept of Duck Typing using a UPI payment system.
"""

class GooglePay:
    def payment(self,pay):
        print("\nPayment in process....\nPaid rs of %.2f using GooglePay"%(pay))
class Paytm:
    def payment(self,pay):
        print("\nPayment in process....\nPaid rs of %.2f using Paytm"%(pay))
class SuperMoney:
    def payment(self,pay):
        print("\nPayment in process....\nPaid rs of %.2f using SuperMoney"%(pay))

class All:
    def __init__(self, amount, payment_method):
        self.amount = amount
        self.payment_method = payment_method()
    def payment(self):
        self.payment_method.payment(self.amount)

gpay = All(1000,GooglePay)
paytm = All(1100,Paytm)
supermoney = All(1200,SuperMoney)

gpay.payment()
paytm.payment()
supermoney.payment()


