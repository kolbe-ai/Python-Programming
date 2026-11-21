#Implement a class MyRange that mimics Python’s built-in range function using __iter__ and __next__.

class MyRange:
    def __init__(self,start,end = None, step = 1):
        if (end == None):
            self.end = start
            self.start = 0
        else:
            self.end = end
            self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.start >= self.end):
            raise StopIteration
        current_value = self.start
        self.start += self.step
        return current_value


for i in  MyRange(0,10,2):
    print(i)

