"""
Create an array 1 to 12, reshape it to 3×4, then print the shape, the sum of each row, and the max of each column.
"""

import numpy as np

arr = np.arange(1,13).reshape(3,4)
print(arr)

print("\n\nShape: ",arr.shape)

sum1 = arr.sum(axis = 1)
print("Sum of each row is: ",sum1)
sum1 = arr.sum(axis = 0)
print("Sum of each column is: ",sum1)
