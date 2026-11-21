6. Implement a Configuration class using the Singleton design pattern.
Store application settings such as application name and version.
Demonstrate that modifying the settings through one object is reflected
when accessed through another object.
"""

class Configuration:
    instance = None
    def __new__(cls):
        if(cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance
    def show(self,name,version):
        print(f"Name: {name} \tVersion: {version}")


Config1 = Configuration ()
Config2 = Configuration()

Config1.show("User1","V1.23.2")
Config2.show("User2","V1.26.4")

Config2.name = "User 2"
Config2.version = "V1.26.4"
print(Config1.name)         #prints config2
print(Config1.version)      #prints config2

#Config1.show("User1","V1.23.2")