"""
Use a lambda function with map() to find the square of each number
in the list. (Take input from user.)
"""

numbers = input("Enter the number you wish to get squares off (provide space in each numbers: ")

list_num = list(map(int,numbers.split()))
sqr_num = list(map(lambda x: x*x , list_num))
print("Numbers: ",list_num)
print("Squared numbers: ",sqr_num)