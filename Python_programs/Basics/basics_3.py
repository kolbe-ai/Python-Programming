"""
Without %, check whether a number is divisible by 2 using &. Then write a one-liner that swaps two numbers using XOR.
"""

num = int(input("Enter a number to check divisible by 2: "))
if (num & 1):
  print("False")
else:
  print("True")
num1 = 1
num2 = 2
temp = num1^num2
num1 = temp^num1
num2 = temp^num2
print(num1)
print(num2)