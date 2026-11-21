#43. Perform element-wise addition, subtraction, multiplication and division on two matrices.

import numpy as np
import random

arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr2 = np.array([[4,3,2,1],[4,3,2,1]])

print("\nArray addition:\n",(arr1+arr2))
print("\nArray subtraction: \n",(arr1-arr2))
print("\nArray multiplication: \n",(arr1*arr2))
print("\nArray division: \n",(arr1/arr2))