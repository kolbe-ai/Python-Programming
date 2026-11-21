"""
Create a Logger class that acts as a Singleton. It should have a class attribute list called logs.
"""

class Logger:
        instance = None
        log = []
        def __new__(cls):
                if (cls.instance == None):
                        cls.instance = super().__new__(cls)
                return cls.instance
        def logs(self,message):
                        self.log.append(message)
                        print(message)

l1 = Logger()
l2 = Logger()
print(l1)
print(l2 == l1)

l1.logs("Ravi logged ")
l2.logs("John IP: 191:12:00:123")    