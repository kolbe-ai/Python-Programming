73. (Singleton) Implement a Logger class so that only one instance exists, even if several objects are created.
"""

class Logger:
    _instance = None
    def __new__(cls):
        if (cls._instance is None):
            super().__new__(cls)
        return cls._instance


l1= Logger()
l2= Logger()
print(l1==l2)
print("Memory address of l1 is: ",id(l1))
print("Memory address of l2 is: ",id(l2))

