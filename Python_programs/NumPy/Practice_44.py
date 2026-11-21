#44. Create a 1D NumPy array of integers from 0 to 9, display its shape, size and data type, then reshape it to 2×5.

import numpy as np

arr1 = np.arange(0,10)
print("Array 1D is: ",arr1)
print("Shape: ",arr1.shape)
arr2 = arr1.reshape(2,5)
print("\n\nArray 2x5 is: \n",arr2)