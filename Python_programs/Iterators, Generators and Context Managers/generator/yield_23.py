"""
23. Create a generator that yields the squares of numbers from 1 to n.
Use the generator to display the generated values
"""

def sqr(n):
    for i in range(n):
        yield i*i

for i in sqr(10):
    print(i)