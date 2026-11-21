"""
Write a program to create a class BankAccount with a class variable bank_name and instance variables name and balance.
Display the bank name along with customer details.
"""

class BankAccount:
    b_name = "Python Bank"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def display(self):
        print("\n\n|--- %s ---|\nName: %s\nBalance: %d"%(BankAccount.b_name,self.name,self.balance))

name = input("Enter the name: ")
balance = int(input("Enter the balance: "))
b1 = BankAccount(name,balance)
b1.display()