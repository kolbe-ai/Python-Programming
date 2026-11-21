"""
Create a 4×4 array and print the diagonal and the array flipped vertically using slicing.
"""

import numpy as np

arr = np.arange(0,16).reshape(4,4)
print("Array is: \n",arr)

arr_dia = arr.diagonal()
print("\n\nArray is: \n",arr_dia)

print("\n\nThe array flipped vertically: \n",arr[:,::-1])