#64. Implement a MyRange class that mimics the built-in range using __iter__ and __next__.


class MyRange:
    def __init__(self,start,end = None,step =1):
        if (end == None):       #checks if only 1 argument is passed
            self.end = start
            self.start =0
            self.step = step
        else:
            self.start = start
            self.end = end
            self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start >= self.end):
            raise StopIteration
        itr = self.start
        self.start+= self.step
        return itr

for i in MyRange(10):
    print(i)



