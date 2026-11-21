"""
41. Try to open file_Op.txt in read mode. If it does not exist, catch the exception and create an empty file using the proper mode,
without writing anything. Use else and finally blocks.
"""

try:
    with open("file_Op.txt","r") as f:
        pass
except FileNotFoundError as e:
    print("File Not Found!\nCreating the file....")
    with open("file_Op.txt","w") as f:
        pass
    print("File Created!")
else:
    print("File Found!")
finally:
    print("Process Completed!")