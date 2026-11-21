#24. Create a generator that yields only odd numbers up to n

def odd(n):
    for i in range(1,n,2):
        yield i

for i in odd(10):
    print(i)