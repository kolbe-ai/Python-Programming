"""
Reverse Iterator : Write a class that takes a list and allows iteration over it in reverse order.
"""

class Range:
    def __init__(self,start ,step = 1):
        #initialize them
        self.start = start
        #end = length of list - 1 so we can access last value
        self.end = len(start) -1
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        #checking if iteration came to first position
        if (self.end < 0):
            raise StopIteration
        #current value = list[current_last value]
        current_value = self.start[self.end]
        #current_last = current_last - step
        self.end -= self.step
        return current_value

items = ["shoes","football","food"]
for i in Range(items):
    print(i)