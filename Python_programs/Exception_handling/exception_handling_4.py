"""
Write a function using raise to re-raise an exception after logging it.
"""

def check():
    return 10/0

try:
    check()
except ZeroDivisionError as e:
    print(e)
    raise