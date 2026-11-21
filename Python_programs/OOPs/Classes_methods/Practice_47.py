"""
47. Create a BankAccount class with a class variable bank_name and instance variables name and balance.
 Display the bank name along with the customer details.
"""

class BankAccount:
    bank_name = "SBI"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def display(self):
        print(f"\n{self.bank_name}\nName: {self.name}\nBalance: {self.balance}")

b = BankAccount("Ravi",12493)
b.display()
