"""
Make an array of 8 random integers from 10 to 50 and print the mean, standard deviation, and values above the mean.
"""
import numpy as np
import random

arr = np.random.randint(10,50, 8)
print("Array is: ",arr)
print("Mean is: ",arr.mean())
print("Standard division is: ",arr.std())
above = arr[arr>arr.mean()]
print("Values above the sum is: ",above)