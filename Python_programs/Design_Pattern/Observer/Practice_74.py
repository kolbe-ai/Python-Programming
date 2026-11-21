"""
74. (Observer) Create a StockMarket class where investors (observers) are notified whenever a stock price changes.
"""

class Investor:
    def __init__(self,name):
        self.name = name
    def update(self,stock):
        print(f"Notification: To {self.name} Price of {stock.stock} changed to {stock.price}")

class StockMarket:
    def __init__(self,stock,price):
        self.stock = stock
        self.price = price
        self.investors  = []
    def register_user(self,user):
        self.investors.append(user)
    def update(self,new_price):
        self.price = new_price
        for i in self.investors:
            i.update(self)

user1 = Investor("Ravi")
tata = StockMarket("Tata",1000)
tata.register_user(user1)
tata.update(1100)