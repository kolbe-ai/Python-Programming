"""
Show what happens when you open an existing file in x mode, and handle the error.
"""

try:
    with open("example.txt","w") as f:
        f.write("Hello")
    with open("example.txt","x") as f:
        pass
except FileExistsError:
    print("File already exists")