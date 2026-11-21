"""
Write a function to collect n numbers during the function call and print the numbers that are not a multiple of the number 7.
"""

def check(*args):
  for i in args:
    if(i%7 == 0):
      continue
    print(i,end=" ")


check(14,28,32,7,7,7,7,7,7,1,2,3,4,5,6,7,8,9,8,6,5,6,6,6,5,4,56,7876,
      54,6,76,54,3,678,76543,34543,56,43,45,6,543,456,76543,2,3456,54,345,6543,4567,8765,789,876,5,7876,54)