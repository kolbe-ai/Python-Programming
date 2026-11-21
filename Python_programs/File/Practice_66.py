#66. Write a class-based context manager that opens a file, writes some text, and closes the file automatically when the block ends.

class MyFile:
    def __init__(self,file_name,file_mode):
        self.file_name = file_name
        self.file_mode =file_mode
        self.f = None
    def __enter__(self):
        self.f = open(self.file_name,self.file_mode)
        return self.f
    def __exit__(self,*args):
        self.f.close()

with MyFile("example.txt","r") as f:
    line = f.readline()
    print(line)

