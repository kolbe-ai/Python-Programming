#45. Create a NumPy array of 10 random integers and find its mean and standard deviation.

import numpy as np
import random

arr1 = np.random.randint(1,100,10)
print("Random array is: ",arr1)

arr_mean = arr1.mean()
print("\n\nMean of array is: ",arr_mean)  #or can use np.mean(arr1)
arr_std = arr1.std()
print("\n\nStandard deviation of array is: ",arr_std)  #or can ue np.std(arr1)


