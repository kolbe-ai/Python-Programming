"""
(Context Manager: Class-based) [PDF Q66] Write a class-based context manager FileWriter using __enter__ and __exit__.
Write 2 lines, then confirm the file is closed.
"""

class Context_manager:
    def __init__(self,file_name):
        self.file_name = file_name
        self.file = None
    def __enter__(self):
        self.file = open(self.file_name,"w")
        return self.file
    def __exit__(self,a,b,c):
        self.file.close()

with Context_manager("example.txt") as f:
    f.write("Hello how are you!")
    f.write("Good to see you!")
    f.write("Bye")
    print("Inside the with block is file closed: ",f.closed)

print("Outside the with block is file closed: ",f.closed)