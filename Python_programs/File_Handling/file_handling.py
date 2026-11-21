"""
Write a program that tries to open notes.txt in r mode. If it doesn’t exist, create it (without writing anything). Use else and finally.
"""

try:
    with open("notes.txt","r") as file:
        pass
except FileNotFoundError:
    print("File not found... Creating it")
    with open("notes.txt","w") as file:
        pass
else:
    print("File found!")
finally:
    print("Process completed!")