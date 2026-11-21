"""
Write a program to create a NumPy array with 10 random integers
and determine their mean and standard deviation
"""

import numpy as np

array = np.random.randint(0,1000,size = 10)
print(f"Array is: {array}")
mean = array.mean()
sd = array.std()
print("Mean of array is: ",mean)
print("Standard deviation of array is: ",sd)