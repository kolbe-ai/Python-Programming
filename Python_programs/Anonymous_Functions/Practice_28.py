"""
28. Use a lambda with map() to square each number in a list taken from the user. (Sample input [2, 3, 4] gives output [4, 9, 16].)
"""

nums = list(map(int,input("Enter the numbers: ").split()))
print(nums)
sqr = lambda x : x**2
sqr_nums = list(map(sqr,nums))
print(sqr_nums)