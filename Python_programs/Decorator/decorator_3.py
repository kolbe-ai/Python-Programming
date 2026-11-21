"""
(Decorator with Arguments) 🚫 Out of PDF. Write a decorator that runs a function 3 times: @repeat(3).
"""

def repeat(num):
  def decorator(func):
    def wrapper(*args):
      for i in range(num):
          print(i)
          func(*args)
    return wrapper
  return decorator

@repeat(3)
def greet():
  print("Hello")

greet()
