"""
Create Wallet with a private __balance, plus add_money(), spend() (can’t go below 0), and get_balance().
(b) (Name Mangling). What happens when you do w.__balance? How can it still be reached?
"""

class Wallet:
  __balance = 0
  def __init__(self,amount):
    self.__balance = amount
  def add_money(self,money):
    self.__balance += money
  def spend(self,spend):
    if (self.__balance - spend <=0):
      print("No bank balance")
    else:
      self.__balance -= spend
  def get_balance(self):
    print("Current balance is: ",self.__balance)

w = Wallet(1400)
w.add_money(1000)
w.spend(500)
w.get_balance()

#doesn't change
w.__balance = 20000
w.get_balance()
"""Name mangling
w._Wallet__balance = 20000
w.get_balance()
"""