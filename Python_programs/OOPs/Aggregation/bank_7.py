"""
7. Create a Bank class and a Customer class. A customer has an account
in the bank (aggregation). Show that a customer can exist without the
bank being deleted.
"""

class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
    def display(self):
        print(f"Bank: {self.bank_name}")

class Customer:
    def __init__(self,cust,b_name):
        self.cust = cust
        self.b_name = b_name
    def display(self):
        print(f"\nCustomer: {self.cust}\nBank: {self.b_name.bank_name}")

#creating objects
b = Bank("SBI")
c = Customer("Ravi",b)

#printing results
b.display()
c.display()

#deleting bank
del b
c.display()     #still exists