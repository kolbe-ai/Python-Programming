"""
Write a Python program to implement a decorator that performs two tasks:
it should log the function name every time a function is called and also calculate how long the function takes to execute.
The log information (function name and execution time) should be stored in a text file named function_log.txt using file operations.
"""

import time

def log_reg(func):
    def wrapper():
        start_time = time.time()
        result= func()
        stop_time = time.time()
        execution_time = stop_time - start_time

        with open("file_log_python.txt","a") as f:
            f.write(f"Function name: {func.__name__}\nExecution time: {execution_time}\n\n")
        return result
    return wrapper

@log_reg
def process1():
    print("Hello how are you")

@log_reg
def process2():
    print("Good to see you")
process1()
process2()

with open("file_log_python.txt","r") as f:
    print(f.read())