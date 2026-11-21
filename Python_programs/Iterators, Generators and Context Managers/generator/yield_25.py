#25. Create a generator that yields numbers divisible by 3 up to n.

def div(n):
    for i in range(3,n+1,3):
        yield i

for i in div(100):
    print(i)