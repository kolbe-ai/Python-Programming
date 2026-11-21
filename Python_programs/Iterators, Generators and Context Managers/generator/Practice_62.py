#62. Create a generator that yields only the even numbers up to n.


def generator(num):
    for i in range(num):
        if (i%2==0):
            yield i

num = int(input("Enter the number: "))
gen = generator(num)
for i in gen:
    print(i)


