70. (Aggregation) Create Bank and Customer classes where a customer has an account in the bank.
Show that the customer can still exist even if the bank is deleted.
"""

class Bank:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Bank: ",self.name)

class Customer:
    def __init__(self,name,bank):
        self.customer = name
        self.bank = bank
    def display(self):
        print(f"Customer: {self.customer}\nBank: {self.bank.name}")

b= Bank("SBI")
b.display()

print("\nBefore deleting:")
c = Customer("Ravi",b)
c.display()

del b
print("\n\nAfter deleting: ")
c.display()
