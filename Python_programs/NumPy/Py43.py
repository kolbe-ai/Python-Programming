"""
Write a program to perform element-wise addition, subtraction,
multiplication, and division of two matrices
"""

import numpy as np


def matrix(n):
    full_matrix= []
    print("Enter the elements for Matrix ",n)
    for r in range(row):
        row_num = []
        for c in range(col):
            num = int(input(f"Enter the element [{r}][{c}]: "))
            row_num.append(num)
        full_matrix.append(row_num)
    return np.array(full_matrix)
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
m1 = matrix("M1")
m2 = matrix("M2")

print(f"\nMatrix 1: \n{m1}\n")
print(f"\nMatrix 2: \n{m2}")

print(f"\nAdded matrix: \n{m1+m2}")
print(f"Subtracted matrix: \n{m1-m2}")
print(f"Multiplied matrix: \n{m1*m2}")
print(f"Divided matrix: \n{m1/m2}")