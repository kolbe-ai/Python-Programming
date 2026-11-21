"""
(Iterator: __iter__ / __next__) [PDF Q64] Create a class Countdown(n) that counts from n to 1 and then raises StopIteration.
"""

class Countdown:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if (self.n <= 0):
            raise StopIteration
        current = self.n
        self.n -= 1
        return self.n

for i in Countdown(10):
    print(i)