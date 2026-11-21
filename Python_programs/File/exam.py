"""
42.	Write a Python program to demonstrate the use of different file modes (r, w, x, and a).
For each mode, perform an appropriate file operation and display the result or any error message using exception handling.
Ensure that the file name remains the same throughout the program.
"""
try:
    with open("example1.txt","x") as file:
        pass
    with open("example1.txt","w") as file:
        file.write("Hello how are you?")
    with open("example1.txt","r") as file:
        print(file.read())
    with open("example1.txt","a") as file:
        file.write("Hello bye")
except Exception as e:
    print(e)
