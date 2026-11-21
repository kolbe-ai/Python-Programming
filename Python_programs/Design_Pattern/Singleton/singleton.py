"""
(Design Pattern: Singleton) [PDF Q73] Create a Config class where Config() is Config() is True. Prove it.
"""

class Config:
        instance = None
        def __new__(cls):
                if (cls.instance == None):
                        cls.instance = super().__new__(cls)
                return cls.instance

c1 = Config()
c2 = Config()
print(c1)
print(c2)
print(f"Print is c1 and c2 same: {c1==c2}")