"""
Q25. Create a function calculator(operation, *args) that performs:

"add": returns the sum of args
"mul": returns the product of args
"avg": returns the average of args
"""

def calculator(op,*args):
  result = 0
  if op == "add":
    for i in args:
      result+= i
  elif op == "mul":
    mul = 1
    for i in args:
      mul *= i
    result = mul
  else:
    for i in args:
      result+= i
    result = result/len(args)
  return result

c = calculator("mul",1,2)
print(c)