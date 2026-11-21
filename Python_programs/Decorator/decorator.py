"""
(Decorator: Function Decorator) [PDF Q59] Write a decorator @timer that prints how long a function takes.
Apply it to a function that sums 1 to 1,000,000.
"""

import time
def decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print("The total time take is: ",(end_time - start_time))
        return result
    return wrapper

@decorator
def time_sum():
    i = 0
    while(i != 1000000):
        i+=1

time_sum()