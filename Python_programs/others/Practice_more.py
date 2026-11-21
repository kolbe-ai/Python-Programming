"""
Using the concept of arbitrary keyword arguments, write a function
to collect details from customer and display them as (key: value) pairs.
"""
"""
def collect():
    id = int(input("Enter the ID: "))
    n = input("Enter the Name: ")
    age = input("Enter the age: ")
    data = {"ID": id, "Name": n,"Age": age}
    return data

def display(**data):
    for i,j in data.items():
        print(i,":",j)

data = collect()
display(**data)
"""


"""
Create a function broadcast_message(*recipients, **personalized) that:
● Sends a personalized message if available in **kwargs
● Otherwise, sends a default message: "Hello from University!"
Example:
broadcast_message("Alice","Bob","Charlie", Alice="Your library books are due.", Charlie="Exam schedule updated."
"""
"""
def broadcast_message(*recipients,**personalized):
    for i in recipients:
        if i in personalized:
            message = personalized[i]
        else:
            message = "Hello from university!"
        print(f"To {i}: {message}")

broadcast_message("Alice","Bob","Charlie", Alice="Your library books are due.", Charlie="Exam schedule updated.")
"""

#27. Write a recursive function to print the nth term of a Fibonacci series.

"""
def fib(num):
    if num == 1:
        return 1
    if num == 0:
        return 1
    return fib(num-1)+fib(num-2)
print("Fibonacci series: ",fib(5))
"""

#28. Use a lambda function with map() to find the square of each number in the list. (Take input from user.)
"""
input_num = [1,2,3,4]
num = list(map(lambda x: x**2,input_num))
print(num)
"""


#43. Write a program to perform element-wise addition, subtraction, multiplication, and division of two matrices
"""
import numpy as np
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
print(arr1)
arr2= np.array([[4,3,2,1],[4,3,2,1]])
print(arr2)

print("Addition: \n",arr1+arr2)
print("Subtraction: \n",arr1-arr2)
print("Multiplication: \n",arr1*arr2)
print("Division: \n",arr1/arr2)
"""

"""
50. Create a ComplexNumber class with real and imaginary attributes.
Overload + to add two complex numbers and == to compare them, and demonstrate both with examples.
"""

class ComplexNum:
    def __init__(self,c,i):
        self.c = c
        self.i = i
    def __add__(self,other):
        return ComplexNum(self.c+other.c, self.i + other.i)
    def __eq__(self,other):
        return self.c==other.c and self.i == other.i
    def display(self):
        print(f"{self.c} + {self.i}i")
c1 = ComplexNum(1,3)
c2 = ComplexNum(1,3)
c3 = ComplexNum(1,2)

c4 = c1+c3
c4.display()
