#Write a generator that reads a file line by line (like open().readlines() but lazily).

def generator(n):
    with open(n,"r") as f:
        for i in f:
            yield i

with open("example.txt","w") as f:
    f.write("1. Hello how are you? \n2. Good to see you! \n3. Happy with you!\n")

#using next
line = generator("example.txt")
print(next(line))
print(next(line))
print(next(line))

#using loop
for i in generator("example.txt"):
    print(i)