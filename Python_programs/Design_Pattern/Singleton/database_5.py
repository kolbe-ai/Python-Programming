"""
5. Create a DatabaseConnection class using the Singleton pattern. Ensure
that all objects share the same database connection instance.
Demonstrate that multiple object creations refer to the same instance.
"""

class Connection:
    instance = None
    def __new__(cls):
        if (cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance
    def show(self,message):
        print(Connection.instance," : ",message)

Con1 = Connection()
Con2 = Connection()
Con1.show("Con1")
Con2.show("Con2")