class File:
    def __init__(self,name,mode):
        self.mode = mode
        self.name = name
    def __enter__(self):
        self.f= open(self.name,self.mode)
        return self.f
    def __exit__(self,*args):
        self.f.close()

with File("example.txt","r") as f:
    print(f.read())