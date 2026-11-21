#Create a generator that yields only even numbers up to n.
def numbers(n):
    for i in range (0,n+1,2):
        yield i


n = int(input("Enter a number: "))
print("Even numbers: ")
for i in numbers(n):
    print(i)