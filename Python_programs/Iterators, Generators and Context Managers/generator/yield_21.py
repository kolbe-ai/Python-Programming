#22. Create a generator that yields only even numbers up to n.

def number(n):
    for i in range(2,n,2):
        yield i

for i in number(20):
    print(i)
