#(Iterator: Reverse Iterator) [PDF Q65] Create a reverse iterator over a string

class Reverse:
    def __init__(self,word):
        self.word = word
        self.count = len(self.word)-1
    def __iter__(self):
        return self
    def __next__(self):
        index = self.count
        char = self.word[index]
        self.count -= 1
        if (self.count<-1):
            raise StopIteration
        return char

for i in Reverse("Hello"):
    print(i,end="")