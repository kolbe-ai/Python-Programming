"""
46. Create a 5×5 array with numbers 1 to 25 and use slicing to:
(a) print the center 3×3 part,
(b) print the reverse of that part,
(c) print the first 2 rows and last 2 columns,
(d) print all elements in a single line.
"""

import numpy as np
arr = np.arange(1,26).reshape(5,5)
print("Array is: \n",arr)

#a
print("\n\nThe center 3x3 part of the arr is: \n",arr[1:4,1:4])

#b
arr_rev = arr[1:4,1:4]
print("\n\nThe center 3x3 reversed part is of the array is: \n",arr_rev[::-1,::-1])      #reverse of both

#c
print("\n\nFirst 2 rows and last 2 columns of the array is: \n",arr[0:2,-2:])

#d
arr_flat = arr.flatten()
print("\n\nSingle lined array is : ",arr_flat)