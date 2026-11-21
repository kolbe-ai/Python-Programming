#65. (Reverse Iterator) Write a class that takes a list and lets you iterate over it in reverse order.


class MyRev:
    def __init__(self,list):
        self.list = list
        self.index = len(list)-1
    def __iter__(self):
        return self
    def __next__(self):
        if (self.index<0):
            raise StopIteration
        itr = list[self.index]
        self.index -= 1
        return itr


list =[1,2,3,4,5,6,7,8,9,10]
print("Orginal list: ",*list)
print("Reverse list: ",end="")
for i in MyRev(list):
    print(i,end=" ")