"""
Write a Python program that tries to open a file named file_Op.txt in
read mode. If the file does not exist, catch the exception and create an
empty file using the appropriate file mode without writing any content.
[Make use of else and finally blocks.]
"""

try:
    with open ("file_Op.txt","r") as file:
        content = file.read()
except Exception as e:
    print(e)
    with open("file_Op.txt","w") as file:
        pass

else:
    print("The file opened successfully")
    print(content)
finally:
    print("The process completed")