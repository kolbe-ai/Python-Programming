"""
Write a program that takes a string input and converts it to an
integer.Please address the situation where conversion is unsuccessful..
"""

try:
    num = input("Enter a number: ")
    int_num = int(num)
    print("Number is: ",int_num)
except ValueError:
    print(f"The entered number {num} is not an integer")