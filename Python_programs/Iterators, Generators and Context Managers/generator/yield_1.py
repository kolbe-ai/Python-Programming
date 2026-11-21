#(Generator) [PDF Q62] Write a generator squares(n) that yields squares up to n. Print using a for loop and with next().
def squares(n):
  for i in range(n):
    yield i*i


num = squares(4)
print(next(num))
print(next(num))
print(next(num))
print(next(num))