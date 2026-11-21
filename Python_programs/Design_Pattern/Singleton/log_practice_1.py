"""
Question 3 — Easy
Create a Logger class using the Singleton pattern.
Create three Logger objects and demonstrate that all three objects refer to the same instance.
"""

class Logger:
    instance = None
    def __new__(cls):
        if (cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance
    def display(self,message):
        print(f"Log: {message}")

l1 = Logger()
l2 = Logger()
l1.display("Hello1")
l2.display("Hello2")