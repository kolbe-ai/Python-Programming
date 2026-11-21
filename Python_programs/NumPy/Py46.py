"""
Create a 5 × 5 NumPy array with numbers from 1 to 25. Then do the
following using slicing:
a. Print the center 3 × 3 part of the array.
b. Print the reverse of the center 3 × 3 part.
c. Print the first 2 rows and last 2 columns.
d. Print all elements of the array in a single line
"""

import numpy as np
arr = np.arange(1,26).reshape(5,5)
print("The array is: \n",arr)

arr_3x3 = arr[1:4,1:4]
print("The center 3x3 is:\n",arr_3x3)

rev_arr_3x3 = arr_3x3[::-1,::-1]
print("The reversed center 3x3 is:\n",rev_arr_3x3)

arr_2 = arr[0:2,-2:]
print("The first 2 rows and last 2 columns: \n",arr_2)

arr_flat = arr.flatten()
print("The all elements of the array in a single line: \n",arr_flat)