"""
Imagine you want to see how long your code takes to run without writing time.time() manually every time.
We can build a context manager that automatically starts a timer when entering a block and prints the total time when leaving it!
"""

import time

class Check:
  def __init__(self,num):
    self.start = 0
    self.num = num
    self.end = 0
    self.total_time = 0
  def __enter__(self):
    self.start = time.time()
    return self
  def __exit__(self,a,b,c):
    self.end = time.time()
    self.total_time = self.end - self.start
    print("Total time take: ",self.total_time)

with Check(1000) as timer:
  for i in range(1000):
    print(i)

print("Time taken is: ",timer.total_time)





