"""
Create a 1D NumPy array of integers from 0 to 9. Display its shape,
size, and data type and reshape it into 2*5.
"""

import numpy as np
arr = np.arange(10)
print(f"The array shape: {arr.shape}")
print(f"The array size: {arr.size}")
print(f"The array data type: {arr.dtype}")
resize_arr = arr.reshape(2,5)
print(f"The reshaped array: \n{resize_arr}")