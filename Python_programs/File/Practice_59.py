59. Write a decorator that logs the function name each time the function is called and measures its execution time.
Store both in a text file named function_log.txt using file operations.
"""

import time

def decorator(func):

    def wrapper(*args):
        print(f"Function name: {func.__name__}")
        exc_time = time.time()
        result = func(*args)
        exit_time = time.time()
        time_take = exit_time - exc_time
        print(f"The execution time is: {time_take:.6f} seconds")
        with open ("function_log.txt","a") as f:
            f.write(f"\n\nFunction Name: {func.__name__}\t Execution time: {time_take:.7f} seconds")
        return result

    return wrapper

@decorator
def welcome():
    print("Hello how are you!")

welcome()



























