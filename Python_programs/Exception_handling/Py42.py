"""
Write a Python program to demonstrate the use of different file
modes (r, w, x, and a). For each mode, perform an appropriate file
operation and display the result or any error message using exception
handling. Ensure that the file name remains the same throughout the
program.
"""

try:
    with open ("example.txt","w") as file:
        file.write("Hello how are you\nGood to see you!")
    with open("example.txt","a") as file:
        file.write("\n\nHi, its me again\nGood to see you again!\n")
    with open("example.txt","r") as file:
        print(file.read())
    with open("example.txt","x") as file:
        pass
except Exception as e:
    print(e)