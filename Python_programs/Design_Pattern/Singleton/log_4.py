"""
4. Implement a Logger class using the Singleton pattern, ensuring that
only one instance is created even if multiple objects are initialized
"""
class Logger:
    instance = None
    def __new__(cls):
        if (cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance
    def message(self,data):
        print("Log: ",data)

Logger1 = Logger()
Logger2 = Logger()
Logger1.message("Log 1")
Logger2.message("Log 2")