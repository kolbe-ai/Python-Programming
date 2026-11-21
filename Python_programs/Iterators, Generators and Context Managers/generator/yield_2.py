#(Generator) [PDF Q62] Write a generator that yields odd numbers up to n.

def num_odd(n):
    for i in range(1,n,2):
        yield i

odd = num_odd(10)
for i in odd:
    print(i)