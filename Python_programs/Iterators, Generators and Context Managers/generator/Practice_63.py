"""
63. Write a generator that reads a file line by line lazily, as an alternative to open().readlines().
"""

def generator():
    with open("example.txt","r") as f:
          for i in f:
              yield i


lazy_line = generator()
for i in lazy_line:
    print(i,end="")
