"""
Write a function add() that can add:
- two numbers,
- three numbers, or
- Concatenate two strings.
Use default arguments to simulate method overloading.
"""

def add(a,b,c = None):
    if ( c == None):
        return a+b
    return a+b+c

print(f"Two numbers: {add(1,2)}")
print(f"Three numbers: {add(1,2,3)}")
print(f"Adding string: {add("Hello"," Guys")}")
