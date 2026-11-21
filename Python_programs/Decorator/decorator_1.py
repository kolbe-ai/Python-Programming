"""
Decorator: Logging + File Handling) [PDF Q59] Write a decorator @log_call that appends function name and arguments to activity.txt.
"""

def log_call(func):
  def wrapper(*args):
    with open("activity.txt","a") as f:
      f.write(f"Function name: {func.__name__}")
      f.write(f"Argument is : {str(args)}")

    result = func(*args)
    return result
  return wrapper

@log_call
def sum_all(*args):
  return sum(args)

sum_all(1,2,3,4,5)
