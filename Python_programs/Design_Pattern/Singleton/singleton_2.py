"""
Problem Statement:
A company can only have one CEO.
1. Create a CEO Singleton class using __new__.
2. Create two variables, ceo1 = CEO() and ceo2 = CEO().
3. Set ceo1.name = "Sundar Pichai".
4. Print ceo2.name and prove that ceo1 is ceo2 is True.
"""

class CEO:
    instance = None
    name = ""
    def __new__(cls):
        if(cls.instance == None):
            cls.instance = super().__new__(cls)
        return cls.instance

c1 = CEO()
c2 = CEO()
c1.name = "Sundar Pichai"
print(c1.name)
print(c2.name)