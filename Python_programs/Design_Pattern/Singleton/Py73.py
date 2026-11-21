"""
Implement a Logger class using the Singleton pattern,
ensuring that only one instance is created even if multiple objects are initialized.
"""

class Logger:
    instance = None
    def __new__(cls):
        if (cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance

Log1 = Logger()
Log2 = Logger()
print("Log 1 address: ",Log1)
print("Log 2 address: ",Log2)