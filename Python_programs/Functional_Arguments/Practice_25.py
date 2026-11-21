#25. Create calculator(operation, *args) that supports "+" (sum of args), "*" (product of args) and "/" (average of args).

def calculator (operation, *args):
    result = 0
    match(operation):
        case '+':
            for i in args:
                result += i
        case '-':
            for i in args:
                result -= i
        case '*':
            result = 1
            for i in args:
                result *= i
        case '/':
            result = sum(args) / len(args)
    print("Result is: ",result)


count = int(input("Enter the number of numbers you fish to enter: "))
numbers = []
for i in range(count):
    n = int(input("Enter the number: "))
    numbers.append(n)

op = input("Enter the operation: ")
calculator(op,*numbers)