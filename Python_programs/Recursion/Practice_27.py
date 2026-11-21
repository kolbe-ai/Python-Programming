#27. Write a recursive function to print the nth term of the Fibonacci series.

def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib(n-1) + fib(n-2)

num = int(input("Enter the number to print the nth term of the Fibonacci series: "))
result = fib(num)
print(f"The nth term of the Fibonacci series: {result}")