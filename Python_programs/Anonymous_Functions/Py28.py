"""
Use a lambda function with map() to find the square of each number
in the list. (Take input from user.)
"""

list1 = [2,3,4,5,6]

x = lambda n : (
        n*n)

result = list(map(x,list1))
print(result)