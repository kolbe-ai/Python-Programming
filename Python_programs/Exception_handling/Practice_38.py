"""
38. Take a string input and convert it to an integer, handling the case where the conversion fails.
"""

try:
    sent = input("Enter the number: ")
    num = int(sent)
    print("Number is: ",num)
except ValueError as e:
    print("Error: ",e)
