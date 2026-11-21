#28. Use a lambda with map() to square each number in a list taken from the user. (Sample input [2, 3, 4] gives output [4, 9, 16].)

numbers = []
count = int(input("Enter the number of iteration: "))
for i in range(count):
    n = int(input("Enter a number: "))
    numbers.append(n)

x = lambda x: x**2
result = list(map(x,numbers))
result_packed = map(x,numbers)
print("The result is: ",*result_packed)
print("The result is: ",result)