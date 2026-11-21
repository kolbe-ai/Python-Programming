"""
49. Demonstrate duck typing using a UPI payment system.
"""

class SBI:
    def pay(self):
        print("SBI paying!")

class ICICI:
    def pay(self):
        print("ICICI paying!")

class Bob:
    def pay(self):
        print("BOB paying!")

def UPI(obj):
    obj.pay()

sbi = SBI()
icici = ICICI()
bob = Bob()

UPI(sbi)
UPI(icici)
UPI(bob)