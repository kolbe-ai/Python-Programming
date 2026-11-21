"""
Create a Bank class and a Customer class.
A customer has an account in the bank (aggregation).
Show that a customer can exist without the bank being deleted.
"""

class Bank:
  def __init__(self,bank):
    self.bank = bank

class Customer:
  def __init__(self,name,number,age,bank):
    self.name = name
    self.number = number
    self.age = age
    self.bank = bank
  def display(self):
    print(f"Name: {self.name}\nNumber: {self.number}\nAge: {self.age}\nBank: {self.bank.bank}\n\n")

b = Bank("SBI")
c = Customer("Ravi",987654321,45,b)
c.display()

#after deleting
del(b)

c.display()